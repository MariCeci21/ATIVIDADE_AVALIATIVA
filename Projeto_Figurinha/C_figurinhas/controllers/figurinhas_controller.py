# Cenário: C - Figurinhas
# Aluno: Maria Cecília

from flask import Blueprint, render_template, request, redirect, url_for
from models.base import db
from models.colecionador import Colecionador
from models.figurinha import Figurinha
from models.oferta import OfertaTroca

figurinhas_blueprint = Blueprint('figurinhas', __name__, url_prefix='/figurinhas')

@figurinhas_blueprint.route('/')
def index():
    # Busca as ofertas ativas e renderiza o arquivo correto da imagem
    ofertas = OfertaTroca.query.filter_by(status="Ativa").all()
    return render_template('figurinhas/lista_ofertas.html', ofertas=ofertas)

@figurinhas_blueprint.route('/nova', methods=['GET', 'POST'])
def nova_oferta():
    if request.method == 'POST':
        colecionador_id = request.form.get('colecionador_id')
        tem_id = request.form.get('figurinha_tem_id')
        procura_id = request.form.get('figurinha_procura_id')

        nova = OfertaTroca(
            colecionador_id=colecionador_id,
            figurinha_tem_id=tem_id,
            figurinha_procura_id=procura_id
        )
        db.session.add(nova)
        db.session.commit()
        return redirect(url_for('figurinhas.index'))

    # Renderiza o formulário com o nome exato que está na sua pasta
    colecionadores = Colecionador.query.all()
    figurinhas = Figurinha.query.all()
    return render_template('figurinhas/formulario_oferta.html', colecionadores=colecionadores, figurinhas=figurinhas)