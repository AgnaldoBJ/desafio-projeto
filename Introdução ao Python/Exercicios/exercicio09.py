# Para escrever um arquivo no python usamos a letra 'w'
# quando precisamos atualizar o arquivo existente usamos 'a'
# quando vamos ler um arquivo usamos 'r'
# Exemplos de como abrir um arquivo:
#   diretorio = 'C:/Projeto/globalabs/teste.txt'
#   arquivo = open(diretorio, 'w') ou
#   arquivo = open('C:/Projeto/globalabs/teste.txt,' 'w')
# usando o split posso transformar uma string em uma lista

import shutil
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        # print(sum(lista_notas))

def copia_arquivo(nome_arquivo):

    shutil.copy(nome_arquivo, #'C:/Projetos/globallabs/')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,  # 'C:/Projetos/globallabs/')

if __name__ == '__main__':
    copia_arquivo('notas.txt')
    mover_arquivo('notas.txt')
    # media_notas('notas.txt')
    # escrever_arquivo('Primeira linha.\n')
    # aluno = ('\nBrito, 10,10,5,5\n')
    # atualizar_arquivo('notas.txt', aluno)
    # # ler_arquivo('teste.txt')