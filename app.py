from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'titulo': "O senhor dos Aneis - A Sociedade do anel",
        'autor': "J.R.R Tolkien"
    },
     {
        'id':2,
        'titulo': "Harry Potter e a Pedra Filosofal",
        'autor': "J.K Howling"
    },
      {
        'id':3,
        'titulo': "James Clear",
        'autor': "Hábitos Atômicos"
    },
]

# Consultar (Todos)
@app.route("/livros",methods=['GET'])
def obter_livos():
    return jsonify(livros)

# Consultar (Por id)
@app.route("/livros/<int:id>",methods=['GET'])
def obter_livos_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar um livro (Por id)
@app.route("/livros/<int:id>",methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
@app.route("/livros",methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)

# Deletar
@app.route("/livros/<int:id>",methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            
    return jsonify(livros)       
        
app.run(port=5000,host='localhost',debug=True)