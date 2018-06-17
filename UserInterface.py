#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from CriaBanco import CriaBanco
from Delete import Delete
from Read import Read

if __name__ == "__main__":
    print("Digite o nome do usuario mysql: ")
    user = input()
    print("Digite a senha do usuario mysql: ")
    passwd = input()

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    conn_db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd)

    CriaBanco(conn_db)

    while 1:
        print("1 - Inserir dados")
        print("2 - Sair")
        op = int(input())
        if op == 1:
            print("nada nao")
        if op == 2:
            break

    conn_db.close()