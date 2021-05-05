import numpy as np
import  pandas as pd
import matplotlib as plt
import xlrd
import openpyxl


#zad1
# lista = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(lista, header=0)
# dzieci = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(dzieci)
# dzieci.plot()
# plt.xticks(np.arange(2000, 2018, step=1))
# plt.xticks(rotation=90)
# plt.show()

#zad2
# dzieci = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(dzieci)
# dzieci.plot.bar()
# plt.show()


#zad4
# dane = pd.read_csv("zamowienia.csv",sep=';')
#print(dane[['Sprzedawca','Utarg']])
# suma =  dane.groupby('Sprzedawca').agg({'Utarg':['sum']})
# suma.plot.bar()
# plt.xticks(rotation=0)
# plt.show()





