# Por favor, entre com: pedra , papel ou tesoura
import random

possibilities = {'pedra': 1, 'tesoura': 2, 'papel': 3}

player = input().lower()

if not (player == 'pedra' or player == 'tesoura' or player == 'papel'):
    print('Incorreto: digite: pedra ou papel ou tesoura...')
    exit()

num  = possibilities.get(player)
computer = random.choice(list(possibilities.keys()))
num_computer = possibilities[computer]

print('You : {} - {} | Computer: {} - {}'.format(num, player, num_computer, computer))

result = num - num_computer
if result in [-1, 2]:
    print(' \n You Win!!')
elif result in [-2, 1]:
    print(' \n Computer Wins.')
else:
    print(' \n It\'s a draw.')