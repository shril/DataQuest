import psycopg2
conn = psycopg2.connect(dbname="dq", user="postgres")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE income OWNER postgres;")
conn.close()