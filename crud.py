#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import MySQLdb

class dao(object):
    """Data access object. Realiza todo o acesso ao banco de dados."""
    def __init__(self, host='localhost', db='', port=3306,
                 user='root', passwd='root'):
        self.conn_db(host, db, port, user, passwd)

    def __conn_db(self, db=''):
        self.conn_db(host='172.17.0.2', db=db, port=3306,
                     user='root', passwd='root')

    def conn_db(self, host='localhost', db='', port=3306, user='root', passwd='root'):
        try:
            if db:
                self.conn = MySQLdb.connect(host=host, db='mydb', port=port,
                                            user=user, passwd=passwd)
            else:
                self.conn = MySQLdb.connect(host=host, port=port,
                                            user=user, passwd=passwd)
        except Exception:
            print("Não foi possível estabelecer a conexão com o banco.")

    def get_ids(self, table):
        cursor = self.conn.cursor()

        if table != "Candidatura":
            cursor.execute("SELECT id" + table + ", nome FROM " + table + ";")
        else:
            cursor.execute("SELECT id" + table + ",candidato FROM " + table + ";")

        keys = cursor.fetchall()

        return keys

    def get_all_tab(self, table, key):
        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM " + table + " WHERE id" + table + "=" + key + ";")

        return cursor.fetchall()

    def get_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        tables_names = []
        for table in tables:
            tables_names.append(table[0])

        return tables_names

    def get_columns(self, table):
        cursor = self.conn.cursor()

        cursor.execute("SHOW columns FROM " + table)

        columns = cursor.fetchall()

        return columns

    def candidato_get_local(self, table, value):
        cursor = self.conn.cursor()

        cursor.execute("select Candidato.idCandidato, Candidato.nome from Candidato inner join " +
                       table + " on Candidato.origem=" + table +
                       ".id" + table + " and " + table + ".nome=" + value)

        return cursor.fetchall()

    def CandidatoGetLocalProc(self, table, value):
        cursor = self.conn.cursor()
        
        cursor.execute("CALL candlocal(" + value + ")")

        return cursor.fetchall()


    def candidato_get_partido(self, table, value):
        cursor = self.conn.cursor()

        cursor.execute("select Candidato.idCandidato, Candidato.nome from Candidato inner join " +
                       table + " on Candidato.partido=" + table + ".id" +
                       table + " and " + table + ".nome=" + value)

        return cursor.fetchall()

    def partido_get_colig(self, table, value):
        cursor = self.conn.cursor()

        cursor.execute("select Partido.idPartido, Partido.nome from Partido inner join " +
                       table + " on Partido.coligacao=" + table +".id" +
                       table + " and " + table + ".nome=" + value)

        return cursor.fetchall()

    def delete(self, table, value):
        # No campo "passwd" coloca a senha correspondente ao seu MySQL
        cursor = self.conn.cursor()

        cursor.execute("DELETE FROM " + table + " WHERE id" + table + " = " + value + ";")
        # Monta e executa a Query
        dados = cursor.fetchall()

        self.conn.commit()
        return dados

    def insert(self, table, values_names, values):
        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO " + table +
                       " (" + values_names + ") "+
                       "VALUES (" + values + ");")
        self.conn.commit()

    def read(self, coluna, tabela):
        cursor = self.conn.cursor()

        # Monta e executa a Query
        query_string = "SELECT " + coluna + " FROM " + tabela + ";"
        cursor.execute(query_string)
        dados = cursor.fetchall()

        return dados

    def update(self, table, field_name, new_value, key):
        # No campo "passwd" coloca a senha correspondente ao seu MySQL
        cursor = self.conn.cursor()

        # Monta e executa a Query
        query_string = "UPDATE " + table + " SET " + field_name + " = " + new_value
        query_string += " WHERE id" + table + " = " + key + ";"

        cursor.execute(query_string)
        self.conn.commit()

    def create_db(self):
        # Usar cursor para fazer queries sql
        cursor = self.conn.cursor()

        create_script = "criaBanco.sql"

        query = ""

        for line in open(create_script):
            if line.find("--"):
                line = line.rstrip("\n")
                query += line
                if line.endswith(";"):
                    cursor.execute(query)
                    query = ""

        print("Banco de dados mydb criado com sucesso")

    def commit(self):
        if re.findall(r"class (.*?)dao'", str(type(self.conn))):
            self.conn.commit()

    def close(self):
        # Testa pra ver se o atributo self.conn é mesmo da classe dao.
        if re.findall(r"class (.*?)dao'", str(type(self.conn))):
            self.conn.close()
