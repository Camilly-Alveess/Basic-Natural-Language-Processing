# Ferramenta de Processamento de Texto

A aplicação é uma ferramenta de processamento de texto que utiliza técnicas de NLP (Processamento de Linguagem Natural) para realizar várias operações, como tokenização, identificação de entidades nomeadas, análise de sentenças, extração de tópicos e resumo automático de texto.

## Funcionalidades

- **Tokenização:** Divide o texto em palavras ou frases.
- **Identificação de Entidades Nomeadas (NER):** Reconhece e classifica entidades importantes no texto, como pessoas, organizações e locais.
- **Análise de Sentenças:** Separa o texto em sentenças individuais.
- **Extração de Tópicos:** Identifica tópicos principais presentes no texto.
- **Resumo Automático:** Gera um resumo conciso do texto original.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - spaCy
  - Gensim
  - Sumy
  - ReportLab
  - Tkinter

## Estrutura do Projeto

- **main.py:** Arquivo principal que coordena a execução da ferramenta.
- **file_utils.py:** Módulo para carregar texto de um arquivo.
- **gensim_utils.py:** Módulo para extração de tópicos usando Gensim.
- **report_utils.py:** Módulo para montagem do relatório em formato PDF.
- **spacy_utils.py:** Módulo para tokenização, identificação de entidades e análise de sentenças usando spaCy.
- **sumy_utils.py:** Módulo para resumo automático usando Sumy.
- **user_interface.py:** Módulo para interação com o usuário usando Tkinter.

## Como Usar

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter instalado todas as dependências listadas nos requisitos.
3. Execute o arquivo `main.py` para iniciar a ferramenta.
4. Escolha entre inserir um texto manualmente ou carregar de um arquivo.
5. A ferramenta processará o texto e gerará um relatório em formato PDF com os resultados.




* Este projeto foi desenvolvido por *Camilly Alves*.

Sugestões são sempre bem-vindas! =)
