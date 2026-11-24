# Changelog — application

## 2026-11-24 — GoF structural and behavioral services

### Arquivos afetados
- `task_facade.py`
- `task_observer.py`
- `__init__.py`

### Adicionado
- `TaskFacade`: unifica CRUD de tarefas e publica eventos após operações.
- `TaskRepository`: protocolo mínimo usado pela fachada.
- `TaskObserver`: interface abstrata para observadores.
- `TaskEvent`: representa eventos com tipo, ID e descrição.
- Inscrição, remoção e notificação reais de observadores.

### Modificado
- Nenhum arquivo existente nesta pasta foi modificado.

### Removido
- Nenhum arquivo removido.

### Justificativa técnica
A interface não precisa conhecer detalhes de consulta e mudança de estado ao coordenar casos de uso. Observadores podem responder a conclusões sem acoplamento direto com `TaskDatabase`.

### Padrões e princípios relacionados
- Facade.
- Observer.
- SRP.
- DIP.
- GRASP Controller.

### Validação
- 20 testes aprovados.
- Teste específico confirma publicação de `task_completed` para observador inscrito.
