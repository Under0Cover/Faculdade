# TELE AULA 04

# PARTE 01 DA TELE AULA
# ANÁLISE DE DADOS
# BIBLIOTECA PANDAS

# DADOS
# OS DADOS SÃO PRODUZIDOS POR ALGUM TIPO DE DISPOSITIVO
# E A TODOS OS MOMENTOS POR TODOS OS USUÁRIOS DA INTERNET

# BIG DATA
# GRANDE VOLUME DE DADOS COM DIVERSOS TIPOS E GERADOS EM ALTA VELOCIDADE
# METODOLOGIA PARA CAPTURA, ARMAZENAMENTO E PROCESSAMENTO DE INFORMAÇÕES
# MATÉRIA PRIMA PARA CIÊNCIA DE DADOS

# CICLO DE VIDA DOS DADOS
# PRODUÇÃO
# ARMAZENAMENTO
# TRANSFORMAÇÃO         -> PYTHON ENTRA NESSA PARTE
# ANÁLISE
# DESCARTE

# UTILIZAÇÃO DOS DADOS
# DIRECIONAMENTO DE PROPAGANDAS
# SISTEMAS ESPECIALISTAS
# PREVISÃO DE VENDAS
# IoT                   -> INTERNET DAS COISAS

# PANDAS
# BIBLIOTECA PARA MANIPULAÇÃO E ANÁLISE DE DADOS
# INTEGRAÇÃO COM DIVERSOS TIPOS DE ARQUIVOS
# PLOTAGEM DOS DADOS UTILIZANDO MATPLOTLIB
# ESTATÍSTICAS BÁSICAS SÃO FACILMENTE CALCULADAS

# IMPORTAÇÕES
import pandas
import numpy
import sqlite3

# DATAFRAME
# ESTRUTURA DE DADOS BIDIMENSIONAL COM COLUNAS DE TIPOS DIFERENTES (E LINHAS)
# SEMELHANTES A UMA PANILHA DO EXCEL
# TIPOS POSSÍVEIS: DICIONÁRIOS, LISTAS, ARRAYS, SÉRIE, OUTRO DATAFRAME

# DATAFRAME

dataframe = pandas.DataFrame({
    'Nome': ['João da Silva',
             'Carlos Souza',
             'Maria Ferreira'],
    'Idade': [22, 35, 58],
    'Sexo': ['Masculino', 'Masculino', 'Feminino']}
)

print(dataframe)
print('-' * 40)
# DATAFRAME TAMBÉM PODEM SER CLASSIFICADOS COMO UM CONJUNTO DE SERIES

# SERIES
# ESTRUTURA DE DADOS UNIDIMENSIONAL CAPAZ DE CONTER QUALQUER TIPO DE DADOS

# series = pandas.Series(data, index=index)
# DECLARAÇÃO PADRÃO

series = pandas.Series(numpy.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(series)
print('-' * 40)

# CRIANDO DATAFRAMES
cliente = {'Nome': ['Marcelo', 'Ana', 'Maria'],
           'Idade': [33, 26, 56]}

dataframe = pandas.DataFrame(cliente)
print(dataframe)
print('-' * 40)

# UTILIZANDO NO VETOR
vetor = numpy.array([5, 6, 7, 8])
v = pandas.Series(vetor)
print(v)
print('-' * 40)

# SITUAÇÃO PROBLEMA 01
# CADASTRO CLIENTES
cliente = {'Nome':['Manoel', 'Joaquim', 'Benedita', 'Conceição'],
           'Idade': [45, 48, 52, 56],
           'Telefone': [99841234, 99855678, 99868901, 99872345]}
dataframe_cliente = pandas.DataFrame(cliente)
print(dataframe_cliente)
print('-' * 40)
print(dataframe_cliente.Nome)
print('-' * 40)
print(dataframe_cliente.Idade   .mean())
print('-' * 40)

# FAÇA UMA ESTRUTURA DE DADOS QUE RELACIONE
# OS VENDEDORES JUNTAMENTE COM SEU NÚMERO DO SISTEMA

serie = pandas.Series(('Carla', 'Alice', 'Fernanda'), index=['03', '07', '09'])
print(serie)
print('-' * 40)

# PARTE 02 DA TELE AULA
# INTRODUÇÃO E MANIPULAÇÃO DOS DADOS
# CSV
# EXEMPLO:
# variavel = pandas.read_csv('Arquivo.csv', encoding = 'UTF-8', sep = ',')
# CABEÇALHO É OPCIONAL
# NÚMEROS DECIMAIS DEVEM SER SEPARADOS POR PONTO
# SEPARADOS PODE SER VÍRGULA OU PONTO E VÍRGULA

# OUTRO CASO QUE PODE SER MANIPULADO É JSON
# JSON ARMAZENA INFORMAÇÕES ESTRUTURADAS
# É UTILIZADO PARA TRANSFERIR DADOS ENTRE SERVIDOR E CLIENTE
# É COMPOSTO POR CHAVE E VALOR
# EXEMPLO:
# variavel = pandas.read_json('Arquivo.json')


# ALGUMAS FUNCIONALIDADES DO PANDAS NO BANCO DE DADOS
# variavel = pandas.read_sql_query()
# variavel = pandas.read_sql_table()
# dataframe.to_sql()

# EXEMPLO:
# conector = sqlite3.connect('conta.db')
# ler_data_frame = pandas.read_sql_query('Select * from cadastro', conector)
# print(ler_data_frame.head())

# SITUAÇÃO PROBLEMA 02
# A PROFESSORA NÃO AJUDOU A DESENVOLVER A QUESTÃO
# JÁ TINHA FEITO METADE DO EXERCÍCIO
# NA METADE QUE ELA IRIA AJUDAR A DESENVOLVER O PYTHON DEU ERRO
# ELA PEGOU OS COMANDOS PRONTOS EM OUTRA ABA
# RODOU ELES
# FUNCIONOU
# E É ISSO

# VISUALIZAÇÃO DE DADOS EM PYTHON
# MATPLOTLIB
# SEABORN-COUNT PLOT
# SCATTER PLOT