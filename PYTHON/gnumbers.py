#Código UTF-8
# Generate numbers random
# Script for study  While, For, random , math, csv

import random
import math
import pickle
import csv

#listafinal = []   NÃO UTILIZADO MAIS
#n = 0 NÃO UTILIZADO MAIS



with open('lista.csv', 'w', newline='') as saida:
    escreva = csv.writer(saida)
    for i in range (1, 10):
        numberg = ((math.ceil(100000000 * random.random())))
        i = numberg
        escreva.writerow ([i])


# TRASH CODE \/


# ANTIGO CODIGO UTILIZANDO WHILE para efetuar o calculo e o save do arquivo, porém foi aposentado por não
# ser totalmente funcional.
#while n <= 10000:
#    ddd = 55119
#    numberg = ((math.ceil(100000000 * random.random())))
#    listafinal.append(numberg)#
    #with open("lista.csv", "wb") as file:  # Save infos in data.txt
     #   pickle.dump(listafinal, file)

    #n = n + 1
#pass

#print (listafinal)

# TRASH CODE \/