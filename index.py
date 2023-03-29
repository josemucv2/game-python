# Realice el juego de piedra papel o tijera contra una Computdaro

import random

options = ('piedra', 'papel', 'tijera')

rounds = 3
computer_winners = 0
user_winners = 0


for i in range(1, rounds+1):
    print('*' * 10)
    print(f'Rounds: {i}')
    print('Mucho Exito!!')
    print('*' * 10)

    user_options = input('Ingrese su opcion (Piedra, Papel, tijera)').lower()
    while user_options not in options:
        print('Invalid')
        user_options = input(
            'Ingrese de nuevo su opcion (Piedra, Papel, tijera)')
        continue
# Reacorder colocar el continue, una vez que se cumpla la condicion
    computer_options = random.choice(options)

    if user_options == computer_options:
        print('*' * 10)
        print('Empate')
    elif user_options == 'piedra' and computer_options == 'tijera' or \
            user_options == 'papel' and computer_options == 'piedra' or \
            user_options == 'tijera' and computer_options == 'papel':
        print('Gana Usuario')
        user_winners += 1
    else:
        print('Gana Computador')
        computer_winners += 1

print('* ' * 10)
if computer_winners > user_winners:
    print('*'*10 + ' ' + 'computador gano')
elif user_winners > computer_winners:
    print('*'*10 + ' ' + 'Gano el usuario')
else:
    print('El juago quedo en empate')
print('* ' * 10)
