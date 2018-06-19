#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from CRUD import dao
import MySQLdb as sql
import base64

def GetImg(img):
    with open(img, "rb") as f:
        ret = base64.b64encode(f.read())
        return ret

def clear():
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            print("Não foi possível limpar a tela.")

def ShowAtb(dataObj, tableName, id):
    data = dataObj.GetAllTab( tableName, id)
    columns = dataObj.GetColumns( tableName)

    print("\nNome do atributo -- Valor")
    print("-------------------------")
    for i in range(len(data[0])):
        print(str(columns[i][0]) + " -- " + str(data[0][i]))

def ShowColumns(dataObj, tableName):
    columns = dataObj.GetColumns( tableName)
    print("Atributos de " +  tableName + ":")
    for column in columns:
        print(column[0])

def ShowIds(dataObj, tableName):
    ids = dataObj.GetIds( tableName)

    print("id -- Nome")
    print("-----------")
    for item in ids:
        print(str(item[0]) + " -- " + item[1])

def CheckIds( tableName, oid):
    ids = dataObj.GetIds( tableName)    

    exist = False
    for item in ids:
        if(oid == str(item[0])):
            exist = True
    return exist

def CheckColumn(dataObj, tableName, name):
    columns = dataObj.GetColumns( tableName)
    
    exist = False
    for column in columns:
        if(column[0] == name):
            exist = True
    return exist

