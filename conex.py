import mysql.connector

def conexao():
    cnx = mysql.connector.connect(user='root', 
                              password='password',
                              host='localhost',
                              database='Films')
    return cnx

