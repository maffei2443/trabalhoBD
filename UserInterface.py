#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os
from CRUD import *
# import PIL.Image
import base64

def clear():
    os.system("clear")

def Show_atb(conn_db, tableName, id):
    data = GetAllTab(conn_db, tableName, id)
    columns = GetColumns(conn_db, tableName)

    print("\nNome do atributo -- Valor")
    print("-------------------------")
    for i in range(len(data[0])):
        print(str(columns[i][0]) + " -- " + str(data[0][i]))

def Show_columns(conn_db, tableName):
    columns = GetColumns(conn_db, tableName)
    print("Atributos de " +  tableName + ":")
    for column in columns:
        print(column[0])

def Show_ids(conn_db, tableName):
    ids = GetIds(conn_db, tableName)

    print("id -- Nome")
    print("-----------")
    for item in ids:
        print(str(item[0]) + " -- " + item[1])

def Check_ids(conn_db, tableName, id):
    ids = GetIds(conn_db, tableName)    

    exist = False
    for item in ids:
        if(id == str(item[0])):
            exist = True
    return exist

def Check_column(conn_db, tableName, name):
    columns = GetColumns(conn_db, tableName)
    
    exist = False
    for column in columns:
        if(column[0] == name):
            exist = True
    return exist

def UserDelete(conn_db):
    try:
        print("UserDelete")
        tables = GetTables(conn_db)
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja deletar: ")

        if(tableName not in tables):
            input("Não é possível deletar um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        Show_ids(conn_db, tableName)

        id = input("Digite o nome da chave do objeto que deseja deletar(chave de candidatura é o candidato, id da tabela para as demais tabelas): ")

        if(Check_ids(conn_db, tableName, id) == False):
            input("O id que se deseja deletar nao existe, aperte ENTER para voltar ao menu")
            return

        Delete(conn_db, tableName, id)    
       
        conn_db.commit()
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserCreate(conn_db):
    try:
        print("########## UserCreate ##########")
        tables = GetTables(conn_db)
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja inserir: ")

        if(tableName not in tables):
            input("Não é possível inserir um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return
        
        columns = GetColumns(conn_db, tableName)

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
            
            if len(valuesNames):
                valuesNames += ", "
            if len(values):
                values += ", "
            
            valuesNames += column[0]
            values += value

        Insert(conn_db, tableName, valuesNames, values)

        conn_db.commit()
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserUpdate(conn_db):
    try:
        print("########## UserUpdate ##########")
        tables = GetTables(conn_db)
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja atualizar: ")

        if(tableName not in tables):
            input("Não é possível atualizar um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return
        
        Show_ids(conn_db, tableName)
        
        id = input("\nDigite o id do item que deseja atualizar: ")

        if(Check_ids(conn_db, tableName, id) == False):
            input("O id que se deseja atualizar nao existe, aperte ENTER para voltar ao menu")
            return

        Show_atb(conn_db, tableName, id)
        
        name, value = input("Digite o nome do valor e o novo valor que deseja atribuir separados por espaco: ").split(" ")

        if(Check_column(conn_db, tableName, name) == False):
            input("O atributo que se deseja atualizar nao existe, aperte ENTER para voltar ao menu")
            return

        Update(conn_db, tableName, name, value, id)
        input("Aperte ENTER para retornar ao menu")
        conn_db.commit()
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")

def UserRead(conn_db):
    try:
        print("########## UserRead ##########")

        tables = GetTables(conn_db)
        for table in tables:
            print("-- " + table)

        tableName = input("\nDigite o nome do tipo de dado que deseja ler: ")

        if(tableName not in tables):
            input("Não é possível ler um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        Show_columns(conn_db, tableName)

        atbs = input("Digite os nomes dos atributos que deseja ver separados por virgula (sem espaços): ")
        columns = atbs.split(",")

        for column in columns:
            if(Check_column(conn_db, tableName, column) == False):
                input("Não é possível ler o dado " + column + " aperte ENTER para voltar ao menu")
                return

        data = Read(conn_db, atbs, tableName)

        for item in data:
            print("\nAtributo -- Valor")
            print("------------------")
            for i in range(len(item)):
                print(str(columns[i]) + ": " + str(item[i]))

        input("\nDigite ENTER para retornar ao menu")
    except Exception as e:
        print(e)
        input("Digite algo para voltar ao menu")


if __name__ == "__main__":


    user = input("Digite o nome do usuario mysql: ")
    passwd = input("Digite a senha do usuario mysql: ")

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    conn_db = MySQLdb.connect(host="172.17.0.2", port=3306, user=user, passwd=passwd)

    op = input("Deseja criar/resetar o banco? (Y/N) ")

    if(op == "Y" or op == "y"):
        CreateDb(conn_db)

    conn_db = MySQLdb.connect(host="172.17.0.2", db="mydb", port=3306, user=user, passwd=passwd)

    STAY = True

    while(STAY):
        clear()
        print("###################")
        print("# Inserir   - 1   #")
        print("# Atualizar - 2   #") 
        print("# Ler       - 3   #")
        print("# Remover   - 4   #")
        print("#                 #")
        print("# Sair      - 5   #")
        print("###################")
        option = input("# Opção: ")

        if(option == "1" or option == "Inserir"):
            clear()
            UserCreate(conn_db)
        elif(option == "2" or option == "Atualizar"):
            clear()
            UserUpdate(conn_db)
        elif(option == "3" or option == "Ler"):
            clear()
            UserRead(conn_db)
        elif(option == "4" or option == "Remover"):
            clear()
            UserDelete(conn_db)
        elif(option == "5" or option == "Sair"):
            clear()
        elif(option == "6" or option == "photo"):
            clear()
            STAY = False 
    
    conn_db.close()
