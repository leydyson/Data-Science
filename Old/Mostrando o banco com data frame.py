import requests
import json
import pandas as pd
import psycopg2

# Função para conectar ao banco de dados de origem
def conectar_banco_origem():
    conexao_origem = psycopg2.connect(database='financeiro',
                                       host='localhost',
                                       user="postgres",
                                       password="senha",
                                       port="5401")  
    print(conexao_origem.info)
    print(conexao_origem.status)
    return conexao_origem


def consultar_db(sql):
    con = conectar_banco_origem()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    con.close()
    return recset 

def inserir_db(sql):
    con = conectar_banco_origem()
    cur = con.cursor()
    try: 
        cur.execute(sql)
        con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()

# Realizando a consulta no PostgreSQL
sql = 'Select * from lancamentos."Lancamentos"'
registros = consultar_db(sql)

 # Transformando os dados da consulta em um DataFrame
df_bd = pd.DataFrame(registros, columns=['Id','Descricao','Valor','Cliente_Id','Fornecedor_Id','ContaBancaria_Id','DataDeCompetencia','Fatura_Id','Boleto_Id','NFCE_Id','NFS_Id','NumeroReciboPrestador','TipoDePagamento_Id','TipoDoLancamento_Id','FormaDePagamento_Id','Colaborador_Id','Pago','PlanoDeContaItem_Id','CentroDeCustoItem_Id','Lancamento_Id','Recibo','Nota','CupomFiscal','ModalidadeDoLancamento_Id','IntervaloDeRecorrencia','RecorrenciaEncerrada','Observacoes','ContaDeOrigem_Id','ContaDeDestino_Id','Franquia_Id','OrdemDePagamento_Id','NotaFiscalDeServico','FaturaDeLocacao','CodigoReferencia','MotivoApagado','SplitPai_Id','NaoCobrarTaxas','created_at','deleted_at','updated_at','Vencimento'])

# Imprimindo o DataFrame
print(df_bd.head())


# Iterando pelas linhas do DataFrame
for i, row in df_bd.iterrows():
    # Iterando pelas colunas do DataFrame
    for column in df_bd.columns:
        inserir_db(insert(f"{column}: {row[column]}")
    # Adicionando uma linha em branco entre cada registro
    print()

# COnectar com o meu financeiro e inserir valores