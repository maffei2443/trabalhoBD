#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def GetIds(conn_db, table):
    cursor = conn_db.cursor()
    
    if(table != "Candidatura"):
        cursor.execute("SELECT id" + table + ", nome FROM " + table + ";")
    else:
        cursor.execute("SELECT id" + table + ",candidato FROM " + table + ";")

    ids = cursor.fetchall()
    
    return ids

def GetAllTab(conn_db, table, id):
    cursor = conn_db.cursor()

    cursor.execute("SELECT * FROM " + table + " WHERE id" + table + "=" + id + ";")
 
    return cursor.fetchall()

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

    tables = GetTables(conn_db)
    for i in tables:
        print(i)

    tableName = input("Digite o nome da tabela na qual deseja atualizar os dados: ")
    cursor.execute("SELECT * FROM " + tableName)

    obs = cursor.fetchall()

    for i in obs:
        print(i)
    print("\n")

    cursor.execute("DESCRIBE " + tableName)
    fields = cursor.fetchall()

    for i in fields:
        print(i[0])

    fieldName = input("Digite o nome do campo no qual deseja atualizar: ")

    newName = input("Digite o novo valor: ")
    
    cursor.execute("SELECT " + fieldName + " FROM " + tableName)

    keyValue = input("Digite o nome da chave do objeto que deseja atualizar(chave de candidatura é o candidato, id da tabela para as demais tabelas): ")

    if tableName == "Candidatura":
        keyName = "candidato"
    else:
        keyName = "id" + tableName


    # Monta e executa a Query
    QueryString = "UPDATE " + tableName + " SET " + fieldName + " = " + newName + " WHERE " + keyName + " = " + keyValue

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