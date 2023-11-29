import bcrypt

password = input('Podaj haslo: ')
password = password.encode('utf-8')

hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(10))
print(hashed_password)

check = input('Sprawdź haslo ')
check = check.encode('utf-8')

if bcrypt.checkpw(check, hashed_password):
    print('password ok')
else:
    print('Incorrect password')