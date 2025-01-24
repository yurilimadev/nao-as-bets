from flask import Flask, render_template, url_for, flash, redirect, request
from forms import FormCriarDepoimento
from flask_wtf.csrf import CSRFProtect
from dotenv import dotenv_values

app = Flask(__name__)
app.secret_key = "a684e8fb6b2fefa24d3e9119978309f1"
config = dotenv_values(".env")


app.config['SECRET_KEY'] = config['TOKEN_SEGURANCA']

csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form_depoimento = FormCriarDepoimento()
    if form_depoimento.validate_on_submit():
        assunto = form_depoimento.assunto.data
        titulo = form_depoimento.titulo.data
        idade = form_depoimento.idade.data
        sexo = form_depoimento.sexo.data
        estado = form_depoimento.estado.data
        depoimento = form_depoimento.depoimento.data

        # Exemplo: salvar em um banco de dados ou exibir os dados
        print(f"Título: {titulo}, Idade: {idade}, Sexo: {
            sexo}, Estado: {estado}, Depoimento: {depoimento}")
        flash("Depoimento enviado com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template('index.html', form_depoimento=form_depoimento)


@app.route('/motivacao')
def motivacao():
    return render_template('motivacao.html')
