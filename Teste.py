import numpy as np
import pandas as pd
import psycopg2 
import matplotlib.pyplot as plt

conexao = "dbname='financeiro' user='postgres' host='localhost' password='postgrespassword' port=5401"
consulta = 'SELECT * FROM lancamentos."Lancamentos"'

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
    # print(df)

    #print(df.deleted_at.isnull()==False)

    #print(df.columns.values) e print(df.columns, primeiro método retorna um array de valores dos nomes das colunas do dataframe, enquanto o segundo método retorna uma lista de nomes das colunas do dataframe

    #print(df.describe())

    #print(df.T)

    #print(df[["Vencimento","Valor"]])

    #print(df.iloc[1000])

    # print(df['CentroDeCustoItem_Id'].value_counts())
    # print(df['CentroDeCustoItem_Id'].value_counts().plot(kind='bar'))
    # plt.show()
    # np.random.seed(123456)
    # ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    # ts = ts.cumsum()
    # ts.plot()
    # plt.show()

    print(df.groupby(['Franquia_Id']).mean().plot(kind='bar'))
    # plt.show()


except Exception as erro:
    print("Erro ao se conectar com o banco de dados: ", erro)

#ksdjksdjksjd