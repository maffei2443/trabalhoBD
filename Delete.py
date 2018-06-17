#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def Delete(tabela):
    
    # No campo "passwd" coloca a senha correspondente ao seu MySQL
    conn_db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="noobsaibot")
    cursor = conn_db.cursor()

    # Monta e executa a Query
    QueryString = "DELETE FROM " + tabela
    cursor.execute(QueryString)
    dados = cursor.fetchall()

    # Encerra a conexão com a base
    conn_db.close()

    return dados

# Código para teste
tabela = input("Tabela: ")
print(Delete(tabela))   