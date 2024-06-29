from codigo.bytebank import Funcionario
from datetime import datetime

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
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, "11/11/2000", 1111)
        resultado = lucas.sobrenome() # When
        assert resultado == esperado
