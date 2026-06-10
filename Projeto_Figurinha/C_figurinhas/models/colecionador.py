from models.base import db

class Colecionador(db.Model):
    __tablename__ = 'colecionadores'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    whatsapp = db.Column(db.String(20), nullable=False)

    # Relacionamento para acessar as ofertas criadas por este colecionador
    ofertas = db.relationship('OfertaTroca', back_populates='colecionador')