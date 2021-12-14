#Escreva um programa que leia em metros e exiba convertido em centimetros e milimetros

medida = float(input('Uma medida em metroa: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

#fazer a mesma operação com todas as outras medidas metricas!
