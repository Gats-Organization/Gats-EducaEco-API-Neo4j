from flask import Flask, request, jsonify
from neo4j import GraphDatabase
from config import Config
import os

app = Flask(__name__)

uri = Config.NEO4J_URI
driver = GraphDatabase.driver(uri, auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD))



#Tela de Vídeos
# Rota para incrementar o contador de tela
@app.route('/incrementar-contador-videos-vistos', methods=['POST'])
def incrementar_contador_videos_vistos():
    data = request.get_json()
    email_aluno = data.get("email_aluno")

    with driver.session() as session:
        session.run("""
            MERGE (a:Aluno {email: $email_aluno})
            ON CREATE SET a.videos_vistos = 1, a.vezes_jogadas = 0
            ON MATCH SET a.videos_vistos = a.videos_vistos + 1
        """, email_aluno=email_aluno)

    return jsonify({"email_aluno": email_aluno, "mensagem": "Contador de vídeos vistos incrementado com sucesso!"})

# Rota para verificar o contador
@app.route('/verificar-contador-videos-vistos/<email_aluno>', methods=['GET'])
def verificar_contador_videos_vistos(email_aluno):
    with driver.session() as session:
        result = session.run("MATCH (a:Aluno {email: $email_aluno}) RETURN a.videos_vistos AS videos_vistos",
                             email_aluno=email_aluno)
        record = result.single()

    if record is None:
        return jsonify({"error": "Aluno não encontrado"}), 404

    return jsonify({"email_aluno": email_aluno, "videos_vistos": record["videos_vistos"]})


#Tela de Jogos
# Rota para incrementar o contador de tela@app.route('/incrementar-contador-videos-vistos', methods=['POST'])
@app.route('/incrementar-contador-vezes-jogadas', methods=['POST'])
def incrementar_contador_vezes_jogadas():
    data = request.get_json()
    email_aluno = data.get("email_aluno")

    with driver.session() as session:
        session.run("""
            MERGE (a:Aluno {email: $email_aluno})
            ON CREATE SET a.vezes_jogadas = 1, a.videos_vistos = 0
            ON MATCH SET a.vezes_jogadas = a.vezes_jogadas + 1
        """, email_aluno=email_aluno)

    return jsonify({"email_aluno": email_aluno, "mensagem": "Contador de vezes jogadas incrementado com sucesso!"})

# Rota para verificar o contador
@app.route('/verificar-contador-vezes-jogadas/<email_aluno>', methods=['GET'])
def verificar_contador_vezes_jogadas(email_aluno):
    with driver.session() as session:
        result = session.run("MATCH (a:Aluno {email: $email_aluno}) RETURN a.vezes_jogadas AS vezes_jogadas",
                             email_aluno=email_aluno)
        record = result.single()

    if record is None:
        return jsonify({"error": "Aluno não encontrado"}), 404

    return jsonify({"email_aluno": email_aluno, "vezes_jogadas": record["vezes_jogadas"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
