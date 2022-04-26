import xmlrpc.client
import sys
#-----------------------------------------------------------------
def exibeMenu():
    print('''
            MENU:

            [1] - Atores em ordem alfabetica ASC
            [2] - Atores em ordem alfabetica DSC
            [3] - Filmes de um ator em ordem cronologica
            [4] - Filmes em ordem alfabetica ASC
            [5] - Filmes em ordem alfabetica DSC
            [6] - Inserir filme
            [7] - Remover filme
            [8] - Listar filmes de um diretor em ordem cronologica
            [9] - Listar atores relacionados
            [10] - Atores e diretores relacionados
            [11] - Listar filmes duplicados
            [12] - Sair
        ''')
#-----------------------------------------------------------------
if len(sys.argv) !=3:
    print ('%s <ip> <porta>' % sys.argv[0])
    sys.exit(0)

ip = sys.argv[1]
porta = sys.argv[2]

servidor = xmlrpc.client.ServerProxy('http://'+ip+':'+porta)

while(True):
    exibeMenu()
    tempString=input("Digite a opcao:")
    if(tempString=='1'):
        dados = servidor.op1()
        for (record) in dados:
            print(record[0])
    elif(tempString=='2'):
        dados = servidor.op2()
        for (record) in dados:
            print(record[0])
    elif(tempString=='3'):
        tempAtor=input("Digite o Ator:")
        dados = servidor.op3(tempAtor)
        for (record) in dados:
            print(record[0] + " ANO:"+record[1])
    elif(tempString=='4'):
        dados = servidor.op4()
        for (record) in dados:
            print(record[0] + " ANO:"+record[1])
    elif(tempString=='5'):
        dados = servidor.op5()
        for (record) in dados:
            print(record[0] + " ANO:"+record[1])
    elif(tempString=='6'):
        tempFilme=input("Digite o filme que deseja adicionar:")
        tempAno=input("Digite o ano do filme que deseja adicionar:")
        lstDir=[]
        lstAtr=[]
        nmrDire=int(input("Quantos diretores tem?"))
        if (nmrDire==0):
            print("Deve ter no mínimo um diretor")
        else:
            for i in range(0, nmrDire):
                tempDiretor = input()
                lstDir.append(tempDiretor)
            nmrAtr=int(input("Quantos atores tem?"))
            if (nmrAtr==0):
                print("Deve ter no mínimo um ator")
            else:
                for i in range(0, nmrAtr):
                    tempAtor = input()
                    lstAtr.append(tempAtor)
                dados = servidor.op6(tempFilme,tempAno,lstDir,lstAtr)
                print(dados)
    elif(tempString=='7'):
        tempID=input("Digite o id:")
        dados = servidor.op7(tempID)
        print(dados)
    elif(tempString=='8'):
        tempDiretor=input("Digite o Diretor:")
        dados = servidor.op8(tempDiretor)
        for (record) in dados:
            print(record[0] + "  ANO:"+record[1])
    elif(tempString=='9'):
        tempAtor=input("Digite o ator:")
        dados = servidor.op9(tempAtor)
        for (record) in dados:
            print(record[0] + "  FILME:"+ record[1])
    elif(tempString=='10'):
        tempDiretor=input("Digite o Diretor:")
        dados = servidor.op10(tempDiretor)
        for (record) in dados:
            print(record[0] + " ANO:"+record[1] + " ATOR:"+record[2])
    elif(tempString=='11'):
        dados = servidor.op11()
        for (record) in dados:
            print(record[0])
    else:
        break
        
