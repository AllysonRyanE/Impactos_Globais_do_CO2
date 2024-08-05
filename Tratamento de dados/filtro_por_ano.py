import pandas as pd
from infos_iniciais import dataset_co2

#Restarão apenas valores maiores que 1950
dataset_co2_FANO = dataset_co2[dataset_co2['ano'] >= 1950]
