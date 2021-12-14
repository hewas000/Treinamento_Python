#faça um algoritmo que leia o salario de um funcionario e
#mostre seu novo salario, com 15% de aumento.

salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
