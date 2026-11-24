# Changelog — models

## 2026-11-24 — centralized task creation

### Arquivos afetados
- `task_factory.py`

### Adicionado
- `TaskFactory.create(...)`: fabrica tarefas normalizando descrição e categoria.
- Normalização remove espaços da descrição e substitui categoria vazia por `General`.

### Modificado
- Nenhum modelo existente foi alterado diretamente.

### Removido
- Nenhum arquivo removido.

### Justificativa técnica
A criação direta de `Task` estava distribuída na interface e podia assumir diferentes valores padrão. A fábrica concentra essa regra em um ponto extensível.

### Padrões e princípios relacionados
- Simple Factory.
- SRP.
- OCP.

### Validação
- Teste confirma que descrição com espaços é normalizada.
- Suite completa: 20 testes aprovados.
