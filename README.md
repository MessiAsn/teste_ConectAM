# Teste de Formulário com Selenium

Este projeto é um exemplo de teste automatizado de formulário usando **Selenium** em **Python**. Ele preenche automaticamente os campos de um formulário HTML e testa diferentes cenários de validação.

---

## Descrição

O código realiza testes em um formulário HTML para verificar se os campos obrigatórios (nome, e-mail, telefone e mensagem) são validados corretamente. Três cenários principais são testados:

1. **E-mail válido e telefone inválido.**
2. **Telefone válido e e-mail inválido.**
3. **Todos os dados válidos.**

---

## Configuração

No arquivo `teste_ConectAM.py`, altere a linha:

```python
driver.get("http://127.0.0.1:5500/IHM/index.html")
```
Para o caminho do seu arquivo HTML local, por exemplo:
```
driver.get("file:///C:/meu-projeto/IHM/index.html")
```
