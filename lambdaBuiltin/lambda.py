'''
lambda é uma função sem nome, uma arrow function de js

map -> mapeia a função e retorna a mesma quantidade de dados da entrada
filter -> retorna uma quantidade menor ou igual a quantidade inicial
reduce -> retorna apenas um único valor

nome_completo(print('       denilson', 'freitas         '))
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

nomes = ['Issac Asimov', 'Ray Brad', 'Leigh Cabrght']
nomes.sort(key=lamda sobrenome: sobrenome.split(' ')[-1].lower())
print(nomes)

funcao quadratica
def geradora_funcao_quadradica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadradica(2, 3, -5)

print(teste(4))

MAP
#apos utilizar a função map() depois da primeira utilizacao de resultado, ele zera

#recebe dois valores uam função e um iterável e retorna um objeto mapeando a funcao para cada elemento de iterável -> a função retorna tudo


a função pode ser com nome uma lambda

print(list(map(lambda r: math.pi * (r ** 2), raios))

cidade = [('Berlin': 29), ('Cairo': 48), ('Los Angeles': 11)]

c_para_f = map(lambda dada: (dado[0], (9/5) * dado[1] + 32))


FILTER
# recebe dois params uma função e um iterável e retorna um objeto fitlrando apenas os elementos de acordo com a função  - a função do filter retorna True or False

Filter + MAP

nome = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))  --função, dados


usuarios = [
    {"usuario": "samuel", "tweets": ["Eu amo bolos", "Eu adoro pizza"]},
    {"usuario": "carla", "tweets": ["Eu amo gato"]},
    {"usuario": "jeff", "tweets": []},
    {"usuario": "bob123", "tweets": ["Eu amo bolos", "eu adoro pizza"]}
    {"usuario": "gal", "tweets": ["eu adoro pizza"]}
]

inativos = list(filter(lambda usuario: len(u['tweets']) == 0, usuarios))
inativos2 = list(filter(lambda usuario: not usuario["tweets"]), usuarios))


REDUCE

TAMBÉM RECEBE DOIS VALORES, FUNÇÃO E UMA COLEÇÃO DE DADOS

aplica a função nos dois primeiros elementos da colação e guarda o resultado.
aplica  afunção passando o resultado do passo1 mais terceiro elemento e guarda o res, isso é repetido até o final
em cada passo aplica o resultado anterior e aplicando o próximo e retornando o reduce


dados = list(range(1,20))

multi = lambda x,y: x * y

res = reduce(multi, dados)


Funções Built-in
ALL
all -> retorna True se todos os elementos do interável são verdadeiros ou ainda se o interável está vazio

ANY
any -> retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, False

Generator
é quase igual a uma tupla mas não retorna valor algum é bom quando não precisamos do valor, apenas do resultado disso

nommes com a letra C com generator

nomes = ['Carlos', 'Camila', 'Carla', 'Denilson']
print(any(nome[0] == 'C' for nome in nomes))
ele é muito mais leve do que qualquer outro tipo e não executa, ele é um lazy valuation



SORTED

o sorted não modifica os dados original, transforma apenas para mostra naquela hora
sorted(dados, key)



usuarios = [
    {"usuario": "samuel", "tweets": ["Eu amo bolos", "Eu adoro pizza"]},
    {"usuario": "carla", "tweets": ["Eu amo gato"]},
    {"usuario": "jeff", "tweets": []},
    {"usuario": "bob123", "tweets": ["Eu amo bolos", "eu adoro pizza"]}
    {"usuario": "gal", "tweets": ["eu adoro pizza"]}
]

print(sorted(usuario, key=lambda usuario: usuario['usuario']))



MAX E MIN
pode ser usado com qualquer tipo de dado


REVERSED

OBS: A função reverse() só funciona em listas.
Já a função reversed funciona com qualquer interável


ZIP
Cria um iterável Zip Object que agrega elemento de cada um dos iteráveis passados como entrada em paras

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)

[(1, 4), (2, 5), [3,6]]

ele faz isso mas tem que ser a mesma qtd

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, provas2)}


'''

