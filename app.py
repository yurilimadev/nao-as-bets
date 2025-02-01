from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from forms import FormCriarDepoimento, FormChurnDepoimento
from flask_wtf.csrf import CSRFProtect
from dotenv import dotenv_values
from models import db, Depoimento, ChurnDepoimento
from flask_migrate import Migrate

app = Flask(__name__)
config = dotenv_values(".env")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///depoimentos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config['TOKEN_SEGURANCA']


migrate = Migrate(app, db)

csrf = CSRFProtect(app)

db.init_app(app)

# Criação do banco e tabelas
with app.app_context():
    db.create_all()

# Rota para cadastro de depoimentos


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
                assunto=assunto,
                data_cadastro=db.func.now()
            )

            db.session.add(novo_depoimento)
            db.session.commit()

            flash("Depoimento enviado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Você preencheu corretamente o formulário? Tente novamente", "fail")
    return render_template('index.html', form_depoimento=form_depoimento)

# Rota para informações de como contribuir


@app.route('/contribua')
def contribua():
    return render_template('contribua.html')


@app.route('/motivacao')
def motivacao():
    return render_template('motivacao.html')

# Rotas para Mostrar depoimentos


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


@app.route('/get-form', methods=['GET', 'POST'])
def get_form():
    form_churn = FormChurnDepoimento()
    depoimento_id = request.form.get("depoimento_id", type=int)
    assunto = request.form.get("assunto", type=str)
    if request.method == 'POST':
        if form_churn.validate_on_submit():

            motivo = form_churn.motivo.data

            depoimento_para_excluir = Depoimento.query.filter_by(
                id=depoimento_id).first()

            if depoimento_para_excluir:
                churn = ChurnDepoimento(
                    assunto=assunto,
                    motivo=motivo,
                    depoimento_id=depoimento_para_excluir.id,
                    data_exclusao=db.func.now()
                )

                db.session.add(churn)
                db.session.commit()

                db.session.delete(depoimento_para_excluir)
                db.session.commit()

                flash("Depoimento excluido com sucesso!", "success")

            else:
                flash("Erro ao remover? Tente novamente", "fail")
            return redirect(url_for("index"))
        else:
            flash("Erro ao remover. Você preencheu corretamente o formulário?", "fail")
    form_churn_render = render_template(
        'form-churn.html', form_churn=form_churn)
    return jsonify({"html": form_churn_render})
