import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());
        """
        return connectToMySQL('esquema_eventos').query_db(query, datos)

    @classmethod
    def buscar_por_email(cls, datos):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        resultados = connectToMySQL('esquema_eventos').query_db(query, datos)
        if len(resultados) == 1:
            return cls(resultados[0])
        return False

    @classmethod
    def get_by_id(cls, datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultado = connectToMySQL('esquema_eventos').query_db(query, datos)
        if resultado:
            return cls(resultado[0])
        return None

    @staticmethod
    def validar_registro(usuario):
        es_valido = True

        if len(usuario['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        if len(usuario['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "registro")
            es_valido = False

        if not EMAIL_REGEX.match(usuario['email']):
            flash("El email debe tener un formato válido.", "registro")
            es_valido = False
        elif Usuario.buscar_por_email({'email': usuario['email']}):
            flash("El email ya está registrado en la base de datos.", "registro")
            es_valido = False

        if usuario['password'] != usuario['confirm_password']:
            flash("La contraseña y la confirmación deben ser iguales.", "registro")
            es_valido = False

        return es_valido