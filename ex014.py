#escreva um programa que converta uma temperatura digitando
#em graus Celsius °C e converta para graus Fahrenheit °F.

c = float(input('Informe a temperatura em °C: '))
#f = ((9 * c) / 5) + 32 devido a ordem de precedência, nesse caso caso não necessitaria dos parêneses
f = 9 * c / 5 + 32
print('A temperatura de {}°C corresponde a {}°F'.format(c, f))
