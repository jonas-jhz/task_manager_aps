# Relatório técnico de mudanças

## Resumo executivo

O projeto continuou desktop, Tkinter e SQLite. Estado inicial tinha 18 testes aprovados e interface direta com banco. Foram adicionados Simple Factory, Facade e Observer, além de 2 testes TDD.

Estado final: 20 testes aprovados, cobertura 79%, 3 PlantUML editáveis e documentação por pasta.

## Arquitetura original

- `main.py` cria `tk.Tk` e `TaskManagerApp`.
- `TaskManagerApp` monta widgets, valida entrada, cria `Task`, consulta categorias e chama `TaskDatabase`.
- `TaskDatabase` executa SQL e cria objetos de modelo.
- `TaskDialog` cria diretamente `Task` para tarefas novas.

Problema real: UI coordenava validação, criação e persistência sem um serviço de aplicação. Eventos de conclusão não tinham inscritos.

## Arquitetura final

- UI chama `TaskFacade`.
- `TaskFacade` cria pela fábrica, persiste no repositório e publica eventos.
- `TaskDatabase` implementa o protocolo mínimo de persistência.
- `TaskObserver` permite componentes externos responderem a eventos.

## Simple Factory

Categoria: criacional.

Antes:

```python
self.result = Task(
    description=self.description_var.get(),
    priority=self.priority_var.get(),
    category=self.category_var.get(),
    due_date=self.due_date_var.get() or None,
)
```

Depois:

```python
self.result = TaskFactory.create(
    description=self.description_var.get(),
    priority=self.priority_var.get(),
    category=self.category_var.get(),
    due_date=self.due_date_var.get() or None,
)
```

Localização: `models/task_factory.py`, usada em `views/main_window.py` e `application/task_facade.py`.

É Simple Factory porque centraliza uma família pequena de criação de `Task` e esconde normalização básica. Benefício: um ponto para validação futura e formatos de criação sem duplicar construção na interface.

## Facade

Categoria: estrutural.

Antes, `TaskManagerApp.add_task` chamava diretamente `TaskDatabase.insert_task`; edição, exclusão e status faziam chamadas diretas semelhantes.

Depois, `TaskManagerApp` usa `TaskFacade` para os cinco casos de uso. A fachada cria objetos pela fábrica, chama o repositório e publica eventos.

Localização: `application/task_facade.py` e chamadas em `views/main_window.py`.

Benefício: interface não precisa conhecer sequência completa ou detalhes de persistência. Mudanças futuras podem ser absorvidas pela fachada.

## Observer

Categoria comportamental.

Implementado em `application/task_observer.py`. `TaskFacade.subscribe` registra observadores; `_notify` entrega `TaskEvent` a uma cópia da lista.

Os eventos incluem criação, atualização, exclusão, conclusão e reabertura. Fluxo concluído: `TaskFacade.complete_task` persiste e envia `task_completed`.

Testado por `RecordingObserver` em `tests/test_application_patterns.py`.

## SOLID e GRASP

- SRP: fábrica cria, fachada coordena, banco persiste.
- OCP: novos observadores implementam `TaskObserver` sem mudar fachada.
- DIP: fachada declara `TaskRepository` como protocolo mínimo.
- GRASP Controller: `TaskFacade` controla casos de uso.
- GRASP Information Expert: `TaskDatabase` possui acesso aos dados e `Task` possui dados e comportamento próprio.

## Refatoração principal

Code smell: interface concentrava criação e coordenação de tarefas.

Técnica: Extract Service/Class e introdução de fachada/fábrica.

Realizado em `views/main_window.py`: 26 linhas adicionadas, 18 removidas. Chamadas diretas de CRUD nos métodos da interface foram substituídas por `task_service`.

Validação: teste completo 20/20 e nenhum diagnóstico nos arquivos alterados.

## TDD

RED: teste de fábrica falhou com `ModuleNotFoundError`.
GREEN: duas classes novas passaram a satisfazer os testes.
REFACTOR: UI passou a usar fábrica e fachada sem mudar comportamento observado.

Detalhes: `docs/EVIDENCIAS_TDD.md`.

## Métricas

Detalhes reais em `docs/METRICAS.md`.

- 20 testes aprovados.
- Cobertura total 79%.
- Maior complexidade destacada: `TaskDatabase._migrate_v1_to_v2`, 11, nível C.
- `TaskFactory.create` nível A; fachada principal nível A/B.

## UML

- `docs/diagramas/classes.puml`: entidades e componentes dos padrões.
- `docs/diagramas/sequencia_criacao_tarefa.puml`: UI → diálogo → fábrica → fachada → banco.
- `docs/diagramas/sequencia_conclusao_tarefa.puml`: UI → fachada → banco → observadores.

## Como executar e demonstrar

```powershell
python -m pip install -r requirements.txt
python main.py
python -m unittest discover -s tests -v
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
python -m radon cc . -s -a
```

Demonstração sugerida:

1. Criar tarefa pela interface.
2. Mostrar que criação passa pela fábrica e fachada no código.
3. Concluir tarefa e citar publicação `task_completed`.
4. Executar teste do observador.
5. Mostrar PlantUML e relatório de cobertura.

## Changelogs

- `application/CHANGELOG.md`
- `models/CHANGELOG.md`
- `views/CHANGELOG.md`
- `tests/CHANGELOG.md`

## Referências

- Repositório fork atual.
- Repositório original informado no projeto: https://github.com/saidurpulok/task_manager
- Documentação Python/Unittest/Tkinter/SQLite.
- Radon e Coverage.
