from models.base import db

class Figurinha(db.Model):
    __tablename__ = 'figurinhas'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), nullable=False, unique=True) # Ex: BRA-01
    nome_jogador = db.Column(db.String(100), nullable=False)
    selecao = db.Column(db.String(50), nullable=False)