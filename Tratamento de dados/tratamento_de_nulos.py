import pandas as pd

# Leia a planilha
dataset_co2_FPAIS = pd.read_excel('co2_emissions_global_countries.xlsx')
dataset_co2_FCONTINENTE = pd.read_excel('co2_emissions_global_continents.xlsx')

# Substitua células vazias por "DESCONHECIDO"
dataset_co2_FPAIS = dataset_co2_FPAIS.fillna('DESCONHECIDO')
dataset_co2_FCONTINENTE = dataset_co2_FCONTINENTE.fillna('DESCONHECIDO')

# Liste as colunas que você quer modificar
colunas_para_modificar = [
    'pib', 'emissao_co2', 'emissao_co2_per_capita', 'emissao_co2_per_pib', 'emissao_co2_ (cumulativo)',
    'emissao_de_co2_do_carvao', 'emissao_de_co2_do_carvao_per_capita', 'emissao_de_co2_do_carvao(cumulativo)',
    'emissao_de_co2_do_cimento', 'emissao_de_co2_de_queimas', 'emissao_de_co2_de_queimas_per_capita',
    'emissao_de_co2_de_queimas(cumulativo)', 'emissao_de_co2_do_gas', 'emissao_de_co2_do_gas_per_capita',
    'emissao_de_co2_do_gas(cumulativo)', 'emissao_de_co2_da_LUC', 'emissao_de_co2_da_LUC_per_capita',
    'emissao_de_co2_da_LUC(cumulativo)', 'emissao_de_co2_do_oleo', 'emissao_de_co2_do_oleo_per_capita',
    'emissao_de_co2_do_oleo(cumulativo)', 'emissao_de_GHG_per_capita', 'emissao_de_GHG', 'metano',
    'metano_per_capita', 'oxido_nitroso', 'oxido_nitroso_per_capita', 'emissao_de_co2_do_cimento_per_capita',
    'emissao_de_co2_do_cimento(cumulativo)', 'proporcao_global_do_co2', 'proporcao_global_da_emissao_de_co2_do_cimento', 'proporcao_global_da_emissao_de_co2_do_carvao',	'proporcao_global_da_emissao_de_co2_de_queimas',	'proporcao_global_da_emissao_de_co2_do_gas',	'proporcao_global_da_emissao_de_co2_da_LUC',	'proporcao_global_da_emissao_de_co2_do_oleo', 'proporcao_global_da_emissao_de_co2_do_cimento(cumulativo)',	'proporcao_global_do_co2_ (cumulativo)', 'proporcao_global_da_emissao_de_co2_do_carvao(cumulativo)', 'proporcao_global_da_emissao_de_co2_de_queimas(cumulativo)', 'proporcao_global_da_emissao_de_co2_da_LUC(cumulativo)', 'proporcao_global_da_emissao_de_co2_do_gas(cumulativo)', 'proporcao_global_da_emissao_de_co2_do_oleo(cumulativo)'
]

# Substitua o valor 0 por "DESCONHECIDO" nas colunas especificadas
for coluna in colunas_para_modificar:
    if coluna in dataset_co2_FPAIS.columns:
        dataset_co2_FPAIS[coluna] = dataset_co2_FPAIS[coluna].replace(0, 'DESCONHECIDO')
    if coluna in dataset_co2_FCONTINENTE:
        dataset_co2_FCONTINENTE[coluna] = dataset_co2_FCONTINENTE[coluna].replace(0, 'DESCONHECIDO')
