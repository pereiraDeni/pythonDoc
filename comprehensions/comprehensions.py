'''
[return (if return 2 else) looping (if else)]

Ex.: 
numbers = [1, 4, 5, 6]
duble = [number * 2 for number in numbers]

pares
numbers = list(range(1, 20))
even = [number for number in numbers if not number % 2] # porque quando o numero for par numero % 2 = 2  e isso é false
odd = [number for number in numbers if number % 2]

numero = [number * 2 if number % 2 == 0 else number for number in numbers]

LISTA ANINHADA

numeros = [[1,2,3], [4,5,6], [7,8,9]]

for x in numeros:
    for y in x:
        print(y)

[[print(y) for y in x] x in numeros]

matriz 3x3:
aqui o segundo elemento valor in range(1,4) cria as listas
e o numero for numero in range(1,4) cria os elementos dentro de cada lista
tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]

DICT COMPREHENSION
mesma coisa do outro só que aqui temos dicionários

numero = (1, 2, 3, 4, 5,)

quadrado = {valor: valor ** 2 for valor in numero}

mistura 
chave = 'abcde'
valores = [1,2,3,4,5,6]
mistura = {chave[i]: valores[i] for i in range(0, len(chaves))}

lógica condicional:
numeros = list(range(1,11))
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num numeros}

set = {}
list = []
tuple = ()
dict = {key: value}

'''