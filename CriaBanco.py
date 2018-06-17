#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def CriaBanco(conn_db):
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