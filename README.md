# chat-serv

![](https://github.com/taniodev/chat-serv/workflows/python_ci/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/taniodev/chat-serv/branch/master/graph/badge.svg?token=YhWQsLyu4w)](https://codecov.io/gh/taniodev/chat-serv)

Um simples servidor de bate-papo via telnet escrito em Python usando AsyncIO

Este servidor aceita várias conexões simultâneas de clientes telnet.
Cada cliente pode definir um nickname único que é utilizado para identificação.

Existe um comando disponível para fazer a troca de nick enquanto estiver conectado:

`/nome novo-nick`

Também é possível enviar mensagens privadas para um cliente específico, basta saber o nickname do destinatário. Suponha um cliente com o nick *fulano*:

`/fulano Tudo bem?`

## Instalação

Você precisa ter o pipenv instalado para gerenciar as dependências do projeto:

`$ pip install pipenv`

Instale as dependências do projeto:

`pipenv sync -d`

Copie o arquivo *contrib/env-sample* para a raíz do projeto nomeando-o como *.env*:

`cp contrib/env-sample .env`

Você pode editar o arquivo *.env* e definir as opções de acordo com as suas necessidades.

## Testes e verificação do código

Para rodar os testes execute o seguinte comando em um terminal:

`pytest .`

Para rodar o flake8 em busca de problemas no código:

`flake8 .`
