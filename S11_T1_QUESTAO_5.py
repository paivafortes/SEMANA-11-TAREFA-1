#Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. 
# Pedro também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. 
# Considerando que a situação se refere ao mês de outubro do ano de 2016, 
# faça um programa leia o valor do salário e o valor da dívida e calcula, 
# simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com o cartão de crédito será superior ao seu próprio salário.
#Represente os meses como inteiros de 1 a 12.
#Dica: Controle essas quatro variáveis:
#“dívida” que aumenta todo mês; “salário” que aumenta apenas se o número do mês for 3 (março); 
# “mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12; “ano” que só é incrementado quando o mês retornar a 1.



salario = float(input())
divida = float(input())

mes = 10  
ano = 2016
divida_t= divida

while divida_t <= salario:
    mes += 1

    if mes > 12:
        mes = 1
        ano += 1

    if mes == 3:
        salario = salario * 1.05  

    divida_t += divida_t * 0.15 
print(f'{mes}/{ano}')
