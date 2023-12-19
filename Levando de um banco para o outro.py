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
df_bd = pd.DataFrame(registros, columns=['Id',
                                         'created_at',
                                         'updated_at',
                                         'deleted_at',
                                         'Descricao',
                                         'Vencimento',
                                         'Valor',
                                         'Cliente_Id',
                                         'Fornecedor_Id',
                                         'ContaBancaria_Id',
                                         'DataDeCompetencia',
                                         'Fatura_Id',
                                         'Boleto_Id',
                                         'NFCE_Id',
                                         'NFS_Id',
                                         'NumeroReciboPrestador',
                                         'TipoDePagamento_Id',
                                         'FormaDePagamento_Id',
                                         'TipoDoLancamento_Id',
                                         'Colaborador_Id',
                                         'Pago',
                                         'PlanoDeContaItem_Id',
                                         'CentroDeCustoItem_Id',
                                         'Lancamento_Id',
                                         'Recibo',
                                         'Nota',
                                         'CupomFiscal',
                                         'ModalidadeDoLancamento_Id',
                                         'IntervaloDeRecorrencia',
                                         'RecorrenciaEncerrada',
                                         'Observacoes',
                                         'ContaDeOrigem_Id',
                                         'ContaDeDestino_Id',
                                         'Franquia_Id',
                                         'OrdemDePagamento_Id',
                                         'NotaFiscalDeServico',
                                         'FaturaDeLocacao',
                                         'CodigoReferencia',
                                         'MotivoApagado',
                                         'SplitPai_Id',
                                         'NaoCobrarTaxas'])


""" for i, row in df_bd.iterrows():
    # Mapear "NaT" para NULL para campos de data/hora
    for col in ['created_at', 'updated_at', 'deleted_at', 'Vencimento']:
        if pd.isna(row[col]):
            row[col] = 'NULL' """


""" # Imprimindo o DataFrame
print(df_bd.head())


# Iterando pelas linhas do DataFrame
for i, row in df_bd.iterrows():
    # Iterando pelas colunas do DataFrame
    for column in df_bd.columns:
        print(f"{column}: {row[column]}")
    # Adicionando uma linha em branco entre cada registro
    print()
  """





# COnectar com o meu financeiro e inserir valores

# Conectando com o banco de dados destino
def conectar_banco_destino():
    conexao_destino = psycopg2.connect(database='meufinanceiro',
                                        host='localhost',
                                        user="postgres",
                                        password="postgrespassword",
                                        port="5401")  
    print(conexao_destino.info)
    print(conexao_destino.status)
    return conexao_destino


def consultar_db_destino(sql):
    con = conectar_banco_destino()
    cur = con.cursor()
    cur.execute(sql)
    recset = cur.fetchall()
    con.close()
    return recset 


# Função para inserir dados no banco de destino
def inserir_db_destino(sql):
    con_destino = conectar_banco_destino()
    cur_destino = con_destino.cursor()
    try: 
        cur_destino.execute(sql)
        con_destino.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con_destino.rollback()
        cur_destino.close()
        return 1
    cur_destino.close()


