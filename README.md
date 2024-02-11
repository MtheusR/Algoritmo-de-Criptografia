# Projeto de Criptografia

Este é um projeto de criptografia desenvolvido em Python que oferece funcionalidades básicas de criptografia e descriptografia de texto usando códigos binários.

## Visão Geral

O projeto consiste em vários arquivos que desempenham funções específicas:

- `arquivo_main.py`: O arquivo principal do projeto, onde a interação com o usuário ocorre. Ele solicita ao usuário que insira o texto a ser criptografado e oferece a opção de descriptografar o texto, se desejado.

- `arquivo_chave_bits.py`: Este arquivo é responsável pela geração de tabelas de caracteres e seus códigos binários para uso na criptografia.

- `arquivo_cripto_bits.py`: Este arquivo contém funções para criptografar e descriptografar o texto, bem como funções auxiliares para manipular os códigos binários.

- `arquivo_funcoes.py`: Um arquivo que contém diversas funções úteis para o projeto, como limpar o console e imprimir mensagens de sucesso.

- `arquivo_gerador.py`: Este arquivo gera as combinações binárias e as escreve em um arquivo CSV para uso posterior.

## Pré-requisitos

Certifique-se de ter Python instalado em seu sistema. Além disso, o projeto faz uso das bibliotecas `tqdm` e `colorama`. Você pode instalá-las executando:

```
pip install tqdm colorama
```

## Como usar

1. Clone o repositório para o seu sistema local.

2. Navegue até o diretório do projeto.

3. Execute o arquivo `arquivo_main.py` para iniciar o programa.

4. Siga as instruções fornecidas no console para criptografar ou descriptografar texto.
