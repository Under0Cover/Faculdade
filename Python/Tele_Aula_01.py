# EXEMPLOS PRÁTICOS DA TELE AULA 01 - LINGUAGEM DE PROGRAMAÇÃO PYTHON

# INÍCIO DA AULA
# EXERCÍCIO 01
print('Olá, Mundo!')
print('-=-' * 50)

# EXERCÍCIO 02
nome = input('Digite o seu nome: ')
print(nome)

# EXERCÍCIO 03
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
print(nome)
print(idade)

# ESTRUTURAS IF-ELIF-ELSE
# ESTRUTURA FOR
# EXERCÍCIO 04
# EXEMPLO:
for i in range(10):
    print(i + 1, end=' ')
print(' ')

# EXERCÍCIO 05
# CÁLCULO IMPORTO
salario = int(input('Salário: '))
imposto = input('Importo: ')

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)
sal_liquido = salario - (salario * (imposto * 0.01))
print(sal_liquido)


# FUNÇÕES BUILT-IN
# EXERCÍCIO 06
def soma(x, y):
    r = x + y
    return r


a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))

s = soma(a, b)
print('a + b = {}'.format(s))
s = soma(a, c)
print('a + c = {}'.format(s))
s = soma(b, c)
print('b + c = {}'.format(s))
print('FIM DO PROGRAMA')
print(' ')


# FUNÇÕES GLOBAIS E LOCAIS
# EXERCÍCIO 07

def estuda_escopo():
    y = x * 2
    print('X Global existe dentro da função: valor = {0}'.format(x))
    print('Y Local existe dentro da função: valor = {0}'.format(y))


print('Início do Programa')
x = 10
print('X Global existe fora da função: valor = {0}'.format(x))
estuda_escopo()
print('Fim do Programa')
print(' ')


# FUNÇÕES COM PARÂMETROS
# EXERCÍCIO 08

def ler_inteiro():
    n = int(input('Digite um número inteiro: '))
    return n


x = ler_inteiro()
print('Valor lido na função = {0}'.format(x))


# FUNÇÕES COM PARÂMETROS
# EXERCÍCIO 09

def soma(x, y=1):
    r = x + y
    return r


print(' ')
print('Início do Programa')
a = int(input('Deigite um valor para a: '))
b = int(input('Digite um valor para b: '))
s = soma(a, b)
print(s)


# EMPACOTAMENTO E DESEMPACOTAMENTO DE PARÂMETROS
# EXERCÍCIO 10

def exibe_formato (a, b, c):
    print('1º valor = {0}'.format(a))
    print('2º valor = {0}'.format(b))
    print('3º valor = {0}'.format(c))

l = (31, 77, 193)
exibe_formato(*l)
print(' ')
l = (66, 99, 101)
exibe_formato(*l)
print(' ')
# A professora passou 4 valores 2x
# O programa apresentou erro nas 2x
# O segundo erro é proposital

# FUNÇÃO ANÔNIMAS
# EXPRESSÃO ÇAMBDA
# MEDIA = LAMBDA VALORES:SUM(VALORES)/LEN(VALORES)

# ESTRUTURA WHILE
# EXERCÍCIO 11

def calculo_imposto():
    imposto = 27.5
    while imposto > 0:
        imposto = input('Imposto ou (S) Sair: ').upper().strip()
        if not imposto:
            imposto = 27.5
        elif imposto == 'S':
            break
        else:
            imposto = float(imposto)
        print("Valor Final {0}".format(salario - (salario * imposto * 0.01)))

salario = int(input('Qual é o seu salário: '))
calculo_imposto()

# ESTRUTURA FOR
# EXERCÍCIO 12

for i in range(6):
    print(i)