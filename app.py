from flask import Flask, render_template
import json
from utils import db
import os
from flask_migrate import Migrate
from models import Usuario, Pizza

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_usuario = os.getenv('DB_USERNAME')
db_senha = os.getenv('DB_PASSWORD')
db_mydb = os.getenv('DB_DATABASE')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

conexao = f"mysql+pymysql://{db_usuario}:{db_senha}@{db_host}:{db_port}/{db_mydb}"
print(conexao)
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/teste_insert') 
def teste_insert():
    user = Usuario("Jungwon", "jungwon@ifrn.edu.br", "54321")
    db.session.add(user) # Insert into Usuario(nome, email, senha) values ('Dafne Lima', 'dafne.c@escolar.ifrn.edu.br', '12345')
    db.session.commit()
    return 'Dados inseridos com sucesso!'

@app.route('/teste_select')
def teste_select():
    users = Usuario.query.all()
    #print(users)
    for u in users:
        print (u.nome)

    user = Usuario.query.get(2)
    print (f"O email do usuário de id 2 é {user.email}")

    return 'dados recuperados'

@app.route('/teste_update')
def teste_update():
    user = Usuario.query.get(1)
    user.nome = "Dafne L."
    user.senha = "123456"
    db.session.add(user)
    db.session.commit()
    return 'dados alterados com sucesso!'
