# TELE AULA 02

# RELEMBRANDO AS DEFINIÇÕES BÁSICAS DA TELE AULA 01
# ESTRUTURA IF-ELIF-ELSE
# VARIAVEIS

# EXEMPLOS PRÁTICOS DA TELE AULA 02 - LINGUAGEM DE PROGRAMAÇÃO PYTHON
# TRABALHAREMOS COM LISTAS, TUPLAS E DICIONÁRIOS EM PYTHON

# LISTAS EM PYTHON:
# SÃO ESTRUTURAS SEQUENCIAIS COMPOSTAS POR ELEMENTOS ORGANIZADOS DE MODO LINAER
# AS LISTAS SÃO MUTÁVEIS
# OS ELEMENTOS PODEM SER ACESSADOS A PARTIR DE UM ÍNDICE
# AS LISTAS PODEM SER DE VÁRIOS TIPOS DE DADOS DIFERENTES
# O TAMANHO DA LISTA VAI DE 0 ATÉ N-1
# PODEMOS CRIAR LISTAS DENTRO DE LISTAS
# COMANDOS DAS LISTAS
# APPEND()              -> ADICIONA UM ELEMENTO NO FINAL DA LISTA
# INSERT(X, Y)          -> ADICIONA O ELEMENTO Y NA POSICAO X
# REMOVE(Y)             -> REMOVE Y DA LISTA
# SORT()                -> ORDENA POR VALOR
# EXTEND(LISTA)         -> CONCATENAR COM OUTRA LISTA
# INDEX(ELEMENTO)       -> DESCOBRIR A POSIÇÃO DE UM ELEMENTO
# CLEAR()               -> APAGAR TODOS OS ELEMENTOS DA LISTA

# FATIAMENTO DE LISTAS
l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
print(l[0:3])
# RETORNO SERÁ DOS ELEMENTOS 0 ATÉ 2
print(l[4:10])
# RETORNO SERÁ DOS ELEMENTOS 4 ATÉ 9
print(l[:5])
# RETORNO SERÁ DOS ELEMENTOS INICIAIS ATÉ 4
print(l[0:8:3])
# RETORNO SERÁ DOS ELEMENTOS 0 ATÉ 7 DE 3 EM 3

# LIST COMPREHENSION
# UMA CONSTRUÇÃO SINTÁTICA PARA CRIAÇÃO DE UMA LISTA BASEADA EM LISTAS EXISTENTES
# [EXPRESSAO FOR ITEM IN LISTA IF CONDICAO
s = [x*2 for x in range(0, 10) if x % 2 == 0]
print(s)

# TUPLAS EM PYTHON
# SEMELHANTE AS LISTAS, POREM IMUTAVEL
# SAO CAPAZES DE CONTER QUALQUER OUTRO TIPO DEFINIDO EM PYTHON
# ACESSO AOS ELEMENTOS SE DÁ POR ÍNDICES
# SÃO DECLARADAS ENTRE PARENTESES
# ACEITAM OS OPERADORES DE CONCATENAÇÃO '+' E MULTIPLICATIVO '*'
# APLICAM-SE A ELAS AS OPERACOES DE FATIAMENTO

# DICIONARIOS EM PYTHON
# DICIONARIOS TAMBEM SAO CONHECIDOS COMO MAPAS
# UMA COLECAO DE ELEMENTOS, NO QUAL TEMOS N ENTRADAS
# ASSOCIADAS A UMA OU MAIS CHAVES POR ENTRADA

# CRIACAO DE MATRIZES COM NUMPY
# NUMPY E UM PACOTE DE EXTENSAO DO PYTHON PARA MATRIZES MULTI-DIMENSIONAIS


import numpy as np
x = np.array([0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1])


# SOLUCAO PROBLEMA 01
# CALCULAR UMA MEDIA USANDO UMA LISTA

def ValorLista():
    for indice in range(1, 5):
        notas.append(float(input(f'Digite a nota do seu {indice}º Bimestre: ')))

def Media():
    soma = 0
    for indice in range(len(notas)):
        soma += notas[1]
    media = soma / len(notas)
    return media

notas = []
ValorLista()
media = Media()
print(media)

# CONCEITOS: ALGORITMOS DE BUSCA

# TIPOS DIFERENTES DE BUSCA

# BUSCA SEQUENCIAL
# É O ALGORITMO MAIS SIMPLES DE BUSCA:
# PERCORRE TODA A COLECAO COMPARANDO A CHAVE COM O VALOR DO ELEMENTO EM CADA POSICAO
# NO CASO, SE A CHAVE FOR IGUAL A ALGUM VALOR, RETORNA A POSICAO CORRESPONDENTE NA COLECAO
# CASO NÃO EXISTA A CHAVE NA ESTRUTURA PERCORRIDA, O RETORNO SERÁ -1

# BUSCA BINÁRIA
# EFICIENTE PARA UMA ESTRUTURA DE DADOS ORDENADA
# O ELEMENTO É COMPARADO COM O ELEMENTO DO MEIO DO ARRANJO, SE IGUAL, RETORNA O VALOR
# SE MENOR, REALIZA A BUSCA NA METADE INFERIOR DO ARRANJO
# SE MAIOR, REALIZA A BUSCA NA METADE SUPERIOR DO ARRANJO

