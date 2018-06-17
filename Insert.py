#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

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

