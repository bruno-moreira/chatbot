import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):
    def setUp(self):
        self.configurado, self.robo = configurar()

    def testar_01_robo_configurado(self):
        self.assertTrue(self.configurado)

    def testar_02_saudacoes_basicas(self):
        saudacoes = ["oi", "olá", "ola", "tudo bem?", "como vai?", "Como vai? Tudo bem?"]

        for saudacao in saudacoes:
            print(f"Testando a saudação: {saudacao}")

            resposta = self.robo.get_response(saudacao)

            print(f"Obtendo a confiança: {resposta.confidence}")
            print(f"Texto da resposta: {resposta.text}")

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Olá, sou o robô de informação sobre serviços de monitoramento. Como posso te ajudar?", resposta.text)

class TesteInformacoes(unittest.TestCase):
    def setUp(self):
        self.configurado, self.robo = configurar()

    def testar_01_robo_configurado(self):
        self.assertTrue(self.configurado)

    def testar_02(self):
        perguntas = ["O que é Zabbix?", "Zabbix faz o que?", "Zabbix o que é?"]

        for pergunta in perguntas:
            print(f"Perguntando: {pergunta}")

            resposta = self.robo.get_response(pergunta)
            print(f"Confiança da resposta: {resposta.confidence}")
            print(f"Texto da resposta: {resposta.text}")

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O Zabbix é uma plataforma de software open-source para monitoramento de redes", resposta.text)
            
    def testar_03(self):
        perguntas = ["Qual relação entre Zabbix e grafana?", "O que tem a ver Zabbix e Grafana?", "Como são relacionados?"]

        for pergunta in perguntas:
            print(f"Perguntando: {pergunta}")

            resposta = self.robo.get_response(pergunta)
            print(f"Confiança da resposta: {resposta.confidence}")
            print(f"Texto da resposta: {resposta.text}")

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("O Grafana pode ser integrado ao Zabbix utilizando plugins específicos, permitindo que os dados coletados.", resposta.text)
            
    def testar_04(self):
        perguntas = ["Quais são os benefícios de integrar zabbix com grafana?", "O que tenho a ganhar com os dois juntos?", "Por que juntar o Zabbix com Grafana?" ]

        for pergunta in perguntas:
            print(f"Perguntando: {pergunta}")

            resposta = self.robo.get_response(pergunta)
            print(f"Confiança da resposta: {resposta.confidence}")
            print(f"Texto da resposta: {resposta.text}")

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Visualização Avançada: Enquanto o Zabbix possui suas próprias ferramentas de visualização, o Grafana é conhecido por suas capacidades avançadas de criação de gráficos e dashboards", resposta.text)
            
    def testar_05(self):
        perguntas = ["Como configurar a integração entre zabbix e grafana?", "Integrar Zabbix com Grafana?", "Como configurar os dois?"]

        for pergunta in perguntas:
            print(f"Perguntando: {pergunta}")

            resposta = self.robo.get_response(pergunta)
            print(f"Confiança da resposta: {resposta.confidence}")
            print(f"Texto da resposta: {resposta.text}")

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("https://medium.com/zabbix-brasil/integrando-zabbix-e-grafana-d46de4d1526d#:~:text=A%20integra%C3%A7%C3%A3o%20entre%20as%20ferramentas,consumir%20a%20API%20do%20Zabbix.", resposta.text)

    def testar_06(self):
        perguntas = ["Grafana?", "Faz o que Grafana?", "Grafana é uma ferramenta?"]

        for pergunta in perguntas:
            print(f"Perguntando: {pergunta}")

            resposta = self.robo.get_response(pergunta)
            print(f"Confiança da resposta: {resposta.confidence}")
            print(f"Texto da resposta: {resposta.text}")

            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Grafana é uma plataforma open-source amplamente utilizada para a visualização e análise de dados.", resposta.text)

if __name__ == "__main__": 
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)