# Iterando pelas linhas do DataFrame
for i, row in df_bd.iterrows():
    print(row)
    # Montando a instrução SQL de inserção (adapte de acordo com sua tabela de destino)
    sql_insercao = f"""
    INSERT INTO meufinanceiro.public.lancamentos ("Id",
    "created_at",
    "updated_at",
    "Descricao",
    "Vencimento",
    "Valor",
    "Cliente_Id",
    "Fornecedor_Id",
    "ContaBancaria_Id",
    "DataDeCompetencia",
    "Fatura_Id",
    "Boleto_Id",
    "NFCE_Id",
    "NFS_Id",
    "NumeroReciboPrestador",
    "TipoDePagamento_Id",
    "FormaDePagamento_Id",
    "TipoDoLancamento_Id",
    "Colaborador_Id",
    "Pago",
    "PlanoDeContaItem_Id",
    "CentroDeCustoItem_Id",
    "Lancamento_Id",
    "Recibo",
    "Nota",
    "CupomFiscal",
    "ModalidadeDoLancamento_Id",
    "IntervaloDeRecorrencia",
    "RecorrenciaEncerrada",
    "Observacoes",
    "ContaDeOrigem_Id",
    "ContaDeDestino_Id",
    "Franquia_Id",
    "OrdemDePagamento_Id",
    "NotaFiscalDeServico",
    "FaturaDeLocacao",
    "CodigoReferencia",
    "MotivoApagado",
    "SplitPai_Id",
    "NaoCobrarTaxas")
    VALUES (
    '{row['Id']}', 
    '{row['created_at']}', 
    '{row['updated_at']}', 
    '{row['Descricao']}', 
    '{row['Vencimento']}', 
    '{row['Valor']}', 
    '{row['Cliente_Id']}', 
    '{row['Fornecedor_Id']}', 
    '{row['ContaBancaria_Id']}', 
    '{row['DataDeCompetencia']}', 
    '{row['Fatura_Id']}', 
    '{row['Boleto_Id']}', 
    '{row['NFCE_Id']}', 
    '{row['NFS_Id']}', 
    '{row['NumeroReciboPrestador']}', 
    '{row['TipoDePagamento_Id']}', 
    '{row['FormaDePagamento_Id']}', 
    '{row['TipoDoLancamento_Id']}', 
    '{row['Colaborador_Id']}', 
    '{row['Pago']}', 
    '{row['PlanoDeContaItem_Id']}', 
    '{row['CentroDeCustoItem_Id']}', 
    '{row['Lancamento_Id']}', 
    '{row['Recibo']}', 
    '{row['Nota']}', 
    '{row['CupomFiscal']}', 
    '{row['ModalidadeDoLancamento_Id']}', 
    '{row['IntervaloDeRecorrencia']}', 
    '{row['RecorrenciaEncerrada']}', 
    '{row['Observacoes']}', 
    '{row['ContaDeOrigem_Id']}', 
    '{row['ContaDeDestino_Id']}', 
    '{row['Franquia_Id']}', 
    '{row['OrdemDePagamento_Id']}', 
    '{row['NotaFiscalDeServico']}', 
    '{row['FaturaDeLocacao']}', 
    '{row['CodigoReferencia']}', 
    '{row['MotivoApagado']}', 
    '{row['SplitPai_Id']}', 
    '{row['NaoCobrarTaxas']}'
    );
    """
    
    # Inserindo o registro no banco de destino
    try:
        inserir_db_destino(sql_insercao)
    except:
        print(row)

print("Inserção concluída!")


""" # Realizando a consulta no PostgreSQL
sql = 'Select * from MeuFinanceiro.public.lancamentos'
registros = consultar_db_destino(sql)

 # Transformando os dados da consulta em um DataFrame
df_bd = pd.DataFrame(registros, columns=['Id','Descricao','Valor','Cliente_Id','Fornecedor_Id','ContaBancaria_Id','DataDeCompetencia','Fatura_Id','Boleto_Id','NFCE_Id','NFS_Id','NumeroReciboPrestador','TipoDePagamento_Id','TipoDoLancamento_Id','FormaDePagamento_Id','Colaborador_Id','Pago','PlanoDeContaItem_Id','CentroDeCustoItem_Id','Lancamento_Id','Recibo','Nota','CupomFiscal','ModalidadeDoLancamento_Id','IntervaloDeRecorrencia','RecorrenciaEncerrada','Observacoes','ContaDeOrigem_Id','ContaDeDestino_Id','Franquia_Id','OrdemDePagamento_Id','NotaFiscalDeServico','FaturaDeLocacao','CodigoReferencia','MotivoApagado','SplitPai_Id','NaoCobrarTaxas','created_at','deleted_at','updated_at','Vencimento'])

# Imprimindo o DataFrame
print(df_bd.head())

# ALTERAR DF_DB
# Iterando pelas linhas do DataFrame
for i, row in df_bd.iterrows():
    # Iterando pelas colunas do DataFrame
    for column in df_bd.columns:
        print(f"{column}: {row[column]}")
    # Adicionando uma linha em branco entre cada registro
    print()
 """
