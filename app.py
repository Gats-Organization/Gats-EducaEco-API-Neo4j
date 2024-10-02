from flask import Flask, request, jsonify
from neo4j import GraphDatabase
from config import Config
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)  # Inicializa o Swagger na sua aplicação Flask

uri = Config.NEO4J_URI
driver = GraphDatabase.driver(uri, auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD))

# Tela de Vídeos
# Rota para incrementar o contador de tela
@app.route('/incrementar-contador-videos-vistos/<email_aluno>', methods=['POST'])
def incrementar_contador_videos_vistos(email_aluno):
    """
    Incrementa o contador de vídeos vistos do aluno
    ---
    parameters:
      - name: email_aluno
        in: path
        type: string
        required: true
        description: O email do aluno
    responses:
      200:
        description: Contador de vídeos incrementado com sucesso
        schema:
          type: object
          properties:
            email_aluno:
              type: string
            mensagem:
              type: string
    """
    with driver.session() as session:
        session.run("""
            MERGE (a:Aluno {email: $email_aluno})
            ON CREATE SET a.videos_vistos = 1, a.vezes_jogadas = 0
            ON MATCH SET a.videos_vistos = a.videos_vistos + 1
        """, email_aluno=email_aluno)

    return jsonify({"email_aluno": email_aluno, "mensagem": "Contador de vídeos vistos incrementado com sucesso!"})

# Rota para verificar o contador de vídeos vistos
@app.route('/verificar-contador-videos-vistos/<email_aluno>', methods=['GET'])
def verificar_contador_videos_vistos(email_aluno):
    """
    Verifica o contador de vídeos vistos do aluno
    ---
    parameters:
      - name: email_aluno
        in: path
        type: string
        required: true
        description: O email do aluno
    responses:
      200:
        description: Contador de vídeos vistos retornado com sucesso
        schema:
          type: object
          properties:
            email_aluno:
              type: string
            videos_vistos:
              type: integer
      404:
        description: Aluno não encontrado
    """
    with driver.session() as session:
        result = session.run("MATCH (a:Aluno {email: $email_aluno}) RETURN a.videos_vistos AS videos_vistos",
                             email_aluno=email_aluno)
        record = result.single()

    if record is None:
        return jsonify({"error": "Aluno não encontrado"}), 404

    return jsonify({"email_aluno": email_aluno, "videos_vistos": record["videos_vistos"]})


# Tela de Jogos
# Rota para incrementar o contador de jogos
@app.route('/incrementar-contador-vezes-jogadas/<email_aluno>', methods=['POST'])
def incrementar_contador_vezes_jogadas(email_aluno):
    """
    Incrementa o contador de vezes jogadas do aluno
    ---
    parameters:
      - name: email_aluno
        in: path
        type: string
        required: true
        description: O email do aluno
    responses:
      200:
        description: Contador de vezes jogadas incrementado com sucesso
        schema:
          type: object
          properties:
            email_aluno:
              type: string
            mensagem:
              type: string
    """
    with driver.session() as session:
        session.run("""
            MERGE (a:Aluno {email: $email_aluno})
            ON CREATE SET a.vezes_jogadas = 1, a.videos_vistos = 0
            ON MATCH SET a.vezes_jogadas = a.vezes_jogadas + 1
        """, email_aluno=email_aluno)

    return jsonify({"email_aluno": email_aluno, "mensagem": "Contador de vezes jogadas incrementado com sucesso!"})

# Rota para verificar o contador de vezes jogadas
@app.route('/verificar-contador-vezes-jogadas/<email_aluno>', methods=['GET'])
def verificar_contador_vezes_jogadas(email_aluno):
    """
    Verifica o contador de vezes jogadas do aluno
    ---
    parameters:
      - name: email_aluno
        in: path
        type: string
        required: true
        description: O email do aluno
    responses:
      200:
        description: Contador de vezes jogadas retornado com sucesso
        schema:
          type: object
          properties:
            email_aluno:
              type: string
            vezes_jogadas:
              type: integer
      404:
        description: Aluno não encontrado
    """
    with driver.session() as session:
        result = session.run("MATCH (a:Aluno {email: $email_aluno}) RETURN a.vezes_jogadas AS vezes_jogadas",
                             email_aluno=email_aluno)
        record = result.single()

    if record is None:
        return jsonify({"error": "Aluno não encontrado"}), 404

    return jsonify({"email_aluno": email_aluno, "vezes_jogadas": record["vezes_jogadas"]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
