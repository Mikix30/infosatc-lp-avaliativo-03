
# Atividade número um.
#Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com esse número.

meses = {
    1  : "Janeiro",
    2  : "Fevereiro",
    3  : "Março",
    4  : "Abril",
    5  : "Maio",
    6  : "Junho",
    7  : "Julho",
    8  : "Agosto",
    9  : "Setembro",
    10 : "Outubro",
    11 : "Novembro",
    12 : "Dezembro",

}    

mes = int(input("Qual o mês desejado? Lembre-se de digitar um número de 1 a 12. "))

if mes in meses:
    print("O mês escolhido foi: ",meses.get(mes))
else:
    print("valor invalido, por favor tente novamente.")