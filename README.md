# Projeto de Automação com PyAutoGUI e Pandas

Este projeto utiliza a biblioteca `pyautogui` para automatizar tarefas no computador e a biblioteca `pandas` para manipulação de dados em arquivos CSV. O objetivo é automatizar o preenchimento de um formulário em um site usando dados armazenados em um arquivo CSV.

## Requisitos

Antes de executar o projeto, é necessário instalar as bibliotecas Python necessárias. Você pode instalar as dependências com os seguintes comandos:

```bash
pip install pyautogui pandas numpy openpyxl
```

## Funcionalidade

- O script realiza as seguintes ações:

1. Abre o navegador Chrome.
2. Acessa um link específico.
3. Preenche um formulário de login com um e-mail e senha fornecidos.
4. Lê os dados de um arquivo CSV (produtos.csv).
5. Preenche um formulário baseado em cada linha do CSV com informações do produto (código, marca, tipo, categoria, preço unitário, custo e observações).

## Nota

- Posições de clique: As posições de clique são específicas para a configuração atual da tela e podem precisar ser ajustadas conforme a resolução ou layout do seu sistema.
- Dependências: Certifique-se de que todos os arquivos necessários (por exemplo, produtos.csv) estão disponíveis no mesmo diretório que o script.

## Licença
Este projeto está disponível sob a licença MIT (ou outra licença de sua escolha).

## Contribuição
Se você tiver sugestões ou melhorias para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório do GitHub.

**Nota:** Substitua https://github.com/usuario/repo pelo link real do seu repositório GitHub e adicione um arquivo de licença (LICENSE) se necessário.
