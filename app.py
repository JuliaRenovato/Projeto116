# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/index")
def home():

    nome = "Júlia"
    idade = "15"

    return render_template('index.html' , nome = nome , idade = idade)

@app.route("/pai")
def Father():
    nome = "Alessandro"
    idade = "51"
    return render_template('pai.html', nome = nome, idade = idade)

@app.route("/mãe")
def Mother():
    nome = "Goretti"
    idade = "50"
    return render_template('mae.html', nome = nome, idade = idade)

@app.route("/amigo")
def Friend():
    nome = "Arthur"
    idade = "15"
    return render_template('amigo.html', nome = nome, idade = idade)

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
