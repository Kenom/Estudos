#Código criado por Wesley Maia#
#Voltado totalmente a estudo de Python#

import sys
import os
import pickle

from datetime import date


with open("data.txt", "rb") as file:    #Abre o arquivo data.txt , que possui a lista como um "database"
    register_name = pickle.load(file)


# register_name = ['Wesley','Maia','Silva','Glaydson','Julia','Jeff','arthur','Carol','Renata','Patricia','Gabriel'] #lista inicial criada com valores já previamente salvos.
name_search = ''
user_pass = '123456'

login = input('Digite o Usuário: ')
user_pass_auth = input('Digite a Senha: ')

if login in register_name and user_pass_auth == user_pass:
    print('Login com Sucesso')
else:
    print('Usuário ou senha incorreto! PROGRAMA ENCERRADO!')
    sys.exit()

def data_horario(data):
    "Func data_horario for when called, displays date"
    hj = date.today()
    print(hj)
    return data

def remove_register(remove,register_name):
    "Func response for deleting registers in var list register_name"
    if remove in register_name:
        register_name.remove(remove)
    elif remove not in register_name:   #Caso o valor não esteja em register ele fecha um loop até um valor válido ser aceito.
        while remove not in register_name:
            remove = input("Esse nome não se encontra na Lista, Digite um válido: ")
        return remove


def pesquisa_search(name_search,register_name):
    "Func response for search names in var list register_name"
    if name_search in register_name:
        print('Nome encontrado!')
    elif name_search not in register_name:  #Caso o valor não esteja em register ele fecha um loop até um valor válido ser aceito.
        while name_search not in register_name:
            name_search = input("Por favor digite um numero válido: ")
    return register_name

def cadastro_register(cadastramento,register_name):
    "Func response for register new values in var list register_name"
    if cadastramento in register_name:
        print('Esse nome já contra no banco de Dados!')
    else:
        register_name.append(cadastramento)
        print(register_name)
        print('Registro feito com sucesso!')
        return register_name

def while_escolha(opc1):
    while opc1 != (1, 2, 3):
        "Func loop for menu , forcing them to choose a value"
        print("Digite uma Opção Válida: ")
        opc1 = int(input(" 1- Cadastrar Usuário \n 2- Remover Usuário \n 3- Pesquisar Usuario \n"))
    return opc1


def escolha_func(opc1):
    "Func MENU , need value 1,2 or 3 for software to continue"
    if opc1 == 1:
        cadastramento = input('Qual nome deseja Cadastrar? ')
        cadastro_register(cadastramento, register_name)
        os.system('pause')
    elif opc1 == 2:
        remove = input("Escreva o nome que  gostaria de remover da Lista: ")
        remove_register(remove, register_name)
        print("Usuário removido com sucesso: ")
        print(register_name)
    elif opc1 == 3:
        name_search = input('Qual o nome deseja Pesquisar? ')
        pesquisa_search(name_search, register_name)
    else:
        while_escolha(opc1)
    return opc1

opc1 = int(input(" 1- Cadastrar Usuário \n 2- Remover Usuário \n 3- Pesquisar Usuario \n"))  #Menu de opções onde o usuário precisa inserir os valores 1,2 ou 3
escolha_func(opc1)


with open("data.txt", "wb") as file:  #Save infos in data.txt
    pickle.dump(register_name, file)
data_horario(date)