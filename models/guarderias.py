from db import db

class Guarderias(db.Model):
    __tablename__ = 'guarderias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(255))  # Agregado: Columna para la dirección
    telefono = db.Column(db.String(20))    # Agregado: Columna para el teléfono
    perros = db.relationship('Perros', backref='guarderias', lazy=True)
    cuidadores = db.relationship('Cuidadores', backref='guarderias', lazy=True)

    def __repr__(self):
        return f'<Guarderias {self.nombre}>'

    @property
    def get_nombre(self):
        return self.nombre

    @property
    def get_direccion(self):  # Getter para la dirección
        return self.direccion

    @property
    def get_telefono(self):   # Getter para el teléfono
        return self.telefono