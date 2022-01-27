# Operadores Aritmeticos
a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
print(soma)
soma = str(soma)
print(type(soma))
print(('soma:' + str(soma)))
print(subtracao)
print(multiplicacao)
print(type(divisao))
print(divisao)
print(int(divisao))
print(resto)

x = '1'
soma2 = int(x) + 1
print(soma2)

# Melhor maneira de alterar a type com strings

print('soma:{}' .format(soma))
print('soma:{} \nsubtração:{} \nmultiplicação:{} \ndivisão:{} \nresto:{}' .format(soma, subtracao, multiplicacao, divisao, resto))

# Como interagir com o usuario

a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(a + b)