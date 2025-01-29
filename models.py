from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Depoimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    depoimento = db.Column(db.Text, nullable=False)
    assunto = db.Column(db.String(50), nullable=False)
    data_cadastro = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f'<Depoimento {self.titulo}>'


class ChurnDepoimento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motivo = db.Column(db.String(10), nullable=False)
    assunto = db.Column(db.String(10), nullable=False)
    depoimento_id = db.Column(db.Integer, db.ForeignKey('depoimento.id'))
    data_exclusao = db.Column(db.DateTime(
        timezone=True), server_default=db.func.now())

    depoimento = db.relationship('Depoimento', backref='churns')

    def __repr__(self):
        return f'<Depoimento {self.depoimento_id}>'
