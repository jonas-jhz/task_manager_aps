# Changelog — views

## 2026-11-24 — UI routed through application facade

### Arquivos afetados
- `main_window.py`

### Adicionado
- Importação de `TaskFacade` e `TaskFactory`.
- Inicialização de `task_service` junto ao banco.

### Modificado
- `add_task`: agora chama `task_service.create_task(...)`.
- `edit_task`: agora chama `task_service.update_task(...)`.
- `delete_task`: agora chama `task_service.delete_task(...)`.
- `mark_complete`: agora chama `task_service.complete_task(...)`.
- `mark_incomplete`: agora chama `task_service.incomplete_task(...)`.
- `TaskDialog.save`: criação nova usa `TaskFactory.create(...)`.

### Removido
- Chamadas diretas de criação, atualização, exclusão e status foram substituídas nos cinco fluxos de tarefa.
- Construção direta nova de `Task` no diálogo foi removida.

### Justificativa técnica
A interface deixa de coordenar múltiplas regras de aplicação manualmente. Diferença real no diff: 26 linhas adicionadas e 18 removidas em `main_window.py`.

### Padrões e princípios relacionados
- Facade.
- Simple Factory.
- SRP.
- DIP.
- GRASP Controller.

### Validação
- Nenhum diagnóstico Pylance nos arquivos alterados.
- 20 testes aprovados.
- Inicialização real da aplicação já havia sido confirmada antes das mudanças; reiniciar após conclusão para demonstração final.
