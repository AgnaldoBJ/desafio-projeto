# try:
# except: encadeia condições de excessao
# else:
# finally: sempre sera executado


# try:
#     divisao = 10 / 0
# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por zero')

lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]


except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}' .format(ex))
else:
    print('Execute quando não ocorrer exceção')
finally:
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()