def UserDelete(dataObj):
    try:
        print("UserDelete")
        tables = dataObj.GetTables()
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja deletar: ")

        if(tableName not in tables):
            input("Não é possível deletar um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        ShowIds(dataObj, tableName)

        oid = input("Digite o nome da chave do objeto que deseja deletar(chave de candidatura é o candidato, id da tabela para as demais tabelas): ")

        if(CheckIds( tableName, oid) == False):
            input("O id que se deseja deletar nao existe, aperte ENTER para voltar ao menu")
            return

        dataObj.Delete(tableName, oid)    
       
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserCreate(dataObj):
    try:
        print("########## UserCreate ##########")
        tables = dataObj.GetTables()
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja inserir: ")

        if(tableName not in tables):
            input("Não é possível inserir um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return
        
        columns = dataObj.GetColumns( tableName)

        valuesNames = ""
        values = ""
        for column in columns:
            if(column[5] == "auto_increment"):
                continue
            if(column[2] == "YES"):
                option = input("Deseja inserir " + column[0] + "?(Y/N)")
                if(option != 'Y' and option != 'y'):
                    continue

            value = input("Digite um valor do tipo " + column[1] + " para " + column[0] + ": ")

            if(column[1] == "longblob"):
                value = "\"" + str(GetImg(value)) + "\""
                print("A")
            
            if len(valuesNames):
                valuesNames += ", "
            if len(values):
                values += ", "
            
            valuesNames += column[0]
            values += value

        dataObj.Insert( tableName, valuesNames, values)

    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserUpdate(dataObj):
    try:
        print("########## UserUpdate ##########")
        tables = dataObj.GetTables()
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja atualizar: ")

        if(tableName not in tables):
            input("Não é possível atualizar um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return
        
        ShowIds(dataObj, tableName)
        
        id = input("\nDigite o id do item que deseja atualizar: ")

        if(CheckIds( tableName, id) == False):
            input("O id que se deseja atualizar nao existe, aperte ENTER para voltar ao menu")
            return

        ShowAtb(dataObj, tableName, id)
        
        name, value = input("Digite o nome do valor e o novo valor que deseja atribuir separados por espaco: ").split(" ")

        if(CheckColumn( tableName, name) == False):
            input("O atributo que se deseja atualizar nao existe, aperte ENTER para voltar ao menu")
            return


        if(name == "foto"):
            value = "\"" + str(GetImg(value)) + "\""
            print("A")

        dataObj.Update( tableName, name, value, id)
        input("Aperte ENTER para retornar ao menu")
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserRead(dataObj):
    try:
        print("########## UserRead ##########")

        tables = dataObj.GetTables()
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja ler: ")

        if(tableName not in tables):
            input("Não é possível ler um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        ShowColumns( tableName)

        atbs = input("Digite os nomes dos atributos que deseja ver separados por virgula (sem espaços): ")
        columns = atbs.split(",")

        for column in columns:
            if(CheckColumn( tableName, column) == False):
                input("Não é possível ler o dado " + column + " aperte ENTER para voltar ao menu")
                return

        data = dataObj.Read( atbs, tableName)

        for item in data:
            print("\nAtributo -- Valor")
            print("------------------")
            for i in range(len(item)):
                print(str(columns[i]) + ": " + str(item[i]))

        input("\nDigite ENTER para retornar ao menu")
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserSpecial(dataObj):
    try:
        # cursor = conn_db.cursor()

        print("########## UserSpecial ##########")
        print("#1 - Candidatos de um local                           #")
        print("#2 - Candidatos de um partido                         #")
        print("#3 - Partidos de uma coligacao                        #")
        # print("#4 - Candidatos de um local e partido especificos     #")

        option = input("# Opção: ")

        if(option == "1" or option == "Candidatos de um local"):
            clear()
            local = input("Digite o nome do local: ")
            data = dataObj.CandidatoGetLocal( "Local", local)
            for item in data:
                print("Id -- Nome")
                print("----------------------")
                print(str(item[0]) + "--" + str(item[1]) + "\n")
            input("Digite ENTER para voltar ao menu")

        elif(option == "2" or option == "Candidatos de um partido"):
            clear()
            partido = input("Digite o nome do partido: ")
            data = dataObj.CandidatoGetPartido( "Partido", partido)
            for item in data:
                print("Id -- Nome")
                print("----------------------")
                print(str(item[0]) + "--" + str(item[1]) + "\n")
            input("Digite ENTER para voltar ao menu")
        
        elif(option == "3" or option == "Partidos de uma coligacao"):
            clear()
            colig = input("Digite o nome da coligacao: ")
            data = dataObj.PartidoGetColig( "Coligacao", colig)
            for item in data:
                print("Id -- Nome")
                print("----------------------")
                print(str(item[0]) + "--" + str(item[1]) + "\n")
            input("Digite ENTER para voltar ao menu")
       
        # elif(option == "4" or option == "Candidatos de um local e partido especificos"):
        #     clear()
        #     colig = input("Digite o nome do local: ")
        #     data = dataObj.PartidoGetColig( "Coligacao", colig)
        #     for item in data:
        #         print("Id -- Nome")
        #         print("----------------------")
        #         print(str(item[0]) + "--" + str(item[1]))
        #     input("Digite ENTER para voltar ao menu")
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

if __name__ == "__main__":


    user = input("Digite o nome do usuario mysql: ")
    passwd = input("Digite a senha do usuario mysql: ")

    # user = 'root'
    # passwd = 'root'

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    dataObj = dao()
    dataObj.conn_db(host="localhost", port=3306, user=user, passwd=passwd)
    op = input("Deseja criar/resetar o banco? (Y/N) ")

    if(op == "Y" or op == "y"):
        dataObj.CreateDb()
    dataObj.conn_db(host="localhost", db="mydb", port=3306, user=user, passwd=passwd)

    STAY = True

    while(STAY):
        clear()
        print("###################")
        print("# Inserir             - 1   #")
        print("# Atualizar           - 2   #") 
        print("# Ler                 - 3   #")
        print("# Remover             - 4   #")
        print("# Consulta especial   - 5   #")
        print("#                           #")
        print("# Sair                - 6   #")
        print("###################")
        option = input("# Opção: ")

        if(option == "1" or option == "Inserir"):
            clear()
            UserCreate(dataObj)
        elif(option == "2" or option == "Atualizar"):
            clear()
            UserUpdate(dataObj)
        elif(option == "3" or option == "Ler"):
            clear()
            UserRead(dataObj)
        elif(option == "4" or option == "Remover"):
            clear()
            UserDelete(dataObj)
        elif(option == "5" or option == "Consulta especial"):
            clear()
            UserSpecial(dataObj)
        elif(option == "6" or option == "Sair"):
            clear()
            STAY = False 
    
    dataObj.close()
