from flask import Flask, render_template, url_for, flash, redirect, request
from forms import FormCriarDepoimento
from flask_wtf.csrf import CSRFProtect
from dotenv import dotenv_values
from models import db, Depoimento

app = Flask(__name__)
config = dotenv_values(".env")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///depoimentos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config['TOKEN_SEGURANCA']

csrf = CSRFProtect(app)

db.init_app(app)

# Criação do banco e tabelas
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    form_depoimento = FormCriarDepoimento()
    if request.method == 'POST':
        if form_depoimento.validate_on_submit():
            assunto = form_depoimento.assunto.data
            titulo = form_depoimento.titulo.data
            idade = form_depoimento.idade.data
            sexo = form_depoimento.sexo.data
            estado = form_depoimento.estado.data
            depoimento = form_depoimento.depoimento.data

            novo_depoimento = Depoimento(
                titulo=titulo,
                idade=idade,
                sexo=sexo,
                estado=estado,
                depoimento=depoimento,
                assunto=assunto
            )

            db.session.add(novo_depoimento)
            db.session.commit()

            flash("Depoimento enviado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Você preencheu corretamente o formulário? Tente novamente", "fail")
    return render_template('index.html', form_depoimento=form_depoimento)


@app.route('/motivacao')
def motivacao():
    return render_template('motivacao.html')


@app.route('/depoimento/seis-por-um')
def depoimento_seis_por_um():
    # Busca os depoimentos relacionados ao "seis por um"
    depoimentos = Depoimento.query.filter_by(assunto="S").all()
    return render_template('depoimento-seis-por-um.html', depoimentos=depoimentos)


@app.route('/depoimento/bets')
def depoimento_bets():
    # Busca os depoimentos relacionados ao "bets"
    depoimentos = Depoimento.query.filter_by(assunto="B").all()
    return render_template('depoimento-bets.html', depoimentos=depoimentos)
