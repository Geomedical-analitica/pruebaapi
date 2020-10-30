#db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('root')
db_password = os.environ.get('prueba')
db_name = os.environ.get('prueba')
db_connection_name = os.environ.get('prueba-api-294023:us-central1:prueba-api')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_padres():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM padre;')
        padre = cursor.fetchall()
        if result > 0:
            got_padre = jsonify(padre)
        else:
            got_song = 'No hay registro en la DB'
    conn.close()
    return got_padre

def add_padre(padre):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO padre (ID_Padre, Primer_NombreP, Primer_ApellidoP) VALUES(%s, %s, %s)', (padre["ID_Padre"], padre["Primer_NombreP"], padre["Primer_ApellidoP"]))
    conn.commit()
    conn.close()
