import MySQLdb

# Cria conexao com o banco. No caso, caso você possua uma instância do MySQL rodando
# localmente, pode-se atribuir ao parâmetro host o valor "localhost"
conn_db = _mysql.connect(host="172.17.0.2", port=3306, user="root", passwd="root")

# Mandar como parâmetro uma string, que será executada como um query SQL
conn_db.query("create database trabd")
conn_db.query("use trabd;")

# Pronto! Usar o db.query() é como se estivesse na CLI do mysql.
# PS: db.query("show databases;") DÁ ERRO e dps disso só consegui acessa o banco 
# normalmente após fechar a conexão.

# FECHAR conexão com o banco
conn_db.close()