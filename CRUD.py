#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def GetTables(conn_db):
    cursor = conn_db.cursor()
    
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    tablesNames = []
    for table in tables:
        tablesNames.append(table[0])

    return tablesNames

def GetColumns(conn_db, table):
    cursor = conn_db.cursor()
        

    cursor.execute("SHOW columns FROM " + table)
    
    columns = cursor.fetchall()

    return columns

def Delete(conn_db, tabela):
    # No campo "passwd" coloca a senha correspondente ao seu MySQL
    cursor = conn_db.cursor()

    # Monta e executa a Query
    QueryString = "DELETE FROM " + tabela
    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados

def Insert(conn_db, table, valuesNames, values):
    cursor = conn_db.cursor()

    print("INSERT INTO " + table +
                    " (" + valuesNames + ") "+
                    "VALUES (" + values + ");")

    cursor.execute("INSERT INTO " + table +
                    " (" + valuesNames + ") "+
                    "VALUES (" + values + ");")

def Read(conn_db, coluna, tabela):
    cursor = conn_db.cursor()

    # Monta e executa a Query
    QueryString = "SELECT " + coluna + " FROM " + tabela
    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados

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

    for v in values:
        print(v + "\n")

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