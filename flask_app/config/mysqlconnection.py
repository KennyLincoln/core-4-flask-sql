import os

import pymysql.cursors


class MySQLConnection:
    """Crea una conexión MySQL usando variables de entorno."""

    def __init__(self, db=None):
        database = db or os.getenv("MYSQL_DATABASE")
        if not database:
            raise ValueError("Define MYSQL_DATABASE antes de iniciar la aplicación.")

        self.connection = pymysql.connect(
            host=os.getenv("MYSQL_HOST", "127.0.0.1"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", ""),
            db=database,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True,
        )

    def query_db(self, query, data=None):
        try:
            with self.connection.cursor() as cursor:
                executable = cursor.execute(query, data)
                if query.lstrip().lower().startswith("insert"):
                    return cursor.lastrowid
                if query.lstrip().lower().startswith("select"):
                    return cursor.fetchall()
                return executable
        except Exception as exc:
            print("Error al ejecutar la consulta:", exc)
            return False
        finally:
            self.connection.close()


def connectToMySQL(db=None):
    return MySQLConnection(db)
