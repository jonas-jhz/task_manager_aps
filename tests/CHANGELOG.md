# Changelog — tests

## 2026-11-24 — GoF and TDD evidence

### Arquivos afetados
- `test_application_patterns.py`

### Adicionado
- `RecordingObserver` para capturar eventos.
- Teste de criação normalizada pela fábrica.
- Teste de inscrição e notificação ao concluir tarefa.

### Modificado
- Nenhum teste existente foi alterado.

### Removido
- Nenhum arquivo removido.

### Justificativa técnica
A nova suíte prova o comportamento mínimo da fábrica e do Observer, além de funcionar como evidência TDD.

### Padrões e princípios relacionados
- Simple Factory.
- Observer.
- TDD.

### Validação
- RED: `ModuleNotFoundError` para `models.task_factory`.
- GREEN: 2 testes do novo módulo aprovados.
- Final: 20 testes aprovados.
