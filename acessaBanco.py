import MySQLdb

# Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
# localmente, pode-se atribuir ao parametro host o valor "localhost"
conn_db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="q123q123")

# Usar cursor para fazer queries sql
cursor = conn_db.cursor()

print "Digite o caminho absoluto para o script que cria o banco de dados"
createScript = input()

query = ""
for line in open(createScript):
    if(line.find("--")):
        query += line
        if(line[-1] == ';'):
            cursor.execute(query)
            query = ""

# Teste de insercao na tabela "mydb.Local"
cursor.execute("SELECT * FROM mydb.Local")
print(cursor.fetchall())

cursor.execute("INSERT INTO mydb.Local"+
                "(idLocal, Nome, Regiao, EstatisticaPartidaria)"+
                "VALUES (1, \"Cidade\", \"GO\", \"Muito bom\");")

cursor.execute("INSERT INTO mydb.Local"+
                "(idLocal, Nome, Regiao, EstatisticaPartidaria)"+
                "VALUES (2, \"Aguas Filtradas\", \"MG\", \"Divertido\");")

cursor.execute("SELECT * FROM mydb.Local")
print(cursor.fetchall())

# FECHAR conexao com o banco
conn_db.close()