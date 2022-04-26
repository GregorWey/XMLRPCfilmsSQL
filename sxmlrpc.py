import xmlrpc.server
import sys
import conex
#-----------------------------------------------------------------
cnx = conex.conexao()
cursor = cnx.cursor()

print("Servidor iniciado")
#-----------------------------------------------------------------
def op1():  
    query = ("SELECT DISTINCT nomeAtor from Films.Atores order by nomeAtor ASC")
    cursor.execute(query)
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------  
def op2():
    query = ("SELECT DISTINCT nomeAtor from Films.Atores order by nomeAtor DESC")
    cursor.execute(query)
    data = cursor.fetchall()
    return data
#----------------------------------------------------------------
def op3(dadosEntradaAtor):
    cursor.execute("SELECT nomeFilme, anoFilme from Films.Filmes as F inner join Films.Atores as A on F.id = A.idAtor where A.nomeAtor = '%s' order by F.anoFilme" % dadosEntradaAtor)
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------
def op4():
    query = ("SELECT DISTINCT nomeFilme,anoFilme from Films.Filmes order by nomeFilme ASC")
    cursor.execute(query)
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------
def op5():
    query = ("SELECT DISTINCT nomeFilme,anoFilme from Films.Filmes order by nomeFilme DESC")
    cursor.execute(query)
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------
def op6(nomeFilme,anoFilme,listaDiretor,listaAtor):
    query ="SELECT COUNT(id)+1 FROM Filmes"
    cursor.execute(query)
    quantId=cursor.fetchone()
    quantId=quantId[0]
    query = ("INSERT INTO Films.Filmes (id,nomeFilme,anoFilme) VALUES ('%s','%s','%s');" % (quantId, nomeFilme, anoFilme))
    cursor.execute(query)
    cnx.commit()
    for diretor in listaDiretor:
        query = ("INSERT INTO Films.Diretores (idDiretor,nomeDiretor) VALUES ('%s','%s');" % (quantId,diretor))
        cursor.execute(query)
        cnx.commit()
    for ator in listaAtor:
        query = ("INSERT INTO Films.Atores (idAtor,nomeAtor) VALUES ('%s','%s');" % (quantId,ator))
        cursor.execute(query)
        cnx.commit()

    return "Inserido"
#-----------------------------------------------------------------
def op7(stringID):
    intID=int(stringID)
    query = ("DELETE FROM Films.Filmes WHERE id='%s'" % intID)
    cursor.execute(query)
    cnx.commit()
    query = ("DELETE FROM Films.Atores WHERE idAtor='%s'" % intID)
    cursor.execute(query)
    cnx.commit()
    query = ("DELETE FROM Films.Diretores WHERE idDiretor='%s'" % intID)
    cursor.execute(query)
    cnx.commit()
    return "Excluido"
#-----------------------------------------------------------------
def op8(dadosDiretor):
    query=("SELECT nomeFilme,anoFilme from Films.Filmes as F inner join Films.Diretores as D on F.id = D.idDiretor where D.nomeDiretor = '%s' order by F.anoFilme" %dadosDiretor)
    cursor.execute(query)
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------
def op9(dadosEntradaAtor):
    print("Entrou")
    query=("DROP VIEW IF EXISTS Films.Temp")
    cursor.execute(query)
    cnx.commit()
    print("1")
    query=("CREATE VIEW Films.Temp AS SELECT idAtor FROM Films.Atores WHERE nomeAtor ='%s'" % dadosEntradaAtor)
    cursor.execute(query)
    cnx.commit()
    print("2")
    query=("SELECT nomeAtor,nomeFilme FROM Films.Atores as A INNER JOIN Films.Filmes as F on A.idAtor=F.id INNER JOIN Films.Temp as T on F.id =T.idAtor AND A.nomeAtor NOT LIKE '%s'" % dadosEntradaAtor)
    cursor.execute(query)
    print("3")
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------
def op10(stringDiretor):
    query =("SELECT nomeFilme,anoFilme,nomeAtor FROM Films.Diretores as D inner join Films.Filmes as F on D.idDiretor=F.id inner join Films.Atores as A on F.id=A.idAtor where nomeDiretor = '%s'" %stringDiretor)
    cursor.execute(query)	
    data = cursor.fetchall()
    return data
#-----------------------------------------------------------------
def op11():
    query = ("SELECT nomeFilme as Filme,anoFilme as Ano,COUNT(*) as Quantidade FROM Films.Filmes GROUP BY nomeFilme,anoFilme HAVING COUNT(*)>1 ORDER BY anoFilme ASC")
    cursor.execute(query)
    data = cursor.fetchall()
    return data

#-----------------------------------------------------------------
if len(sys.argv) !=2:
    print ('%s <porta>' % sys.argv[0])
    sys.exit(0)


porta = int(sys.argv[1])

servidor = xmlrpc.server.SimpleXMLRPCServer(("localhost",porta))
servidor.register_function(op1,"op1")
servidor.register_function(op2,"op2")
servidor.register_function(op3,"op3")
servidor.register_function(op4,"op4")
servidor.register_function(op5,"op5")
servidor.register_function(op6,"op6")
servidor.register_function(op7,"op7")
servidor.register_function(op8,"op8")
servidor.register_function(op9,"op9")
servidor.register_function(op10,"op10")
servidor.register_function(op11,"op11")
servidor.serve_forever()
