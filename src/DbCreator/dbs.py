import sqlite3
conn = sqlite3.connect('../db.db')
conn.text_factory = str
cur = conn.cursor()
cur.execute("CREATE TABLE therdb(compound,data)")
conn.commit()
conn.close()