#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os
from CRUD import *

def clear():
    os.system("clear")

def UserDelete(conn_db):
    print("UserDelete")

def UserCreate(conn_db):
    print("########## UserCreate ##########")
    tables = GetTables(conn_db)
    for table in tables:
        print("-- " + table)

    tableName = input("\nDigite o nome do que deseja inserir: ")
    
    columns = GetColumns(conn_db, tableName)

    valuesNames = ""
    values = ""
    for column in columns:
        if(column[2] == "YES"):
            option = input("Deseja inserir o valor de " + column[0] + "?(Y/N)")
            if(option != 'Y' and option != 'y'):
                continue
        value = input("Digite um valor do tipo " + column[1] + " para " + column[0] + ": ")
        if(column[1].find("varchar") != -1):
            value = "\"" + value + "\""
        if len(valuesNames):
            valuesNames += ", "
        if len(values):
            values += ", "
        
        valuesNames += column[0]
        values += value

    Insert(conn_db, tableName, valuesNames, values)

def UserUpdate(conn_db):
    print("UserUpdate")
    Update(conn_db)

def UserRead(conn_db):
    print("########## UserRead ##########")

    tables = GetTables(conn_db)
    for table in tables:
        print("-- " + table)

    tableName = input("\nDigite o nome do que deseja ler ")

    print(Read(conn_db, "*", tableName))

    input("\n Digite enter para continuar")

if __name__ == "__main__":
    user = input("Digite o nome do usuario mysql: ")
    passwd = input("Digite a senha do usuario mysql: ")

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    conn_db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd)

    op = input("Deseja criar/resetar o banco? (Y/N)")

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
