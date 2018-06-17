#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def Update(conn_db):
    # No campo "passwd" coloca a senha correspondente ao seu MySQL
    cursor = conn_db.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])

    print("Digite o nome da tabela na qual deseja atualizar os dados: ")
    tableName = raw_input()
    cursor.execute("SELECT * FROM " + tableName)
    print "\n"

    columns = cursor.fetchall()

    for column in columns:
        print(column[0])

    print("Digite o nome dos campos na qual deseja atualizar os dados: ")
    fieldsName = raw_input().split(" ")

    values = []
    for field in fieldsName:
        print("Digite um novo valor para o campo " + field + ": ")
        values.append( raw_input())

    for v in values:
        print v + "\n"

    # Monta e executa a Query
    QueryString = "UPDATE " + tableName + " SET "

    i = 0
    for field in fieldsName:
        QueryString += field + " = " + values[i]
        i += 1
        if len(values):
            QueryString += ", "

    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados
if __name__ == "__main__":
    # Código para teste
    
    tabela = raw_input("Campos, Valores e Tabela: ").split(" ")
    print(Update(campos, valores, tabela))