try:
    x = int(input('Podaj pierwsza liczbe '))
    y = int(input('Podaj 2gą liczbe '))
    z = x / y
except ZeroDivisionError:
    print('cos nie pykło, przyjmuje wynik 1')
    z = 1
except ValueError:
    print('zle wpisane dane, pryzjmuje x = y = 3')
    x = y = 3
    z = x / y

print(z)
print('Dalsza'
      'czesc programu')


def my_sample_function(pierwsza, druga, trzecia):
    return x + y * z


my_sample_function(2, 3, 4)


'mama'.replace('m','M')




