'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''

'''.strip() essa função elimina os espaços antes e depois do/dos nome/nomes'''
'''.split() essa função faz o fatiamento dos nomes em pedaços separados por espaços '''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('seu último nome é {}'.format(nome[len(nome)-1]))
