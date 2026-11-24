# Métricas

## Testes e cobertura

Comando:

```powershell
python -m coverage erase
python -m coverage run -m unittest discover -s tests
python -m coverage report -m
python -m coverage html
```

Resultado: 20 testes aprovados. Cobertura total: 79% sobre 642 statements, 134 não cobertos.

Arquivos relevantes:

| Arquivo | Cobertura |
|---|---:|
| `models/task_factory.py` | 100% |
| `config/settings.py` | 100% |
| `application/task_observer.py` | 90% |
| `models/task.py` | 87% |
| `application/task_facade.py` | 63% |
| `database.py` | 62% |

Relatório HTML: `htmlcov/index.html`.

## Complexidade ciclomática

Comando:

```powershell
python -m radon cc . -s -a --exclude '.venv,venv,data,htmlcov'
```

Radon classificou `TaskDatabase._migrate_v1_to_v2` como nível C com complexidade 11, maior do projeto listado. `DataExporter.export_to_csv` teve complexidade 5. Métodos principais das novas classes ficaram entre A e B.

## Acoplamento

- Dependência original: `views.main_window` importava diretamente `database`, `Task`, validação e exportação.
- Ação: novas operações CRUD passaram por `application.task_facade.TaskFacade`.
- Persistência continua implementada por `TaskDatabase` e não foi substituída.
- `TaskFacade` depende de um protocolo mínimo de repositório, reduzindo acoplamento concreto ao banco.
- `TaskObserver` usa uma interface abstrata, permitindo novos observadores sem alterar a fachada.
- `database.TaskDatabase` continua com forte responsabilidade por schema, SQL e migração. O acoplamento é real, mas não circular.
