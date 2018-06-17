#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os
from CriaBanco import CriaBanco
from Delete import Delete
from Read import Read
from Insert import Insert
from Update import Update

def clear():
    os.system("clear")

def UserDelete():
    print("UserDelete")
def UserCreate():
    print("UserCreate")
    Insert(conn_db)
def UserUpdate():
    print("UserUpdate")
    Update(conn_db)
def UserRead():
    print("UserRead")

if __name__ == "__main__":
    print("Digite o nome do usuario mysql: ")
    user = raw_input()
    print("Digite a senha do usuario mysql: ")
    passwd = raw_input()

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    conn_db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd)

    print("Deseja criar/resetar o banco? (Y/N)")
    op = raw_input()

    if(op == "Y" or op == "y"):
        CriaBanco(conn_db)

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
        option = int(raw_input())

        if(option == 1):
            clear()
            UserCreate()
        elif(option == 2):
            clear()
            UserUpdate()
        elif(option == 3):
            clear()
            UserRead()
        elif(option == 4):
            clear()
            UserDelete()
        elif(option == 5):
            clear()
            STAY = False 
    
    conn_db.close()