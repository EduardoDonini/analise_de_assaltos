import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, mainloop


dados = pd.read_csv("Dados Sobre Crimes Em Allegany/MD_Crime_Data.csv", sep=";")

assaltos = dados["ASSALTOS"].to_list()
ano = dados["YEAR"].to_list()
assasinatos = dados["MURDER"].to_list()

n_assaltos = assaltos
ano_indice = ano
n_assasinatos = assasinatos

serie = pd.Series(n_assaltos,ano_indice)

print(serie)

def grafico_linhas():
    plt.title("NUMERO DE ASSALTOS EM ALLEGANY COUNTY AO LONGO DOS ANOS")
    plt.xlabel("ANOS")
    plt.ylabel("NUMERO DE ASSALTOS")
    plt.plot(ano_indice,n_assaltos, marker = "o", linestyle = "--")
    plt.xticks(range(min(ano), max(ano)+1, 5))
    plt.grid(True)
    plt.show()

def grafico_barras():
    plt.title("NUMERO DE ASSASINATOS EM ALLEGANY COUNTY AO LONGO DOS ANOS")
    plt.xlabel("ANOS")
    plt.ylabel("NUMERO DE ASSALTOS")
    plt.bar(ano_indice,n_assasinatos)
    plt.xticks(range(min(ano), max(ano)+1, 5))
    plt.grid(True)
    plt.show()

janela = Tk()
janela.title("ANALISE DE CRIMES EM ALLEGANY")

Button(janela, text="Analisar Assaltos", command=grafico_linhas).pack()
Button(janela, text="Analisar Assasinatos", command=grafico_barras).pack()

mainloop()
