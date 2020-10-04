# TELE AULA 03

# PYTHON ORIENTADO A OBJETOS

# CLASSES E METODOS EM PYTHON
# CLASSE É GENERALISTA
# EXEMPLO: AUTOMOVEIS
# OBJETO É ESPECIFICO
# EXEMPLO: GOL, BRANCO, G5, 2010, 1.0

# NA DECLARAÇÃO DO METODO DA CLASSE O PRIMEIRO ATRIBUTO DEVE SER O SELF
# O SELF INDICA QUE ELE VAI TER COMO REFERÊNCIA AS VARIÁVEIS DA CLASSE
# PARA MANIPULAR AS VARIÁVEIS DA CLASSE, EU PRECISO DO PARAMENTRO SELF COMO PRIMEIRO ARGUMENTO

# TODA VEZ QUE SE CRIA UM OBJETO DEVEMOS SETAR OS VALORES DOS ATRIBUTOS
# MESMO QUE DEPOIS ESSES VALORES SEJAM MODIFICADOS PELOS METODOS
# AS VARIÁVEIS DEVEM SER INICIALIZADAS
# PARA ISSO EXISTE O CONSTRUTOR, ELE SERVE PARA INICIAR OS ATRIBUTOS


class Pessoas:
    def __init__(self, nome, telefone):
        self.nome = nome

        self.telefone = telefone


# O CONSTRUTUOR É UM METODO RESERVADO CHAMADO __INIT__
# O PARAMETRO SELF É OBRIGATORIO E OS DEMAIS SÃO DEFINIDOS PELO PROGRAMADOR


class Queue:
    def __init__(self):
        self.q = []


# CLASSE CRIANDO UMA LISTA
# SELF.Q ESTÁ FAZENDO A CRIAÇÃO DA LISTA


def isEmpety(self):
    return (len(self.q) == 0)


# VERIFICANDO SE A LISTA ESTÁ VAZIA


def enqueue(self, item):
    return self.q.append(item)


# ADICIONANDO UM ITEM A FILA


def denqueue(self):
    return self.q.pop(0)


# REMOVENDO UM ITEM DA FILA


# SOLUÇÃO PROBLEMA 01
# PRÁTICA DE CONSTRUTOR, METODO E OBJETOS

# CONSTRUTOR
class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.numero = numero
        self.saldo = 0

    # METODO SALDO
    def Saldo(self):
        return self.saldo

    # METODO CLIENTE
    def get_cliente(self):
        return self.cliente

    # METODO DEPOSITO
    def Depositar(self, valor):
        self.saldo += valor

    # METODO TRANSFERÊNCIA
    # ADICIONADO NA SP_02
    def Transferencia(self, conta_entrada, valor):
        self.saldo = self.saldo - valor
        conta_entrada.saldo = conta_entrada.saldo + valor


# OBJETOS
conta_01 = Conta('João', 1)
conta_01.Depositar(100.00)
print(f'O dono da Conta 01 é {conta_01.get_cliente()}, com saldo de R$: {conta_01.Saldo()}')

conta_02 = Conta('Maria', 2)
conta_02.Depositar(50.00)
print(f'O dono da Conta 02 é {conta_02.get_cliente()}, com saldo de R$: {conta_02.Saldo()}')

conta_03 = Conta('Oliver', 3)
conta_03.Depositar(5.00)
print(f'O dono da Conta 03 é {conta_03.get_cliente()}, com saldo de R$: {conta_03.Saldo()}')

# BIBLIOTECAS E MÓDULOS EM PYTHON
# PRINCIPAIS BIBLIOTECAS
# MATH              -> FUNÇÕES MATEMÁTICAS
# PILLOW            -> IMAGENS
# MATPLOTLIB        -> GRÁFICOS E PLOTAGENS
# NUMPY             -> PROCESSAMENTO DE MATRIZES
# PANDA             -> ANÁLISE DE DADOS

# SOLUÇÃO PROBLEMA 02
# ADICIONANDO A TRANSFERÊNCIA E DIVIDIR EM MODULOS

# A PROFESSSORA FEZ A DIVISÃO EM MODULOS
# MAS, PARA FACILIDADE DE ESTUDOS, MANTEREI TODOS NO MESMO ARQUIVO
# import classe

conta_04 = Conta('Marcio', 4)
conta_04.Depositar(200.00)
print(f'O dono da Conta 04 é {conta_04.get_cliente()}, com saldo de R$: {conta_04.Saldo()}')

conta_05 = Conta('Ana', 5)
conta_05.Depositar(200.00)
print(f'O dono da Conta 05 é {conta_05.get_cliente()}, com saldo de R$: {conta_05.Saldo()}')

conta_04.Transferencia(conta_05, 150.00)
print('Foi feita uma transfêrencia da Conta 04 para Conta 05!')
print(f'O novo saldo da Conta 04 é R$ {conta_04.Saldo()} e o novo saldo da Conta 05 é R$: {conta_05.Saldo()}')

# APLICAÇÃO DE BANCO DE DADOS COM PYTHON

# import sqlite3

# conector = sqlite3.connect('teste_02.db')
# cursor = conector.cursor()
# sql = """
#    create table teste_02 (codigo integer, nome text, idade integer)
#    """
# cursor.execute(sql)

# sql = """
#    insert into teste_02 (codigo, nome, idade)
#    values
#    (1284, 'Pedro Oliveira', 32)
#    """
# cursor.execute(sql)
# conector.commit()
# cursor.close()
# conector.close()


# CONCEITOS SQL
# CRUD
# C     -> CREATE (CRIAÇÃO)
# R     -> READ (CONSULTA)
# U     -> UPDATE (ATUALIZAÇÃO)
# D     -> DELETE (DELETAR)

# READ (CONSULTA)
# def Read():
#    sql = 'select * from cadastro'
#    cursor.execute(sql)
#    dados = cursor.fetchall()
#    cursor.close()
#    conector.close()
#    for d in dados:
#        print(d[0], d[1], d[2])


# UPDATE (ATUALIZAÇÃO)
# def Update(Cod, new):
#    cursor.execute("""
#    UPDATE cadastro
#    SET idade = ?
#    where codigo = ?
#    """, (new, Cod))
#   conector.commit()

# DELETE (DELETAR)
# def Excluir_Cliente(Cod):
#    sql = 'delete form cadastro where codigo = :param'
#    cursor.execute(sql, {'param': Cod})
#    conector.commit()
#    return f'Cliente {Cod} excluído'

# RESOLUÇÃO DA SITUAÇÃO PROBLEMA
# A PROFESSORA CRIA UM NOVO ARQUIVO
# MAS PARA FIM DE ESTUDOS, VOU DEIXAR TODOS NO MESMO ARQUIVO

#import sqlite3

#conector = sqlite3.connect('teste_02.db')
#cursor = conector.cursor()

#sql = 'select * from teste_02'
#cursor.execute(sql)
#dados = cursor.fetchall()

#cursor.close()
#conector.close()

#for d in dados:
#    print(d[0], d[1], d[2])

#print(f'Encontrados {len(dados)} registros!')

# SITUAÇÃO PROBLEMA 04
# EXCLUINDO UM DADO

#import sqlite3

#def Excluir_Clientes(Codigo):
#    sql = 'delete from teste_02 where codigo = :parametro'
#    cursor.execute(sql, {'parametro': Codigo})
#    cursor.commit()


#conector = sqlite3.connect('teste_02.db')
#cursor = conector.cursor()
