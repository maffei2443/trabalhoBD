#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def Delete(conn_db, tabela):
    # No campo "passwd" coloca a senha correspondente ao seu MySQL
    cursor = conn_db.cursor()

    # Monta e executa a Query
    QueryString = "DELETE FROM " + tabela
    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados


#######################################################################################################


def Insert(conn_db):
    cursor = conn_db.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])
    
    print("Digite o nome da tabela na qual deseja inserir dados: ")
    tableName = input()
    cursor.execute("SHOW columns FROM " + tableName)
    
    columns = cursor.fetchall()
    
    valuesNames = ""
    values = ""
    for column in columns:
        print("Digite um valor do tipo " + column[1] + " para a coluna " + column[0] + ": ")
        value = input()
        if len(valuesNames):
            valuesNames += ", "
        if len(values):
            values += ", "
        
        valuesNames += column[0]
        values += value

    cursor.execute("INSERT INTO " + tableName +
                    " (" + valuesNames + ") "+
                    "VALUES (" + values + ");")


#######################################################################################################


def Read(conn_db, coluna, tabela):
    cursor = conn_db.cursor()

    # Monta e executa a Query
    QueryString = "SELECT " + coluna + " FROM " + tabela
    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados



#######################################################################################################


def Update(conn_db):
    # No campo "passwd" coloca a senha correspondente ao seu MySQL
    cursor = conn_db.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        print(table[0])

    print("Digite o nome da tabela na qual deseja atualizar os dados: ")
    tableName = input()
    cursor.execute("SELECT * FROM " + tableName)
    print("\n")

    print(cursor.fetchall())
    columns = cursor.fetchall()


    for column in columns:
        print(column[0])

    print("Digite o nome dos campos nos quais deseja atualizar os dados: ")
    fieldsName = input().split(" ")

    values = []
    for field in fieldsName:
        print("Digite um novo valor para o campo " + field + ": ")
        values.append( input())

    # Monta e executa a Query
    QueryString = "UPDATE " + tableName + " SET "

    i = 0
    for field in fieldsName:
        QueryString += field + " = " + values[i]
        i += 1
        if i == len(values) - 1:
            QueryString += ", "

    print(QueryString)

    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados


#######################################################################################################


def CreateDb(conn_db):
    # Usar cursor para fazer queries sql
    cursor = conn_db.cursor()

    createScript = "criaBanco.sql"

    query = ""

    for line in open(createScript):
        if(line.find("--")):
            line = line.rstrip("\n")
            query += line
            if(line.endswith(";")):
                cursor.execute(query)
                query = ""
                
    print("Banco de dados mydb criado com sucesso")
