
from db import db
class Perros(db.Model):
    __tablename__ = 'perros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Float)
    guarderia_id = db.Column(db.Integer, db.ForeignKey('guarderias.id'))
    cuidador_id = db.Column(db.Integer, db.ForeignKey('cuidadores.id'))
    def __repr__(self):
        return f'<Perros {self.nombre}>'

    @property
    def get_nombre(self):
        return self.nombre

    @property
    def get_raza(self):
        return self.raza

    @property
    def get_edad(self):
        return self.edad

    @property
    def get_peso(self):
        return self.peso

    @property
    def get_id_guarderia(self):
        return self.guarderia_id

    @property
    def get_id_cuidador(self):
        return self.cuidador_id 