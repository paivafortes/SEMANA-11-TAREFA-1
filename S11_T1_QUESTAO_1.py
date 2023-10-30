#Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. 
# Mostre em quantos anos o valor acumulado será o dobro do valor inicial.

deposito = float(input())
taxa = float(input())
acumulado = deposito
anos = 0 
while acumulado < 2 * deposito:
    acumulado += acumulado *(taxa / 100)
    anos += 1

print (f'{anos}')

