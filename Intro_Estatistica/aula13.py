import pandas as pd
import numpy as np
#import scipy
import statistics

# lendo dataframe de uma URL
url = 'https://raw.githubusercontent.com/advinstai/python-datascience/master/csv/College.csv'
df1 = pd.read_table(url,sep=",")  

# descubra as colunas qualitativas e quantitativas 
print("+" + "-"*53 +"+" )
print("| 1. Descubra as colunas QUALITATIVAS e QUANTITATIVAS |")
print("+" + "-"*53 +"+" )
print("Colunas qualitativas:",[i for i in df1.columns[:2]])
print("Colunas quantitativas:",[i for i in df1.columns[2:]])


# Descreva os intervalos das colunas quantitativas 
print("\n+" + "-"*53 +"+" )
print("| 2. Descreva os INTERVALOS das colunas quantitativas |")
print("+" + "-"*53 +"+" )
dic = {'Max':df1.max()[2:], 'Min': df1.min()[2:], 'Intervalos': df1.max()[2:]-df1.min()[2:]}
df2 = pd.DataFrame(dic)
print(df2)
print("-"*36)

# calcule a media, mediana e moda de cada coluna quantitativa 
print("\n+" + "-"*64 +"+" )
print("| 3. Calcule a MEDIA, MEDIANA e MODA de cada coluna quantitativa |")
print("+" + "-"*64 +"+" )

dic['Media'] = round(df1.mean(),2)              # calculando media usando funcao pandas
dic['Mediana'] = round(df1.median(),2)          # calculando mediana usando funcao pandas

# Como a MODA pode ser composta de mais de 1 elemento, cria-se uma lista
#   para receber esses elementos, inclui-se essa lista no mesmo dicionario
#   com a MEDIA e MEDIANA, depois transforma-se o dicionario em dataframe.
lista = []              # inicializando lista vazia
[lista.append(list(df1[i].mode())) for i in list(df1.columns[2:])]      # adicionando 'a lista a moda de cada coluna
dic['Moda'] = lista     # adicionando a lista no dicionario que possui media e mediana
df3 = pd.DataFrame(dic)         # transformando o dicionario em dataframe
print(df3)              # imprimpindo tudo
print("-"*105)


