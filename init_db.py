# -*- coding: utf-8 -*-
"""
    Este archivo configura las bases de datos por primera vez.
    Crea el archivo 'usuarios.db', la tabla 'users' y configura sqlalchemy.

    Si algo de lo mencionado arriba no existe, se deberá ejecutar este archivo.

    Para ello, el entorno virtual debe estar activado y las dependencias instaladas,
    luego se debe usar el siguiente comando:

        python init_db.py
"""

from main import app, db

db.create_all(app=app)
