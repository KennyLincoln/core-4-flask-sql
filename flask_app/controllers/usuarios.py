from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def inicio():
    if 'usuario_id' in session:
        return redirect('/eventos')
    return render_template('inicio.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    pass_hasheado = bcrypt.generate_password_hash(request.form['password'])

    formulario = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": pass_hasheado
    }

    usuario_id = Usuario.guardar(formulario)
    session['usuario_id'] = usuario_id
    return redirect('/eventos')

@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.buscar_por_email({'email': request.form['email']})
    if not usuario:
        flash("El email debe estar registrado en la BD.", "login")
        return redirect('/')

    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("La contraseña no corresponde a la registrada.", "login")
        return redirect('/')

    session['usuario_id'] = usuario.id
    return redirect('/eventos')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')