import mysql.connector
import pandas as pd

##info de connection MySQL
server = 'Localhost'
port = '3306'
user = 'root'
password = 'BabouDiDou+182406'
database = 'exo_sql'



db = mysql.connector.connect(
    host = server,
    port = port,
    user = user,
    password = password)

print(db)

fam_D = pd.read_csv("famille_dim.csv")
con_D = pd.read_csv("condition_dim.csv")
fact = pd.read_csv("format_prod.csv")


#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

#requéte SQL
sql = "INSERT INTO famille (famille_id, famille) VALUES (%s, %s)"

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")
res = mycursor.fetchall()
for x in res :
    print(x)

