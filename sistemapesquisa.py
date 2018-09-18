import sys
import os
import pickle

from datetime import date


with open("data.txt", "rb") as file:    #Abre o arquivo data.txt , que possui a lista como um "database"
    register_name = pickle.load(file)


# register_name = ['Wesley','Maia','Silva','Glaydson','Julia','Jeff','arthur','Carol','Renata','Patricia','Gabriel']
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
    hj = date.today()
    print(hj)
    return data

def remove_register(remove,register_name):
    if remove in register_name:
        register_name.remove(remove)
    elif remove not in register_name:
        while remove not in register_name:
            remove = input("Esse nome não se encontra na Lista, Digite um válido: ")
        return remove


def pesquisa_search(name_search,register_name):
    if name_search in register_name:
        print('Nome encontrado!')
    elif name_search not in register_name:
        while name_search not in register_name:
            name_search = input("Por favor digite um numero válido: ")
    return register_name

def cadastro_register(cadastramento,register_name):
    if cadastramento in register_name:
        print('Esse nome já contra no banco de Dados!')
    else:
        register_name.append(cadastramento)
        print(register_name)
        print('Registro feito com sucesso!')
        return register_name
cadastramento = input('Qual nome deseja Cadastrar? ')

cadastro_register(cadastramento, register_name)
os.system('pause')

name_search = input('Qual o nome deseja Pesquisar? ')
pesquisa_search(name_search,register_name)

remove = input ("Escreva o nome que  gostaria de remover da Lista: ")
remove_register(remove,register_name)

print("Usuário removido com sucesso: ")
print(register_name)

with open("data.txt", "wb") as file:  # "Salva a variavel List em um arquivo data.txt como um database
    pickle.dump(register_name, file)
data_horario(date)


