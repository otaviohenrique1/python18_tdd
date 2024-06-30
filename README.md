# python18_tdd

Projeto do curso "Python e TDD: explorando testes unitários" da Alura

## Links

- [Python](https://www.python.org/)

## Comandos

### Criar venv

- python -m virtualenv .venv

### Ativar venv

- venv\scripts\activate
- venv/scripts/activate
- source venv\scripts\activate
- source venv/scripts/activate

### Desativar venv

- deactivate

### Pacotes

- pip install virtualenv
- pip install pytest
- pip install pytest-cov

## Exibir pacotes instalados

- pip freeze
- pip freeze > requirements.txt

## Instalar pacotes

- pip install -r requirements.txt

### Comandos para inicializar o projeto

1. python -m virtualenv .venv
2. source .venv/scripts/activate
3. pip install -r requirements.txt

### Comandos para testar o projeto

1. pytest -v
2. pytest -v -m calcular_bonus
3. pytest --cov=codigo tests/
4. pytest --cov=codigo tests/ --cov-report term-missing
5. pytest --cov=codigo tests/ --cov-report html
6. pytest --junitxml report.xml
7. pytest --cov-report xml
