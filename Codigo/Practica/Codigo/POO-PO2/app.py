from datetime import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
from models import db
from models import Trabajador, Registro

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/entrada', methods=['GET', 'POST'])
def entrada():
    resultado = render_template('aviso.html', mensaje='No se pudo ejecutar la operación')
    if request.method == 'POST':
        legajo = request.form['legajo'].strip()
        dni_ultimos4 = request.form['dni_ultimos4'].strip()

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()

        if not trabajador or str(trabajador.dni).strip()[-4:] != dni_ultimos4:
            resultado = render_template('error.html', error='Credenciales incorrectas')
        else:
            ingreso = Registro.query.filter_by(idtrabajador=trabajador.id, fecha=datetime.now().date(), horasalida=None).first()
            if ingreso is not None:
                resultado = render_template('error.html', error='Este trabajador ya tiene un ingreso sin registrar salida en la dependencia {}.'.format(ingreso.dependencia))
            else:
                nuevo_registro = Registro()
                nuevo_registro.fecha = datetime.now().date()
                nuevo_registro.horaentrada = datetime.now().time()
                nuevo_registro.dependencia = request.form['dependencia']
                nuevo_registro.idtrabajador = trabajador.id
                db.session.add(nuevo_registro)
                db.session.commit()
                resultado = render_template('aviso.html', mensaje='Registro de entrada guardado exitosamente en la dependencia {}.'.format(request.form['dependencia']))
    else:
        resultado = render_template('entrada.html')  

    return resultado


@app.route('/salida', methods=['GET', 'POST'])
def salida():
    resultado = render_template('aviso.html', mensaje='No se pudo ejecutar la operación')
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_ultimos4 = request.form['dni_ultimos4']

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        
        if not trabajador or str(trabajador.dni)[-4:] != dni_ultimos4:
            resultado = render_template('error.html', error='Credenciales incorrectas')
        else:
            ingreso = Registro.query.filter_by(idtrabajador=trabajador.id, fecha=datetime.now().date(), horasalida=None).first()
            if ingreso is None:
                resultado = render_template('error.html', error='Este trabajador no registra su salida.')
            else:
                ingreso.horasalida = datetime.now().time()
                db.session.commit()
                resultado = render_template('aviso.html', mensaje='Registro de salida guardado exitosamente en la dependencia {}.'.format(ingreso.dependencia))
    else:
        resultado = render_template('salida.html')

    return resultado

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    resultado = render_template('aviso.html', mensaje='No se pudo ejecutar la operación')
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_ultimos4 = request.form['dni_ultimos4']
        fecha_desde = datetime.strptime(request.form['fecha_desde'], '%Y-%m-%d').date()
        fecha_hasta = datetime.strptime(request.form['fecha_hasta'], '%Y-%m-%d').date()

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        
        if not trabajador or str(trabajador.dni)[-4:] != dni_ultimos4:
            resultado = render_template('error.html', error='Credenciales incorrectas')
        else:
            registros = Registro.query.filter(Registro.idtrabajador == trabajador.id,Registro.fecha >= fecha_desde,Registro.fecha <= fecha_hasta).all()
            resultado = render_template('consulta.html', registros=registros, trabajador=trabajador)

    else:
        resultado = render_template('consulta.html')

    return resultado

@app.route('/informe', methods=['GET', 'POST'])
def informe():
    resultado = render_template('aviso.html', mensaje='No se pudo ejecutar la operación')
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_ultimos4 = request.form['dni_ultimos4']

        administrador = Trabajador.query.filter_by(legajo=legajo).first()
        
        if not administrador or str(administrador.dni)[-4:] != dni_ultimos4 or administrador.funcion != "AD":
            resultado = render_template('error.html', error='Acceso denegado')
        else:
            fecha_desde = datetime.strptime(request.form['fecha_desde'], '%Y-%m-%d').date()
            fecha_hasta = datetime.strptime(request.form['fecha_hasta'], '%Y-%m-%d').date()
            rol = request.form['funcion']
            dependencia = request.form['dependencia']

            query = db.session.query(Registro, Trabajador).join(Trabajador)

            if rol != "Todos":
                query = query.filter(Trabajador.funcion == rol)

            if dependencia != "Todos":
                query = query.filter(Registro.dependencia == dependencia)

            query = query.filter(Registro.fecha >= fecha_desde, Registro.fecha <= fecha_hasta)

            resultados = query.all()
            resultado = render_template('informe.html', resultados=resultados)  

    else:
        resultado = render_template('informe.html')

    return resultado

@app.route('/ver_todo')
def ver_todo():
    trabajadores = Trabajador.query.all()
    return render_template('ver_todo.html', trabajadores=trabajadores)

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug = True)
