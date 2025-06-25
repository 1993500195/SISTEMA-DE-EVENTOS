from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    data = db.Column(db.String(20))
    local = db.Column(db.String(150))
    descricao = db.Column(db.Text)
    imagem = db.Column(db.String(500))  # URL ou caminho da imagem
