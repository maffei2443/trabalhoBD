#import acessaBanco
#import Delete
#import Read
# import Update
# import Create

#Arquivo para a implementação da interface com o usuário.

def UserDelete():
    print("UserDelete")
def UserCreate():
    print("UserCreate")
def UserUpdate():
    print("UserUpdate")
def UserRead():
    print("UserRead")

def main():
    
    STAY = True

    while(STAY):
        print("###################")
        print("# Inserir   - 1   #")
        print("# Atualizar - 2   #") 
        print("# Ler       - 3   #")
        print("# Remover   - 4   #")
        print("#                 #")
        print("# Sair      - 5   #")
        print("###################")
        print("# Opção: ")
        option = int(input())

        if(option == 1):
            UserCreate()
        elif(option == 2):
            UserUpdate()
        elif(option == 3):
            UserRead()
        elif(option == 4):
            UserDelete()
        elif(option == 5):
            STAY = False 
    

main()           
