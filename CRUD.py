#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import re
class dao(object):
    """Data access object. Realiza todo o acesso ao banco de dados."""
    def __init__(self):
        self.conn = ''

    def __conn_db(self, db=''):
        self.conn_db( host='172.17.0.2', db=db, port=3306, user='root', passwd='root')        

    def conn_db(self, host='localhost', db='', port=3306, user='root', passwd='root'):
        try:
            if(db):
                self.conn = MySQLdb.connect(host=host, db='mydb', port=3306, user=user, passwd=passwd)    
            else:
                self.conn = MySQLdb.connect(host=host, port=3306, user=user, passwd=passwd)    
        except Exception as e:
            print("Não foi possível estabelecer a conexão com o banco.")
            return e
    def GetIds(self, table):
        cursor = self.conn.cursor()
        
        if(table != "Candidatura"):
            cursor.execute("SELECT id" + table + ", nome FROM " + table + ";")
        else:
            cursor.execute("SELECT id" + table + ",candidato FROM " + table + ";")

        ids = cursor.fetchall()
        
        return ids

    def GetAllTab(self, table, id):
        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM " + table + " WHERE id" + table + "=" + id + ";")
     
        return cursor.fetchall()

    def GetTables(self):
        cursor = self.conn.cursor()
        
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        tablesNames = []
        for table in tables:
            tablesNames.append(table[0])

        return tablesNames

    def GetColumns(self, table):
        cursor = self.conn.cursor()
            
        cursor.execute("SHOW columns FROM " + table)
        
        columns = cursor.fetchall()

        return columns

    def CandidatoGetLocal(self, table, value):
        cursor = self.conn.cursor()
        
        cursor.execute("select Candidato.idCandidato, Candidato.nome from Candidato inner join " + table + " on Candidato.origem=" + table + ".id" + table + " and " + table + ".nome=" + value)

        return cursor.fetchall()

    def CandidatoGetLocalProc(self, table, value):
        cursor = self.conn.cursor()
        
        cursor.execute("CALL candlocal(" + value + ")")

        return cursor.fetchall()


    def CandidatoGetPartido(self, table, value):
        cursor = self.conn.cursor()
        
        cursor.execute("select Candidato.idCandidato, Candidato.nome from Candidato inner join " + table + " on Candidato.partido=" + table + ".id" + table + " and " + table + ".nome=" + value)

        return cursor.fetchall()

    def PartidoGetColig(self, table, value):
        cursor = self.conn.cursor()
        
        cursor.execute("select Partido.idPartido, Partido.nome from Partido inner join " + table + " on Partido.coligacao=" + table + ".id" + table + " and " + table + ".nome=" + value)

        return cursor.fetchall()

    def Delete(self, table, value):
        # No campo "passwd" coloca a senha correspondente ao seu MySQL
        cursor = self.conn.cursor()
        
        cursor.execute("DELETE FROM " + table + " WHERE id" + table + " = " + value + ";")
        # Monta e executa a Query
        dados = cursor.fetchall()

        self.conn.commit()
        return dados

    def Insert(self, table, valuesNames, values):
        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO " + table +
                        " (" + valuesNames + ") "+
                        "VALUES (" + values + ");")
        self.conn.commit()

    def Read(self, coluna, tabela):
        cursor = self.conn.cursor()

        # Monta e executa a Query
        QueryString = "SELECT " + coluna + " FROM " + tabela + ";"
        cursor.execute(QueryString)
        dados = cursor.fetchall()

        return dados

    def Update(self, table, fieldName, newValue, id):
        # No campo "passwd" coloca a senha correspondente ao seu MySQL
        cursor = self.conn.cursor()

        # Monta e executa a Query
        QueryString = "UPDATE " + table + " SET " + fieldName + " = " + newValue + " WHERE id" + table + " = " + id + ";"

        cursor.execute(QueryString)
        self.conn.commit()

    def CreateDb(self):
        # Usar cursor para fazer queries sql
        cursor = self.conn.cursor()

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

    def commit(self):
        if( re.findall(r"class (.*?)dao'", str(type(self.conn))) ):
            self.conn.commit()

    def close(self):
        # Testa pra ver se o atributo self.conn é mesmo da classe dao.
        if( re.findall(r"class (.*?)dao'", str(type(self.conn))) ):
            self.conn.close()
