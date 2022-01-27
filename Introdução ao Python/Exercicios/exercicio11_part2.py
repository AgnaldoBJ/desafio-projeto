# break - força a saida do loop
# para se criar uma classe de exceção personalizada é preciso,
# deve existir uma classe 'Error' mesmo que ela não faça nada e depois criar a classe personalizada
# comando 'Raise' força uma exceção



class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com um nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que zero')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)