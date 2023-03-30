import random

rounds = 3
computer_wins = 0
user_wins = 0


def chose_options():
    options = ('piedra', 'papel', 'tijera')
    print('#'*10)
    print('Apartado para seleccion')

    user_options = input('Ingrese su opcion (Piedra, Papel, tijera)').lower()

    while user_options not in options:
        print('ALERT ' * 2 + 'Opcion invalida')
        user_options = input(
            'Ingrese de nuevo su opcion (Piedra, Papel, tijera)')
        continue
    computer_options = random.choice(options)
    return user_options, computer_options


