# interagindo com modulos e classes de outros arquivos

from exercicio07_part3 import Televisao
from exercicio07 import  Calculadora
from exercicio08_part2 import contador_letra

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    toltal_letras = contador_letra(lista)
    print('total de letras por palavra de lista: {}' .format(toltal_letras))