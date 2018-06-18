#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os
from CRUD import *

def clear():
    os.system("clear")

def UserDelete(conn_db):
    print("UserDelete")
    tables = GetTables(conn_db)
    for table in tables:
        print("-- " + table)

    tableName = input("\nDigite o nome do tipo de dado que deseja ler: ")

    if(tableName not in tables):
        input("Não é possível ler um dado do tipo desejado, aperte ENTER para voltar ao menu")
        return

    keyValue = input("Digite o nome da chave do objeto que deseja deletar(chave de candidatura é o candidato, id da tabela para as demais tabelas): ")


    cursor.execute("DELETE  FROM " + tableName + " WHERE " + field + " (SELECT * FROM (SELECT " + field + "")    


def UserCreate(conn_db):
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
        if(column[2] == "YES"):
            option = input("Deseja inserir o valor de " + column[0] + "?(Y/N)")
            if(option != 'Y' and option != 'y'):
                continue

        value = input("Digite um valor do tipo " + column[1] + " para " + column[0] + ": ")
        
        #if(column[1].find("INT") == -1):
        #   value = "\"" + value + "\""
        
        if len(valuesNames):
            valuesNames += ", "
        if len(values):
            values += ", "
        
        valuesNames += column[0]
        values += value

    Insert(conn_db, tableName, valuesNames, values)

    conn_db.commit()

def UserUpdate(conn_db):
    print("########## UserUpdate ##########")
    tables = GetTables(conn_db)
    for table in tables:
        print("-- " + table)

    tableName = input("\nDigite o nome do tipo de dado que deseja atualizar: ")

    if(tableName not in tables):
        input("Não é possível atualizar um dado do tipo desejado, aperte ENTER para voltar ao menu")
        return
    
    ids = GetIds(conn_db, tableName)

    print("id -- Nome")
    print("-----------")
    for item in ids:
        print(str(item[0]) + " -- " + item[1])

    id = input("\nDigite o id do item que deseja atualizar: ")

    dados = GetAllTab(conn_db, table, id)

    conn_db.commit()

def UserRead(conn_db):
    print("########## UserRead ##########")

    tables = GetTables(conn_db)
    for table in tables:
        print("-- " + table)

    tableName = input("\nDigite o nome do tipo de dado que deseja ler: ")

    if(tableName not in tables):
        input("Não é possível ler um dado do tipo desejado, aperte ENTER para voltar ao menu")
        return

    print(Read(conn_db, "*", tableName))

    input("\nDigite enter para continuar")

if __name__ == "__main__":
    user = input("Digite o nome do usuario mysql: ")
    passwd = input("Digite a senha do usuario mysql: ")

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    conn_db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd)

    op = input("Deseja criar/resetar o banco? (Y/N) ")

    if(op == "Y" or op == "y"):
        CreateDb(conn_db)

    conn_db = MySQLdb.connect(host="localhost", db="mydb", port=3306, user=user, passwd=passwd)

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
        option = int(input("# Opção: "))

        if(option == 1):
            clear()
            UserCreate(conn_db)
        elif(option == 2):
            clear()
            UserUpdate(conn_db)
        elif(option == 3):
            clear()
            UserRead(conn_db)
        elif(option == 4):
            clear()
            UserDelete(conn_db)
        elif(option == 5):
            clear()
            STAY = False 
    
    conn_db.close()
