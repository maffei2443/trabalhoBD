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
if __name__ == "__main__":
    # Código para teste
    tabela = input("Tabela: ")
    print(Delete(tabela))   