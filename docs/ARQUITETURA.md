# Arquitetura

## Estado original

Camadas:

- Entrada: `main.py`.
- Interface: `views/main_window.py`.
- Regras e entidade: `models/`.
- Persistência: `database.py`.
- Utilitários: `utils/`.
- Configuração: `config/`.

A interface chamava diretamente `TaskDatabase` para operações CRUD. Isso preservava MVC-esque separação, mas fazia `TaskManagerApp` coordenar vários componentes.

## Estado final

Novos componentes:

- `application/task_facade.py`: controller de casos de uso de tarefa.
- `application/task_observer.py`: abstração comportamental para eventos.
- `models/task_factory.py`: criação centralizada.

Fluxo: `TaskManagerApp` → `TaskFacade` → `TaskRepository`/`TaskDatabase` → SQLite. Eventos: `TaskFacade` → `TaskObserver`.

## SOLID

- SRP: `TaskFactory` cria tarefas; `TaskFacade` coordena casos de uso; `TaskDatabase` persiste.
- OCP: novos observadores podem ser adicionados sem modificar a fachada.
- DIP: a fachada depende do protocolo `TaskRepository`, não de uma classe específica além da capacidade mínima.

## GRASP

- Controller: `TaskFacade` recebe intenção de caso de uso e coordena especialistas.
- Information Expert: `TaskDatabase` conhece SQL e persistência; `Task` conhece validação e representação própria.
