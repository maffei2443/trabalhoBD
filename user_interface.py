#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import base64
from CRUD import dao

def get_img(img):
    with open(img, "rb") as file:
        ret = base64.b64encode(file.read())
        return ret

def clear():
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            print("Não foi possível limpar a tela.")

def show_atb(data_obj, table_name, key):
    data = data_obj.GetAllTab(table_name, key)
    columns = data_obj.GetColumns(table_name)

    print("\nNome do atributo -- Valor")
    print("-------------------------")
    for i in range(len(data[0])):
        print(str(columns[i][0]) + " -- " + str(data[0][i]))

def show_columns(data_obj, table_name):
    columns = data_obj.GetColumns(table_name)
    print("Atributos de " +  table_name + ":")
    for column in columns:
        print(column[0])

def show_ids(data_obj, table_name):
    keys = data_obj.GetIds(table_name)

    print("id -- Nome")
    print("-----------")
    for item in keys:
        print(str(item[0]) + " -- " + item[1])

def check_ids(data_obj, table_name, key):
    keys = data_obj.GetIds(table_name)

    exist = False
    for item in keys:
        if key == str(item[0]):
            exist = True
    return exist

def check_column(data_obj, table_name, name):
    columns = data_obj.GetColumns(table_name)

    exist = False
    for column in columns:
        if column[0] == name:
            exist = True
    return exist

