from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class FormCriarDepoimento(FlaskForm):
    assunto = RadioField("Assunto", choices=[
        ("B", "Bets"), ("S", "Seis Por Um")], validators=[DataRequired()])
    titulo = StringField("Título", validators=[
                         DataRequired(), Length(min=2, max=100)])
    idade = IntegerField("Idade", validators=[
                         DataRequired(), NumberRange(min=1, max=120)])
    sexo = RadioField("Sexo", choices=[
                      ("M", "Masculino"), ("F", "Feminino")], validators=[DataRequired()])
    estado = SelectField(
        "Estado",
        choices=[
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AP", "Amapá"),
            ("AM", "Amazonas"),
            ("BA", "Bahia"),
            # ... outros estados
        ],
        validators=[DataRequired()],
    )
    depoimento = TextAreaField("Depoimento", validators=[
                               DataRequired(), Length(min=10)])
    submit = SubmitField("Enviar")
