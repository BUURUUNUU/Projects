from flask import Flask, render_template


#comando iniciar server -> flask run --debug


#comando inicial: set FLASK_APP = app.py

#cria o aplicativo
app = Flask(__name__)

#cria a rota
#http://127.0.0.1:5000
#rodar o server: flask run
@app.route('/')
#cria função definida na rota
def principal():
    nome = "Fulano"
    idade = 25
    
    return render_template("index.html", nome = nome, idade=idade)

#nova rota
@app.route('/sobre')

def sobre():
        return render_template("sobre.html")