# crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dolares ele pode comprar

real = float(input('Quanto dinheiro você tem na caryeira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))