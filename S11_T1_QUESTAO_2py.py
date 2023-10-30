#Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). 
# Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero).


soma = 0
contador = 0

while True:
    numero = int(input())
    if numero == 0:
        break
    if numero > 0:
        soma += numero
        contador += 1


media = soma / contador
print(f'{media:.2f}')
