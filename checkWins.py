def checkWins(computer_winners, user_winners):
    print('* ' * 10)
    if computer_winners > user_winners:
        print('*'*10 + ' ' + 'computador gano')
    elif user_winners > computer_winners:
        print('*'*10 + ' ' + 'Gano el usuario')
    else:
        print('El juago quedo en empate')
        print('* ' * 10)
