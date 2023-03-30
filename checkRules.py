def checkRules(user, computer, user_winners, computer_winners):
    if user == computer:
        print('*' * 10)
        print('EMPATE')
        print('*' * 10)
    elif user == 'piedra' and computer == 'tijera' or \
            user == 'papel' and computer == 'piedra' or \
            user == 'tijera' and computer == 'papel':
        print('Gana Usuario')
        user_winners += 1
    else:
        print('Gana Computador')
        computer_winners += 1
    return computer_winners, user_winners
