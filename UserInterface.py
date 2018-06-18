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

    print("\nDigite o nome da tabela na qual deseja inserir dados: ")
    tableName = input()
    
    columns = GetColumns(conn_db, tableName)

    valuesNames = ""
    values = ""
    for column in columns:
        if(column[2] == "YES" or column[3] == "MUL"):
            print("Deseja manter o valor da coluna " + column[0] + " nulo?(Y/N)")
            option = input()
            if(option == 'Y' or option == 'y'):
                continue
        print("Digite um valor do tipo " + column[1] + " para a coluna " + column[0] + ": ")
        value = input()
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
    print("UserRead")

if __name__ == "__main__":
    print("Digite o nome do usuario mysql: ")
    user = input()
    print("Digite a senha do usuario mysql: ")
    passwd = input()

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    conn_db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd)

    print("Deseja criar/resetar o banco? (Y/N)")
    op = input()

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
        print("# Opção: ")
        option = int(input())

        if(option == 1):
            clear()
            UserCreate(conn_db)
        elif(option == 2):
            clear()
            UserUpdate(conn_db)
        elif(option == 3):
            clear()
            UserRead()
        elif(option == 4):
            clear()
            UserDelete(conn_db)
        elif(option == 5):
            clear()
            STAY = False 
    
    conn_db.close()