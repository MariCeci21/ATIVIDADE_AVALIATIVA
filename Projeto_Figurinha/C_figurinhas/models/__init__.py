from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from models.base import db
from models.colecionador import Colecionador
from models.figurinha import Figurinha
from models.oferta import OfertaTroca

__all__ = ["db", "ModeloBase", "Colecionador", "Figurinha", "OfertaTroca", "ItemOferta"]
