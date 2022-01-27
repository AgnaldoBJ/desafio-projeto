# listas e tuplas

# Listas são mutaveis pode-se fazer alteração nos dados
lista = [1, 3, 5, 7]
lista_animal = ['cachorro' , 'gato' , 'elefante' , 'lobo' , 'arara']
# print(lista_animal[0])

# for x in lista_animal:
#     print(x)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# somando todos os numeros da lista com 'sum'
# 'max' traz o maior valor da lista
# 'min' traz o menor valor da lista

# print(sum(lista))
# print(max(lista))
# print(min(lista))

# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo'in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um lobo na lista')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
#     lista_animal.pop(0)
#     print(lista_animal)
#
#     lista_animal.remove('elefante')
#     print(lista_animal)

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

#tuplas são imutaveis, não da para fazer nenhuma alteração nos dados

tupla = (1, 10, 12, 14)
# print(tupla[2])
print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)


