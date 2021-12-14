'''Crie um programa que leia o nome de uma cidade
diga se ela começa ou não com o nome “SANTO”.
strip() = elimina os espaços do inicio e do fim
upper() = faz com que o programa leia de forma correta em maiuscula e menuscula'''

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')