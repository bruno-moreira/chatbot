from flask import Flask, jsonify
from robo import *

servico = Flask("bot_monitor")

configurado, robo = configurar()

@servico.get("/bot_monitor/info")
def get_informacoes():
    return jsonify(
        descricao = "Robô de informações sobre zabbix & grafana",
        email = "moreira.bruno10@gmail.com",
        versao = "1.0",
        robo_online = configurado
    )

@servico.get("/resposta/<string:mensagem>")
def get_resposta(mensagem):
    resposta = robo.get_response(mensagem)

    return jsonify(
        resposta = resposta.text,
        confianca = resposta.confidence
    )

if __name__ == "__main__":
    servico.run(debug=True)