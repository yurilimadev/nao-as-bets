from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField, SelectField, TextAreaField, HiddenField
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
            ("CE", "Ceará"),
            ("DF", "Distrito Federal"),
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MT", "Mato Grosso"),
            ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PR", "Paraná"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RS", "Rio Grande do Sul"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("SC", "Santa Catarina"),
            ("SP", "São Paulo"),
            ("SE", "Sergipe"),
            ("TO", "Tocantins"),
        ],
        validators=[DataRequired()],
    )
    depoimento = TextAreaField("Depoimento", validators=[
                               DataRequired(), Length(min=10)])
    submit = SubmitField("Enviar")


class FormChurnDepoimento(FlaskForm):

    assunto = RadioField("Assunto", choices=[
        ("B", "Bets"), ("S", "Seis Por Um")], validators=[DataRequired()])
    motivo = SelectField(
        "Motivo",
        choices=[
            ("ameaca", "Ameaça"),
            ("medo", "Medo"),
            ("vergonha", "Vergonha"),
            ("arrependimento", "Arrependimento"),
            ("erro", "Erro no depoimento"),
            ("desconforto", "Desconforto"),
            ("mudanca_de_opiniao", "Mudança de opinião"),
            ("privacidade", "Preocupação com a privacidade"),
            ("pressao_social", "Pressão social"),
            ("irrelevancia", "Considerou irrelevante"),
            ("outro", "Outro"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Remover")
