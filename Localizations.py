import numpy as np
import pandas as pd
import psycopg2 
import matplotlib.pyplot as plt

conexao = "dbname='iot' user='postgres' host='localhost' password='postgrespassword' port=5401"
consulta = 'SELECT * FROM iot."Localizacoes"'

try:
    conexao = psycopg2.connect(conexao)
    print("Conectado com sucesso ao banco de dados!")

    # Criando um cursor para executar a consulta
    cursor = conexao.cursor()

    # Executando a consulta
    cursor.execute(consulta)

    # Pegando todos os resultados da consulta
    colunas = [desc[0] for desc in cursor.description]
    resultado = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

    # Transformando o resultado em um DataFrame
    df = pd.DataFrame(resultado)

    # Imprimindo o DataFrame
    #print(df)

    print(df.info())

    print(df.columns)

    print(df.deleted_at.isnull().sum())

    print(df.head(10))

    print(df.tail(10))

    print(df.describe())

    print(df.deleted_at.isnull()==False)

    print(df.T)

    print(df.shape)

    #print(df[["Id","Imei"]])

# Limpar os dados removendo valores ausentes ou duplicados.
    print(df.duplicated())

    print(df.isna())

# Realizar operações de filtragem e seleção dos dados usando condições lógicas ou operadores matemáticos.
    print(df.select_dtypes("float")) 

    print(df['Ignicao']==True)

    print(df['Ignicao']==True)

except Exception as erro:
    print("Erro ao se conectar com o banco de dados: ", erro)


# Criar novas colunas com base em cálculos ou funções usando operações aritméticas ou funções lambda.
# Realizar operações agregatórias nos dados usando métodos como sum, mean, count etc.
# Realizar operações junta nos dados usando métodos como merge ou join.
# Visualizar os dados usando gráficos ou tabelas usando bibliotecas como matplotlib ou seaborn