def user_delete(data_obj):
    try:
        print("user_delete")
        tables = data_obj.GetTables()
        for table in tables:
            print("-- " + table)

        table_name = input("\nDigite o nome do tipo de dado que deseja deletar: ")

        if table_name not in tables:
            input("Não é possível deletar um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        show_ids(data_obj, table_name)

        key = input("Digite o nome da chave do objeto que deseja deletar(chave de candidatura é o candidato, id da tabela para as demais tabelas): ")

        if check_ids(data_obj, table_name, key) == False:
            input("O id que se deseja deletar nao existe, aperte ENTER para voltar ao menu")
            return

        data_obj.Delete(table_name, key)

    except Exception as exception:
        print(exception)
        input("Digite algo para voltar ao menu")

def user_create(data_obj):
    try:
        print("########## user_create ##########")
        tables = data_obj.GetTables()
        for table in tables:
            print("-- " + table)

        table_name = input("\nDigite o nome do tipo de dado que deseja inserir: ")

        if table_name not in tables:
            input("Não é possível inserir um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        columns = data_obj.GetColumns(table_name)

        values_names = ""
        values = ""
        for column in columns:
            if column[5] == "auto_increment":
                continue
            if column[2] == "YES":
                option = input("Deseja inserir " + column[0] + "?(Y/N)")
                if option != 'Y' and option != 'y':
                    continue

            value = input("Digite um valor do tipo " + column[1] + " para " + column[0] + ": ")

            if column[1] == "longblob":
                value = "\"" + str(get_img(value)) + "\""
                print("A")

            if len(values_names):
                values_names += ", "
            if len(values):
                values += ", "

            values_names += column[0]
            values += value

        data_obj.Insert(table_name, values_names, values)

    except Exception as exception:
        print(exception)
        input("Digite algo para voltar ao menu")

def user_update(data_obj):
    try:
        print("########## user_update ##########")
        tables = data_obj.GetTables()
        for table in tables:
            print("-- " + table)

        table_name = input("\nDigite o nome do tipo de dado que deseja atualizar: ")

        if table_name not in tables:
            input("Não é possível atualizar um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        show_ids(data_obj, table_name)

        key = input("\nDigite o id do item que deseja atualizar: ")

        if not check_ids(data_obj, table_name, key):
            input("O id que se deseja atualizar nao existe, aperte ENTER para voltar ao menu")
            return

        show_atb(data_obj, table_name, key)

        name, value = input("Digite o nome do valor e o novo valor que deseja atribuir separados por espaco: ").split(" ")

        if not check_column(data_obj, table_name, name):
            input("O atributo que se deseja atualizar nao existe, aperte ENTER para voltar ao menu")
            return


        if name == "foto":
            value = "\"" + str(get_img(value)) + "\""
            print("A")

        data_obj.Update(table_name, name, value, key)
        input("Aperte ENTER para retornar ao menu")
    except Exception as exception:
        print(exception)
        input("Digite algo para voltar ao menu")

def user_read(data_obj):
    try:
        print("########## user_read ##########")

        tables = data_obj.GetTables()
        for table in tables:
            print("-- " + table)

        table_name = input("\nDigite o nome do tipo de dado que deseja ler: ")

        if table_name not in tables:
            input("Não é possível ler um dado do tipo desejado, aperte ENTER para voltar ao menu")
            return

        show_columns(data_obj, table_name)

        atbs = input("Digite os nomes dos atributos que deseja ver separados por virgula (sem espaços): ")
        columns = atbs.split(",")

        for column in columns:
            if not check_column(data_obj, table_name, column):
                input("Não é possível ler o dado " + column + " aperte ENTER para voltar ao menu")
                return

        data = data_obj.Read(atbs, table_name)

        for item in data:
            print("\nAtributo -- Valor")
            print("------------------")
            for i in range(len(item)):
                print(str(columns[i]) + ": " + str(item[i]))

        input("\nDigite ENTER para retornar ao menu")
    except Exception as exception:
        print(exception)
        input("Digite algo para voltar ao menu")

def user_special(data_obj):
    try:
        # cursor = conn_db.cursor()

        print("########## user_special ##########")
        print("#1 - Candidatos de um local                           #")
        print("#2 - Candidatos de um partido                         #")
        print("#3 - Partidos de uma coligacao                        #")
        # print("#4 - Candidatos de um local e partido especificos     #")

        option = input("# Opção: ")

        if option == "1" or option == "Candidatos de um local":
            clear()
            local = input("Digite o nome do local: ")
            data = data_obj.CandidatoGetLocalProc("Local", local)
            for item in data:
                print("Id -- Nome")
                print("----------------------")
                print(str(item[0]) + "--" + str(item[1]) + "\n")
            input("Digite ENTER para voltar ao menu")

        elif option == "2" or option == "Candidatos de um partido":
            clear()
            partido = input("Digite o nome do partido: ")
            data = data_obj.CandidatoGetPartido("Partido", partido)
            for item in data:
                print("Id -- Nome")
                print("----------------------")
                print(str(item[0]) + "--" + str(item[1]) + "\n")
            input("Digite ENTER para voltar ao menu")

        elif option == "3" or option == "Partidos de uma coligacao":
            clear()
            colig = input("Digite o nome da coligacao: ")
            data = data_obj.PartidoGetColig("Coligacao", colig)
            for item in data:
                print("Id -- Nome")
                print("----------------------")
                print(str(item[0]) + "--" + str(item[1]) + "\n")
            input("Digite ENTER para voltar ao menu")

        # elif option == "4" or option == "Candidatos de um local e partido especificos":
        #     clear()
        #     colig = input("Digite o nome do local: ")
        #     data = data_obj.PartidoGetColig("Coligacao", colig)
        #     for item in data:
        #         print("Id -- Nome")
        #         print("----------------------")
        #         print(str(item[0]) + "--" + str(item[1]))
        #     input("Digite ENTER para voltar ao menu")
    except Exception as exception:
        print(exception)
        input("Digite algo para voltar ao menu")

def main():
    user = input("Digite o nome do usuario mysql: ")
    passwd = input("Digite a senha do usuario mysql: ")

    # user = 'root'
    # passwd = 'root'

    # Cria conexao com o banco. No caso, caso voce possua uma instancia do MySQL rodando
    # localmente, pode-se atribuir ao parametro host o valor "localhost"
    data_obj = dao()
    data_obj.conn_db(host="localhost", port=3306, user=user, passwd=passwd)
    option = input("Deseja criar/resetar o banco? (Y/N) ")

    if option == "Y" or option == "y":
        data_obj.CreateDb()
    data_obj.conn_db(host="localhost", db="mydb", port=3306, user=user, passwd=passwd)

    stay = True

    while stay:
        clear()
        print("###################")
        print("# Inserir             - 1   #")
        print("# Atualizar           - 2   #")
        print("# Ler                 - 3   #")
        print("# Remover             - 4   #")
        print("# Consulta especial   - 5   #")
        print("#                           #")
        print("# Sair                - 6   #")
        print("###################")
        option = input("# Opção: ")

        if option == "1" or option == "Inserir":
            clear()
            user_create(data_obj)
        elif option == "2" or option == "Atualizar":
            clear()
            user_update(data_obj)
        elif option == "3" or option == "Ler":
            clear()
            user_read(data_obj)
        elif option == "4" or option == "Remover":
            clear()
            user_delete(data_obj)
        elif option == "5" or option == "Consulta especial":
            clear()
            user_special(data_obj)
        elif option == "6" or option == "Sair":
            clear()
            stay = False

    data_obj.close()

if __name__ == "__main__":
    main()
