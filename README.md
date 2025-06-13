## Dependências

- Python v3.9
- Docker
- Git

## Exercicio 1
```sh
$ /tinnova-teste-python/exerc-1/src/entites/Voters.py
```

Resolução Votos em relação ao total de eleitores

## Exercicio 2
```sh
$ /tinnova-teste-python/exerc-2/src/entites/main.py
```

Algoritmo de ordenação Bubble Sort

## Exercicio 3
```sh
$ /tinnova-teste-python/exerc-3/src/entites/main.py
```

Fatorial

## Exercicio 4
```sh
$ /tinnova-teste-python/exerc-4/src/entites/main.py
```

Soma dos multiplos de 3 ou 5

## Exercicio 5

Resolução Cadastro de veículos

## Instalação MacOS & Linux

```sh
$ git clone git@github.com:Rap255/tinnova-teste-python.git
$ cd tinnova-teste-python
```

1. Execute os comandos abaixo:

```sh
$ cd exerc-5-django
$ cd src
$ docker build -t django-python .
$ docker run -it django-python
```
OBS.: Caso seu editor de código reclame da falta de bibliotecas, crie um ambiente virutal e instale via pip

Para acessar o Swagger e acessar a API:
http://localhost:8000/swagger/

Alternativa 
```sh
$ python -m virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python manage.py collectstatic --no-input
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Instalação Windows

```cmd
> git clone https://github.com/Rap255/tinnova-teste-python.git
> cd tinnova-teste-python
```

1. Execute os comandos abaixo:

OBS.: Caso seu editor de código reclame da falta de bibliotecas, crie um ambiente virutal e instale via pip
```cmd
> python -m virtualenv env
> .env\scripts\activate
> pip install -r requirements.txt
```

Alternativa 
```cmd
> python -m virtualenv env
> .env\scripts\activate
> pip install -r requirements.txt
> python manage.py collectstatic --no-input
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver 0.0.0.0:8080
```

Para acessar o Swagger e acessar a API:
http://localhost:8080/swagger/

## Possíveis errors

No caso de saída 1 no web server, altere o fim de sequência de linhas (End of line sequences) no arquivo "Dockerfile" ou arquivos '.sh'. Se você está utilizando o Visual Studio Code, segure "ctrl+shift+P" e digite "Change End Of Line Sequence", clique e altere "CRLF" para "LF"