#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def Read(conn_db, coluna, tabela):
    cursor = conn_db.cursor()

    # Monta e executa a Query
    QueryString = "SELECT " + coluna + " FROM " + tabela
    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados
if __name__ == "__main__":
    # Código para teste
    exp,db = input("Coluna e Tabela: ").split(" ")     
    print(Read(exp,db))