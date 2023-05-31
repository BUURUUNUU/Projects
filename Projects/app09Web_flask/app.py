from flask import Flask, render_template


#comando inicial: set FLASK_APP = app.py

#cria o aplicativo
app = Flask(__name__)

#cria a rota
#http://127.0.0.1:5000
#rodar o server: flask run
@app.route('/')
#cria função definida na rota
def principal():
    return render_template("index.html")