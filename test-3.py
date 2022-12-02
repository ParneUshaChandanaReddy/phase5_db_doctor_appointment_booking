
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_10")

connection = cx_Oracle.connect(user="vxd9845",password="Ashoksai1997",dsn="acaddbprod.uta.edu:1523/pcse1p.data.uta.edu")

cursor = connection.cursor()