def buscaSeq(lista, item):
    posicao = 0
    x = False
    while posicao < len(lista) and not x:
        if lista[posicao] == item:
            x = True
        else:
            posicao += 1
    return x

lista = [5, 6, 8, 12, 1, 5, 7]
print(buscaSeq(lista, 8))
print(buscaSeq(lista, 13))



# SOLUÇÃO PROBLEMA 02
# BUSCA BINÁRIA

def buscaBin(lista, item):
    primeiro = 0
    ultimo = len(lista) - 1
    found = False

    while primeiro <= ultimo and not found:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == item:
            found = True
        else:
            if item < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return found


lista = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(buscaBin(lista, 3))
print(buscaBin(lista, 13))
print(buscaBin(lista, 32))



# ORDENAÇÃO
# DEFINIÇÃO:
# DADO UMA SEQUÊNCIA ARBITRÁRIA COM N (>= 0) ELEMENTOS O OBJETIVO DA ORDENAÇÃO É PRODUZIR UMA NOVA SEQUÊNCIA
# EM QUE OS ELEMENTOS APARECEM EM ORDEM
# PARA ORDENAR DETERMINADO DOMÍNIO DE DADOS, DEVE-SE EXISTIR A RELAÇÃO ENTRO OS ELEMENTOS: <, = OU >

# BUBBLE SORT
# PERCORRE O VETOR VÁRIAS VEZES, A CADA PASSAGEM FAZ A TROCA PARA O TOPO O MAIOR/MENOR ELEMENTO DA SEQUÊNCIA
# --- x ---
# ELE FAZ A COMPARAÇÃO DE DOIS ELEMENTOS DE CADA VEZ, FAZENDO ASSIM A DEMORA FICAR MUITO GRANDE
# [6, 5, 3, 1, 8, 7, 2, 4] -> [5, 6, 3, 1, 8, 7, 2, 4] -> [5, 3, 6, 1, 8, 7, 2, 4] -> [5, 3, 1, 6, 8, 7, 2, 4]
# E ASSIM, ELE VAI TROCANDO OS VALORES DE LUGAR COMPARANDO 2 EM 2 ATÉ ORDENAR

def bubbleSort(list):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                print(list)


lista = [54, 26, 93, 17, 77, 31, 44, 55, 28]
bubbleSort(lista)
print(lista)

# SELECTION SORT
# ELE SELECIONA NA LISTA O MENOR VALOR E ADICIONA NA CHAVE 0
# DEPOIS ELE PERCORRE A LISTA NOVAMENTE E PROCURA O MENOR VALOR PRA ADICIONAR NA CHAVE 1
# E ASSIM, SUCESSIVAMENTE

# INSERTION SORT
# O INSERTION SORT ORDENA OS ELEMENTOS INSERINDO-OS NA POSIÇÃO CORRETA
# OS ELEMENTOS SÃO DIVIDIOS EM DUAS REGIÕES, ORDENADOS E AINDA NÃO ORDENADOS
# --- x ---
# ENQUANTO ELE PERCORRE A LISTA, ELE JÁ VAI ANALISANDO E POSICIONANDO OS ELEMENTOS CONFORME O SEU VALOR

# CONCEITOS MERGESORT E QUICKSORT

# MERGESORT
# UTILIZA A ESTRATÉGIA DE DIVISÃO E CONQUISTA
# DIVIDE RECURSIVAMENTE A SEQUÊNCIA AO MEIO
# AO CHEGAR A UMA SUBSEQUÊNCIA UNITÁRIA, ESTA ENCONTRA-SE ORDENADA
# A PARTIR DESSE PONTO, INTERCALE GRADATIVAMENTE SUBSEQUÊNCIAS ORDENADAS
# GERANDO SUBSEQUÊNCIAS ORDENADAS DE MAIOR TAMANHO
# TERMINE AO INTERCALAR A SEQUÊNCIA ORIGIAL

# QUICKSORT
# ESTRATÉGIA DE DIVISÃO E CONQUISTA
# ESCOLHA DE UM ELEMENTO: PIVÔ!
# REARRANJA A LISTA, AONDE TODOS OS ELEMENTOS ANTERIORES AO PIVÔ SEJAM MENORES
# E OS ELEMENTOS POSTERIORES AO PIVÔ SEJAM MAIORES
# RECURSIVAMENTE ORDENA AS SEQUÊNCIAS ESQUERDA E DIREITA DO PIVÔ


def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo - 1)
        executar_quicksort(lista, pivo + 1, fim)
    return lista


def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
    lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
    return esquerda


lista = [10, 9, 5, 8, 11, -1, 3]
executar_quicksort(lista, inicio=0, fim=len(lista) - 1)
print(lista)


# EXERCÍCIO  PROPOSTO
# DICIONÁRIOS

aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Media'] = float(input('Digite a média do aluno: '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
else:
    aluno['Situacao'] = 'Reprovado'

for indice, dado in aluno.items():
    print(f'{indice} é igual a {dado}.')

print(aluno.keys())
print(aluno.values())
