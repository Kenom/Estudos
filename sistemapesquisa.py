import sys
import os

register_name = ['Wesley','Maia','Silva','Glaydson','Julia','Jeff','arthur','Carol','Renata','Patricia','Gabriel']
name_search = ''
user_pass = '123456'

login = input('Digite o Usuário: ')
user_pass_auth = input('Digite a Senha: ')

if login in register_name and user_pass_auth == user_pass:
    print('Login com Sucesso')
else:
    print('Usuário ou senha incorreto! PROGRAMA ENCERRADO!')
    sys.exit()


def pesquisa_search(name_search,register_name):
    if name_search in register_name:
        print('Nome encontrado!')
    elif name_search not in register_name:
        print("Registro não Encontrado!")
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


