import psycopg2
import psycopg2.extras
from flask import Flask, g
from urllib.parse import quote_plus


app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma_chave_secreta'

DB_USER = 'postgres'
DB_PASSWORD = 'wcc@2023'
DB_HOST = 'localhost'
DB_NAME = 'briefing3_clinica_veterinaria_3a'
DB_PORT = '5433'

ENCODED_DB_PASSWORD = quote_plus(DB_PASSWORD)

app.config['DATABASE_URL'] = f"postgresql://{DB_USER}:{ENCODED_DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    db.commit()
    last_id = None
    if cur.description:
        # Se a query retornou uma linha (ex: INSERT ... RETURNING id_produto)
        row = cur.fetchone()
        if row:
            # retorne o primeiro campo como valor escalar
            last_id = row[0]
        else:
            last_id = None
    else:
        last_id = None
    cur.close()
    return last_id

