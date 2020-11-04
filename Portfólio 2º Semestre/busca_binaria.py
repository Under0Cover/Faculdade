'''
def busca_simples (lista_ordenada, elemento_procurado):
    for indice, elemento in enumerate(lista_ordenada):
        if (elemento == elemento_procurado) :
            return indice

    return None


atores = ['Brad', 'Quentin', 'Samuel', 'Tim']
print(busca_simples(atores, 'Brad'))
'''
'''BUSCA BINÁRIA'''

def busca_binaria(lista_ordenada, elemento_procurado):
    primeiro = 0
    ultimo = len(lista_ordenada) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        elemento = lista_ordenada[meio]

        if elemento < elemento_procurado:
            primeiro = meio + 1

        elif elemento > elemento_procurado:
            ultimo = meio - 1

        else:
            return print(f'A posição da vaca é {meio + 1}ª')
    return print('A vaca não está na Lista Relacionada!!!')

'''
print(busca_binaria([0, 5, 7, 10, 15], 0))
print(busca_binaria([0, 5, 7, 10, 15], 15))
print(busca_binaria([0, 5, 7, 10, 15], 5))
print(busca_binaria([0, 5, 7, 10, 15], 6))
print(busca_binaria([-50, -10, 200, 500, 550, 900, 1200, 5000, 8000, 8500], 900))
print(busca_binaria(['A', 'B', 'C', 'D', 'E'], 'A'))
print(busca_binaria(['A', 'B', 'C', 'D', 'E'], 'C'))
print(busca_binaria(['A', 'B', 'C', 'D', 'E'], 'F'))
'''

quantidade = int(input('Digite a quantidade de vacas: '))
lista = []
for contador in range(0, quantidade):
    valor = int(input(f'Digite o valor da {contador + 1}ª posição: '))
    while valor in lista:
        print('A vaca já está registrada no sistema!!')
        valor = int(input(f'Digite o valor da {contador + 1}ª posição: '))
    lista.append(valor)
lista.sort()
print(f'A lista de vacas gerada foi: {lista} ')
posicao = int(input('Digite o número da vaca para encontrar sua posição: '))
print(busca_binaria(lista, posicao))