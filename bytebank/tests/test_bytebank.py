from codigo.bytebank import Funcionario
from datetime import datetime
# from datetime import date

# import sys
# sys.path.append('caminho/para/o/diretório')

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000" # Given-Contexto
        esperado = int(datetime.now().strftime("%y"))
        # esperado2 = date.today().year - 2000
        funcioinario_teste = Funcionario("Teste", entrada, 1111)
        resultado = funcioinario_teste.idade() #when-Ação
        assert resultado == esperado #Then-Desfecho
        