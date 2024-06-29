import pytest
from codigo.bytebank import Funcionario
from datetime import datetime
from pytest import mark

# from datetime import date

# import sys
# sys.path.append('caminho/para/o/diretório')


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000"  # Given-Contexto
        esperado = int(datetime.now().strftime("%y"))
        # esperado2 = date.today().year - 2000
        funcionario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcionario_teste.idade()  # when-Ação
        assert resultado == esperado  # Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = " Lucas Carvalho "  # Given
        esperado = "Carvalho"
        lucas = Funcionario(entrada, "11/11/2000", 1111)
        resultado = lucas.sobrenome()  # When
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = "Paulo Bragança"
        esperado = 90000
        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        funcionario_teste.decrecimo_salario()  # when
        resultado = funcionario_teste.salario
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100
        funcionario_teste = Funcionario("teste", "11/11/2000", entrada)
        resultado = funcionario_teste.calcular_bonus()  # when
        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000  # given
            funcionario_teste = Funcionario("teste", "11/11/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()  # when
            assert resultado #then
