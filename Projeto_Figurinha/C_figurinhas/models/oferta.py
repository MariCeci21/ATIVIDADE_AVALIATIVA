from models.base import db
from datetime import datetime

class OfertaTroca(db.Model):
    __tablename__ = 'ofertas_troca'

    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="Ativa") # Ativa, Finalizada

    # FK para o Colecionador que criou a oferta
    colecionador_id = db.Column(db.Integer, db.ForeignKey('colecionadores.id'), nullable=False)
    
    # FK para a Figurinha que ele está OFERECENDO
    figurinha_tem_id = db.Column(db.Integer, db.ForeignKey('figurinhas.id'), nullable=False)
    
    # FK para a Figurinha que ele PROCURA
    figurinha_procura_id = db.Column(db.Integer, db.ForeignKey('figurinhas.id'), nullable=False)

    # Relacionamentos
    colecionador = db.relationship('Colecionador', back_populates='ofertas')
    
    # foreign_keys é necessário aqui porque temos duas FKs apontando para a mesma tabela (Figurinha)
    figurinha_tem = db.relationship('Figurinha', foreign_keys=[figurinha_tem_id])
    figurinha_procura = db.relationship('Figurinha', foreign_keys=[figurinha_procura_id])