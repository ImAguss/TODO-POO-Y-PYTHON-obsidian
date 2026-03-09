from flask_sqlalchemy import SQLAlchemy
from datetime import date, time

db = SQLAlchemy()

class Trabajador(db.Model):
    __tablename__ = "trabajador"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(10), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    legajo = db.Column(db.String(20), unique=True, nullable=False)
    horas = db.Column(db.Integer, nullable=False)
    funcion = db.Column(db.String(2), nullable=False)
    
    registros_horarios = db.relationship('Registro', backref='trabajador', cascade="all, delete-orphan")

class Registro(db.Model):
    __tablename__ = "registrohorario"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    fecha = db.Column(db.Date, nullable=False)  # Usa Date si solo almacenas la fecha
    horaentrada = db.Column(db.Time, nullable=False)
    horasalida = db.Column(db.Time)
    dependencia = db.Column(db.String(4), nullable=False)
    idtrabajador = db.Column(db.Integer, db.ForeignKey('trabajador.id'), nullable=False)

