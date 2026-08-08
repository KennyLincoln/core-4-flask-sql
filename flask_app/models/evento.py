from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Evento:
    def __init__(self, data):
        self.id = data['id']
        self.nombre_evento = data['nombre_evento']
        self.ubicacion = data['ubicacion']
        self.fecha = data['fecha']
        self.detalles = data['detalles']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.organizador = data.get('organizador', '')

    @classmethod
    def guardar(cls, datos):
        query = """
            INSERT INTO eventos (nombre_evento, ubicacion, fecha, detalles, usuario_id, created_at, updated_at)
            VALUES (%(nombre_evento)s, %(ubicacion)s, %(fecha)s, %(detalles)s, %(usuario_id)s, NOW(), NOW());
        """
        return connectToMySQL('esquema_eventos').query_db(query, datos)

    @classmethod
    def get_todos_con_organizador(cls):
        query = """
            SELECT eventos.*, CONCAT(usuarios.nombre) AS organizador 
            FROM eventos 
            JOIN usuarios ON eventos.usuario_id = usuarios.id;
        """
        resultados = connectToMySQL('esquema_eventos').query_db(query)
        eventos = []
        if resultados:
            for fila in resultados:
                e = cls(fila)
                e.organizador = fila['organizador']
                eventos.append(e)
        return eventos

    @classmethod
    def get_by_id(cls, datos):
        query = """
            SELECT eventos.*, usuarios.nombre AS organizador 
            FROM eventos 
            JOIN usuarios ON eventos.usuario_id = usuarios.id 
            WHERE eventos.id = %(id)s;
        """
        resultados = connectToMySQL('esquema_eventos').query_db(query, datos)
        if resultados:
            e = cls(resultados[0])
            e.organizador = resultados[0]['organizador']
            return e
        return None

    @classmethod
    def actualizar(cls, datos):
        query = """
            UPDATE eventos 
            SET nombre_evento = %(nombre_evento)s, ubicacion = %(ubicacion)s, 
                fecha = %(fecha)s, detalles = %(detalles)s, updated_at = NOW()
            WHERE id = %(id)s;
        """
        return connectToMySQL('esquema_eventos').query_db(query, datos)

    @classmethod
    def borrar(cls, datos):
        query = "DELETE FROM eventos WHERE id = %(id)s;"
        return connectToMySQL('esquema_eventos').query_db(query, datos)

    @staticmethod
    def validar_evento(formulario):
        es_valido = True
        
        if not formulario.get('nombre_evento') or len(formulario['nombre_evento'].strip()) < 3:
            flash("Nombre del evento es obligatorio y debe tener al menos 3 caracteres", "evento")
            es_valido = False

        if not formulario.get('ubicacion') or len(formulario['ubicacion'].strip()) < 3:
            flash("Ubicación es obligatoria y debe tener al menos 3 caracteres", "evento")
            es_valido = False

        if not formulario.get('fecha'):
            flash("La fecha es obligatoria", "evento")
            es_valido = False

        if not formulario.get('detalles') or len(formulario['detalles'].strip()) < 3:
            flash("Detalles no puede estar vacío y debe tener al menos 3 caracteres", "evento")
            es_valido = False

        return es_valido