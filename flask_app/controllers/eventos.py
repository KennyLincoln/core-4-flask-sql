from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.evento import Evento
from flask_app.models.usuario import Usuario

@app.route('/eventos')
def dashboard():
    if 'usuario_id' not in session:
        return redirect('/')

    usuario = Usuario.get_by_id({'id': session['usuario_id']})
    todos_eventos = Evento.get_todos_con_organizador()
    return render_template('eventos.html', usuario=usuario, eventos=todos_eventos)

@app.route('/nuevo')
def nuevo_evento():
    if 'usuario_id' not in session:
        return redirect('/')
    return render_template('crear_evento.html')

@app.route('/crear/evento', methods=['POST'])
def crear_evento():
    if 'usuario_id' not in session:
        return redirect('/')

    if not Evento.validar_evento(request.form):
        return redirect('/nuevo')

    datos = {
        "nombre_evento": request.form['nombre_evento'],
        "ubicacion": request.form['ubicacion'],
        "fecha": request.form['fecha'],
        "detalles": request.form['detalles'],
        "usuario_id": session['usuario_id']
    }
    Evento.guardar(datos)
    return redirect('/eventos')

@app.route('/ver/<int:id>')
def ver_evento(id):
    if 'usuario_id' not in session:
        return redirect('/')

    evento = Evento.get_by_id({'id': id})
    return render_template('ver_evento.html', evento=evento)

@app.route('/editar/<int:id>')
def editar_evento(id):
    if 'usuario_id' not in session:
        return redirect('/')

    evento = Evento.get_by_id({'id': id})
    if evento.usuario_id != session['usuario_id']:
        return redirect('/eventos')

    return render_template('editar_evento.html', evento=evento)

@app.route('/actualizar/evento/<int:id>', methods=['POST'])
def actualizar_evento(id):
    if 'usuario_id' not in session:
        return redirect('/')

    evento = Evento.get_by_id({'id': id})
    if evento.usuario_id != session['usuario_id']:
        return redirect('/eventos')

    if not Evento.validar_evento(request.form):
        return redirect(f'/editar/{id}')

    datos = {
        "id": id,
        "nombre_evento": request.form['nombre_evento'],
        "ubicacion": request.form['ubicacion'],
        "fecha": request.form['fecha'],
        "detalles": request.form['detalles']
    }
    Evento.actualizar(datos)
    return redirect('/eventos')

@app.route('/borrar/<int:id>')
def borrar_evento(id):
    if 'usuario_id' not in session:
        return redirect('/')

    evento = Evento.get_by_id({'id': id})
    if evento and evento.usuario_id == session['usuario_id']:
        Evento.borrar({'id': id})

    return redirect('/eventos')