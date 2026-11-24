# Evidências de TDD

## Funcionalidade

Criação normalizada de tarefa e notificação ao concluir tarefa.

## RED

Foi criado `tests/test_application_patterns.py` antes das classes de produção.

Execução:

```text
python -m unittest tests.test_application_patterns -v
ModuleNotFoundError: No module named 'models.task_factory'
FAILED (errors=1)
```

Falha esperada: a fábrica ainda não existia.

## GREEN

Implementados:

- `models/task_factory.py`: criação centralizada de `Task`.
- `application/task_observer.py`: evento e interface de observador.
- `application/task_facade.py`: coordenação e publicação de eventos.

Execução:

```text
Ran 2 tests
OK
```

## REFACTOR

A interface passou a usar `TaskFacade`, e o diálogo passou a usar `TaskFactory` em criação. A suíte completa manteve aprovação.

Resultado final: 20 testes aprovados.
