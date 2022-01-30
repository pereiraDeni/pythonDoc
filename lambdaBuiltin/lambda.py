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

recebe dois valores uma função e os dados

a função pode ser com nome uma lambda

print(list(map(lambda r: math.pi * (r ** 2), raios))

cidade = [('Berlin': 29), ('Cairo': 48), ('Los Angeles': 11)]

c_para_f = lambda dada: (dado[0], (9/5) * dado[1] + 32)




'''