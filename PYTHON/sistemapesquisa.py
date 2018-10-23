# Código criado por Wesley Maia #
# Voltado totalmente a estudo de Python #

import sys
import os
import pickle
import smtplib

from datetime import date


with open("data.txt", "rb") as file:    # open file data.txt , list names "database"
    register_name = pickle.load(file)

"register_name = ['Wesley','Maia','Silva','Glaydson','Julia','Jeff','arthur','Carol','Renata','Patricia','Gabriel'] #lista inicial criada com valores já previamente salvos."
name_search = ''
user_pass = '123456'

login = input('Digite o Usuário: ')
user_pass_auth = input('Digite a Senha: ')

if login in register_name and user_pass_auth == user_pass:
    print('Login com Sucesso')
else:
    print('Usuário ou senha incorreto! PROGRAMA ENCERRADO!')
    sys.exit()


### Seding_mail, envia um e-mail de origem GMAIL, utilizando a biblioteca smtplib
def seding_mail(opc_mail):
    opc1 = input("Enviar e-mail?\n1 - Sim \n 2 - Não")
    if opc1 == '1':
        # credentials
        remetente = 'keXXXX@gmail.com'
        senha = 'XXXXXXX'

        # information destination and title/context
        destinatario = 'XXXXX@outlook.com'
        assunto = 'Enviando email com python'
        texto = 'Esse email foi enviado usando python! :)'

        # preparing e-mail for send
        msg = '\r\n'.join([
            'From: %s' % remetente,
            'To: %s' % destinatario,
            'Subject: %s' % assunto,
            '',
            '%s' % texto
            ])

        # sending e-mail
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg)
        server.quit()
    elif opc1 == '2':
        print ("Ok, mensagem não será enviada.")



def letras_iniciais(register_name):
    search_letras = input ('Com qual letra deve começar?')
    if search_letras == register_name[0]:
        print (register_name [0] == search_letras)
    else:
        print ("Valor invalido!")


def data_horario(data):
    "Func data_horario for when called, displays date"
    hj = date.today()
    print(hj)
    return data

def remove_register(remove,register_name):
    "Func response for deleting registers in var list register_name"
    if remove in register_name:
        register_name.remove(remove)
    elif remove not in register_name:
        while remove not in register_name:
            remove = input("Esse nome não se encontra na Lista, Digite um válido: ")
        return remove


def pesquisa_search(name_search,register_name):
    "Func response for search names in var list register_name"
    if name_search in register_name:
        print('Nome encontrado!')
    elif name_search not in register_name:
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


opc1 = int(input(" 1- Cadastrar Usuário \n 2- Remover Usuário \n 3- Pesquisar Usuario \n"))
# Menu de opções onde o usuário precisa inserir os valores 1,2 ou 3 #
escolha_func(opc1)



with open("data.txt", "wb") as file:  # Save infos in data.txt
    pickle.dump(register_name, file)
data_horario(date)

