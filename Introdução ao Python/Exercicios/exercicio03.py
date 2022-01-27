#Operadores Condicionais = if, elif e else
#Operadores Logicos = and, or

# Usando estruturas condicionais
# Exercicio 01
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior numero é {}' .format(b))
# else:
#     print('o maior número é {}' .format(c))
# # a identação separa a linha de codico da linha da condição
# print('final do programa')

#Exercicio 02

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
# resto_a = a % 2
# resto_b = a % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('foi digitado um numero par')
# else:
#     print('nenhum numero par foi digitado')

#Exercicio 03

a = int(input('Primeiro Brimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Brimestre: '))
c = int(input('Terceiro Brimestre: '))
d = int(input('Quarto Brimestre: '))
media = (a + b + c + d) / 4
print('media: {} ' .format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' .format(media))
# else:
#     print('foi digitado alguma nota errada')


