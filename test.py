import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

#cur.execute("CREATE TABLE coco_base_181184(id, nom, email)")

#res = cur.execute("SELECT name FROM sqlite_master")
#print(res.fetchone())

cur.execute("""
    INSERT INTO ma_base VALUES
        (1, 'fab', 'fab@joj.fr'),
        (2, 'Jiji', 'jij@joj.fr')
""")

con.commit()

res = cur.execute("SELECT * FROM ma_base")
print(res.fetchall())