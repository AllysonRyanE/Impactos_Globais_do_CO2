import pandas as pd #Importar a biblioteca pandas
dataset_co2 = pd.read_excel('CO2 Emissions Global Data.xlsx') #Ler o arquivo informando o caminho
linhas, colunas = dataset_co2.shape #Função que retorna tupla com linhas e colunas
print(linhas, colunas)
dataset_co2.info() #(Identifica o tipo do atributo e o preenchimento)
dataset_co2.describe() #(Informa algumas estatisticas)
dataset_co2.nunique() #Valores que repetem-se
dataset_co2.isnull().sum() #Células vazias
dataset_co2.co2.plot.box() #Plotagem de boxplot de coluna 'co2'
dataset_co2.co2.plot.hist(bins=20) #Plotagem de histograma de coluna 'co2'
