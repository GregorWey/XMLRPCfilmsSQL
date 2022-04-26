import pandas as pd
import conex

arquivo = open('resumo.txt','r')
Linhas = arquivo.readlines()

conectar=conex.conexao()
cursor = conectar.cursor()

contador=1
for line in Linhas:
    filme,ano,diretor,*resto=line.split(',')
    query="""INSERT INTO Filmes (id,nomeFilme,anoFilme) VALUES (%s,%s,%s)"""
    var=(contador,filme,ano)
    cursor.execute(query, var)
    conectar.commit()
    query="""INSERT INTO Diretores (idDiretor,nomeDiretor) VALUES (%s,%s)"""
    var=(contador,diretor)
    cursor.execute(query, var)
    conectar.commit()
    for i in resto:
        if i.startswith('dir:'):
            query="""INSERT INTO Diretores (idDiretor,nomeDiretor) VALUES (%s,%s)"""
            var=(contador,i)
            cursor.execute(query, var)
            conectar.commit()
        else:
            query="""INSERT INTO Atores (idAtor,nomeAtor) VALUES (%s,%s)"""
            var=(contador,i)
            cursor.execute(query, var)
            conectar.commit()
    contador +=1

cursor.close()
conectar.close()
