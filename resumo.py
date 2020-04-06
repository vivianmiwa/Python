'''

# Elif:
x = 1
y = 2

if x == y:
    print("x eh igual a y")
elif x < y:
    print("x eh menor que y") # executa o primeiro elif certo
elif y > x:
    print("y eh maior que x")
else:
    print("x eh diferente de y")

# Laços:
for i in range(10): # vai do 0 ao 9
    print(i) 

for j in range(10,20): # vai de 10 ate 19
    print(j)

for j in range(10,20,2): # vai de 10 ate 19, de dois em dois
    print(j)

# Strings:
nome1 = "Shakira"
nome2 = "Mishi"

concatenar = nome1 + " e " + nome2 + "\n"

print(concatenar)

tamanho = len(concatenar) # devolve tamanho da string
print(tamanho)

print(concatenar[0:5]) # [inicio, qtde]

print(concatenar.lower()) # converte para minusculo

print(concatenar.strip()) # remove o caractere "\n"

frase = "O rato roeu a roupa do rei de Roma"
print(frase.split()) # divide a string a cada espaço

print(frase.split("r")) # divide a string a cada espaço, excluindo o caractere "r"

print(frase.find("r")) # busca o indice da primeira ocorrencia do que esta buscando

print(frase.replace("rei", "rainha")) # substitui uma coisa por outra

# Funções:
def soma(x, y): # def usado para definir uma funcao
    print(x+y)

soma(2,3) # chamada da funcao e entrada de dados

# Listas:

lista1 = ["morango", "tomate", "melao"]
lista2 = ["abacaxi", 2, 4.5, True]
print("Lista 1: ")
print(lista1)
print("Lista 2: ")
print(lista2)
print("Elemento 0 da Lista 1: ")
print(lista1[0])

for item in lista2: # percorre toda a lista
    print(item)

tamanho = len(lista1)
print("Tamanho da lista: ")
print(tamanho)

lista1.append("limao") # adiciona elemento no final da lista
print(lista1)

if "abacaxi" in lista2: # verifica se elemento esta na lista
    print("esta na lista")
else:
    print("nao esta na lista")

del lista1[0:1] # deleta o primeiro elemento
print(lista1)
del lista1[:] # deleta lista toda
print(lista1)


lista3 = [21, 45, 20, 10, 41, 10, 11, 54, 1]
lista3.sort() # ordena a lista original
print(lista3)

ordenada = sorted(lista3) # retorna a lista ordenada
print(ordenada)

lista3.sort(reverse=True) # ordena decrescente
print(lista3)

lista3.reverse() # inverte a ordem da lista
print(lista3)

# Dicionário: chave:valor

dicionario = {"A":"Ameixa", "B":"Banana", "C":"Coco"}
print(dicionario)
print(dicionario["C"]) # imprime o valor da chave

for chave in dicionario: # imprime as chaves
    print(chave)

for chave in dicionario:
    print(dicionario[chave]) # imprime os valores

for i in dicionario.items(): # retorna os valores como uma tupla como se fosse lista
    print(i)

for i in dicionario.keys(): # mostra só as chaves
    print(i)

for i in dicionario.values(): # mostra só os valores
    print(i)


# Números aleatórios:

import random

numero = random.randint(0, 10) # de 0 a 10
print(numero)

random.seed(1) # força a dar sempre o mesmo número
numero = random.randint(0, 10)
print(numero)

lista = [3, 45, 9]
numero = random.choice(lista) # seleciona número de uma lista
print(numero)


# Tratamento de exceções:

a = 2
b = 0

try:
    print(a/b)

except:
    print("divisao por 0")

# Entrada de dados:

nome = input("Digite seu nome: ") # le string do teclado
print("Bem vindo(a),", nome)

idade = int(input("Digite sua idade: ")) # le int do teclado

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")


nota = float(input("Digite sua nota: ")) # le float do teclado

if nota < 6:
    print("Reprovado")
else:
    print("Aprovado")


# List comprehension:

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2) # ao quadrado

print(x)
print(y)

# usando list comprehension:

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x] # [valor_a_adicionar laço condição]

print(x)
print(y)

z = [i for i in x if i%2==1] # adiciona impares de x em z
print(z)


# Função enumerate:

lista = ["banana", "abacate", "mamão"]

for i in range(len(lista)): # range cria o vetor e len mede o tamanho
    print(i, lista[i])

# usando o enumerate:

for i, nome in enumerate(lista): # retorna o indice e o valor
    print(i, nome)


# Função filter: filtra uma lista com base em uma função
# pra ser adicionada em outra lista

def pares(i):
    if i%2 == 0: # se for par
        return i

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filter(pares, lista) # filter(função, parametro)

print(list(lista_pares)) # converte obj do tipo filter para tipo lista


# Função map: aplica uma função para todos os elementos de uma lista

def dobro(x):
    return x*2 # multiplicar lista por 2 eh concatenar a lista com ela mesma

valor = [1, 2, 3, 4, 5]
print(dobro(valor))

# usando função map:

valor_dobrado = map(dobro, valor) # map(função, lista)
# recebe um obj do tipo map

# pode acessar os elementos do obj iterativamente:
for v in valor_dobrado:
    print(v)

# ou converter o tipo do obj para lista:
valor_dobrado = list(valor_dobrado) 
print(valor_dobrado)


# Função zip: concatena listas alternadamente

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]

for numero, nome in zip(lista1, lista2):
    print(numero, nome)


'''