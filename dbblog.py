import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="dbblog",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )
    conn.set_client_encoding('UTF8')
    return conn

def creer_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Articles (
            id SERIAL PRIMARY KEY,
            titre VARCHAR(255) NOT NULL,
            contenu TEXT NOT NULL,
            date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cur.close()
    conn.close()

def ajouter_article(titre, contenu):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO Articles (titre, contenu)
        VALUES (%s, %s)
    """, (titre, contenu))

    conn.commit()
    cur.close()
    conn.close()

def lire_articles():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Articles ORDER BY date_creation DESC")
    articles = cur.fetchall()

    cur.close()
    conn.close()

    return articles

