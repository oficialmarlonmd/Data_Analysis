import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

arquivo = "C:\\Users\\Public\\Documents\\data_science\\titanic.csv"

def carregarDados(file):
    dados = pd.read_csv(file, sep=",") # armazena o arquivo na memória

    return dados

dados = carregarDados(arquivo)

def tratarDados(dados):

    print(dados.head()) # apresenta as 5 primeiras linhas

    print(dados.tail()) # apresenta as 5 ultimas linhas

    print(dados.info()) # informações das colnas

    print(dados.describe()) # estatística básica


    dados.drop_duplicates(inplace=True) # remove linhas duplicadas em memoria e salva
    # print(dados.info())

    dados.drop(columns=["PassengerId", "Name", "Cabin", "Ticket"], inplace=True) # remove colunas inútes
    # print(dados.info())

    dados.dropna(inplace=True) # remove informações null
    # print(dados.info())

    # Classe 
    print(dados.head())
    LE = LabelEncoder()
    dados['Sex'] = LE.fit_transform(dados['Sex']) # transforma sex em tipo numerico
    dados['Embarked'] = LE.fit_transform(dados['Embarked']) # transformar de strig em número 
    print(dados.head())

    return dados


dados = tratarDados(dados)

def vizualizacaoGrafica(dados):

    plt.plot([1, 2], [3, 4], 'r--')
    plt.show()

vizualizacaoGrafica(dados)

def vizualizacaoGrafica2(dados):
    dadosGroup = dados.groupby('Sex').groups
    print(dadosGroup)
    
    lb = []
    vl = []

    for grp in dadosGroup:
        lb.append(str(grp))
        vl.append(len(dadosGroup[grp]))


    bar_colors = ['red', 'blue']  # Cores válidas para as barras
    plt.bar(lb, vl, color=bar_colors)
    plt.title("Contagem de Passageiros por Sexo")
    plt.xlabel("Sexo (0 = Feminino, 1 = Masculino)")
    plt.ylabel("Contagem")
    plt.show()

vizualizacaoGrafica2(dados)
