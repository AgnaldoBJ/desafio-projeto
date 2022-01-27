# Comdandos de repetição For, While e Range - (para gerar numeros sequenciais)

# for x in range(1, 100):
#     print(x)

# a = int(input('Entre com um numero: '))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('numero {} é primo' .format(a))
# else:
#     print('numero {} não é primo' .format(a))

# a = int(input('Entre com um valor: '))
# # for num in range(101):
# for num in range(a+1):
#
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

# a = 0
# while a < 10:
#     print(a)
#     a += 1

nota = int(input('Entre com a nota'))
while nota > 10:
    nota = int(input('Nota invalida. Entre com a nota correta: '))
print(nota)

