# try:
#     x = int(input('Podaj pierwsza liczbe '))
#     y = int(input('Podaj 2gą liczbe '))
#     z = x / y
# except ZeroDivisionError:
#     print('cos nie pykło, przyjmuje wynik 1')
#     z = 1
# except ValueError:
#     print('zle wpisane dane, pryzjmuje x = y = 3')
#     x = y = 3
#     z = x / y
#
# print(z)
# print('Dalsza'
#       'czesc programu')
#
#
# def my_sample_function(pierwsza, druga, trzecia):
#     return x + y * z
import base64

#
# my_sample_function(2, 3, 4)
#
#
# 'mama'.replace('m','M')
#
# for i in range(3, 15, 3):
#     print(i)
#
# for i in range(100, -1, -10):
#     print(i)
#
# lista_imion = ['Jagoda', 'Paula', 'Malgorzata', 'Mariusz']
#
# for imie in lista_imion:
#     print(imie)

import keyring

keyring.set_password('a', 'b', 'c')
print(keyring.get_password('a', 'b'))

# password = 'my_pass'.encode('utf-8')
# print(password)
# encoded = base64.b64encode(password)
# print(encoded)
# decoded = base64.b64decode(encoded)
# decoded = decoded.decode('utf-8')
# print(decoded)