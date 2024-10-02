# EducaEco API - Neo4j

EducaEco é uma API desenvolvida em Python com Flask e utilizando o Neo4j como banco de dados para gerenciar informações relacionadas a alunos e contadores de atividades (como vídeos vistos e jogos jogados). A API oferece endpoints para incrementar e consultar esses contadores.

## Índice

- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Endpoints](#endpoints)
  - [Incrementar contador de vídeos vistos](#incrementar-contador-de-vídeos-vistos)
  - [Verificar contador de vídeos vistos](#verificar-contador-de-vídeos-vistos)
  - [Incrementar contador de vezes jogadas](#incrementar-contador-de-vezes-jogadas)
  - [Verificar contador de vezes jogadas](#verificar-contador-de-vezes-jogadas)
- [Licença](#licença)

## Tecnologias

- Python 3.x
- Flask
- Neo4j
- Neo4j Python Driver
- Flask CORS

## Pré-requisitos

- Python 3.x instalado
- Neo4j rodando em uma instância na nuvem (como Neo4j AuraDB)
- Git instalado

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/SamuelXavierGTech/EducaEco-API-Neo4j.git
    ```

2. Entre no diretório do projeto:

    ```bash
    cd EducaEco-API-Neo4j
    ```

3. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/MacOS
    venv\Scripts\activate  # Para Windows
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Configure o arquivo `.env`:

    Crie um arquivo `.env` na raiz do projeto e adicione suas variáveis de ambiente. Exemplo:

    ```bash
    NEO4J_URI=bolt://<sua-instancia>.databases.neo4j.io:7687
    NEO4J_USER=neo4j
    NEO4J_PASSWORD=<sua-senha>
    FLASK_ENV=development
    ```

6. Inicie o servidor Flask:

    ```bash
    python app.py
    ```

    A API estará rodando em `http://127.0.0.1:5000`.

## Variáveis de Ambiente

O projeto utiliza um arquivo `.env` para armazenar credenciais sensíveis e informações de configuração. Certifique-se de não subir este arquivo para o repositório. Aqui estão as variáveis de ambiente que precisam ser configuradas:

- `NEO4J_URI`: URI da instância do Neo4j
- `NEO4J_USER`: Usuário do banco de dados Neo4j
- `NEO4J_PASSWORD`: Senha do banco de dados Neo4j
- `FLASK_ENV`: Define o ambiente de execução do Flask (`development` ou `production`)

## Endpoints

### Incrementar contador de vídeos vistos

- **Rota:** `/incrementar-contador-videos-vistos`
- **Método:** `POST`
- **Descrição:** Incrementa o contador de vídeos vistos para o aluno.
- **Body (JSON):**
    ```json
    {
      "email_aluno": "email@example.com"
    }
    ```
- **Resposta:**
    ```json
    {
      "email_aluno": "email@example.com",
      "mensagem": "Contador incrementado com sucesso!"
    }
    ```

### Verificar contador de vídeos vistos

- **Rota:** `/verificar-contador-videos-vistos/<email_aluno>`
- **Método:** `GET`
- **Descrição:** Retorna o número de vídeos vistos pelo aluno.
- **Parâmetros de URL:** `email_aluno`: E-mail do aluno a ser consultado.
- **Resposta:**
    ```json
    {
      "email_aluno": "email@example.com",
      "videos_vistos": 5
    }
    ```

### Incrementar contador de vezes jogadas

- **Rota:** `/incrementar-contador-vezes-jogadas`
- **Método:** `POST`
- **Descrição:** Incrementa o contador de vezes jogadas para o aluno.
- **Body (JSON):**
    ```json
    {
      "email_aluno": "email@example.com"
    }
    ```
- **Resposta:**
    ```json
    {
      "email_aluno": "email@example.com",
      "mensagem": "Contador incrementado com sucesso!"
    }
    ```

### Verificar contador de vezes jogadas

- **Rota:** `/verificar-contador-vezes-jogadas/<email_aluno>`
- **Método:** `GET`
- **Descrição:** Retorna o número de vezes jogadas pelo aluno.
- **Parâmetros de URL:** `email_aluno`: E-mail do aluno a ser consultado.
-
