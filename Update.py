#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

def Update(campos, valores, conn_db, tabela):
    # No campo "passwd" coloca a senha correspondente ao seu MySQL
    cursor = conn_db.cursor()

    cam[] = campos.split(",")
    val[] = valores.split(",")
    # Monta e executa a Query
    QueryString = "INSERT INTO " + tabela + " (" + campos + ") " + " (" + valores + ")" 
    
    for i in range(cam)
        QueryString += cam[i] + " = " + val[i] + ", "


    cursor.execute(QueryString)
    dados = cursor.fetchall()

    return dados
if __name__ == "__main__":
    # Código para teste
    
    tabela = raw_input("Campos, Valores e Tabela: ").split(" ")
    print(Update(campos, valores, tabela))