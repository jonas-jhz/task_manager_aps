# Análise inicial

## Estado real

Projeto é aplicação desktop Tkinter com persistência SQLite e testes unittest.

- Ponto de entrada: `main.py`.
- Interface: `views/main_window.py`.
- Persistência: `database.py` (`TaskDatabase`).
- Entidades: `models/task.py` e `models/category.py`.
- Configuração: `config/settings.py`.
- Exportação e validação: `utils/data_export.py` e `utils/validators.py`.
- Testes: `tests/test_task.py` e `tests/test_database.py`.

## Execução confirmada

- Testes baseline: 18 aprovados em 0,439 s.
- Inicialização: `python main.py` criou `data/tasks.db`, iniciou `TaskManagerApp` e entrou no loop principal.
- Interface foi encerrada manualmente após confirmar a inicialização.

## Arquitetura identificada

A organização usa entidades, visão Tkinter e banco de dados direto. `TaskManagerApp` concentra menus, widgets, filtros, validação e coordenação de operações. `TaskDatabase` concentra schema, migrações e SQL.

## Problemas reais identificados

1. `TaskManagerApp` conversa diretamente com `TaskDatabase` em CRUD e filtros.
2. Construção de `Task` ocorre na interface e pode ficar distribuída em diálogos e importações.
3. Alteração de status não oferece mecanismo de inscrição para componentes interessados.
4. `main.py` mantém apenas inicialização direta da aplicação.
5. Cobertura antes das mudanças não havia sido medida.

## Melhorias implementadas

- Simple Factory centraliza criação e normalização de tarefas.
- Facade concentra criação, atualização, exclusão e mudança de status.
- Observer permite inscrição e notificação de eventos de tarefa.
- UI passa a usar `TaskFacade` para casos de uso principais.
- Testes novos demonstram RED, GREEN e observer em execução.
