from db import db
class Cuidadores(db.Model):
    __tablename__ = 'cuidadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    guarderia_id = db.Column(db.Integer, db.ForeignKey('guarderia.id'))
    perros = db.relationship('Perros', backref="cuidadores", lazy=True)
    def __repr__(self):
        return f'<Cuidadores {self.nombre}>'
    @property
    def get_nombre(self):
        return self.nombre

    @property
    def get_telefono(self):
        return self.telefono
    @property
    def get_id_guarderia(self):
        return self.guarderia_id