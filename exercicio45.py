import random
import time

print('-' * 40)
print('\033[1;36mBEM VINDO AO JOKENPO!\033[m')
print('-' * 40)

while True:
    try:
        num = int(input('''
você tem três opções
\033[1;31m[0] = pedra\033[m
\033[1;32m[1] = papel\033[m
\033[1;34m[2] = tesoura\033[m
digite aqui: '''))
    except:
        print('o jogo só funciona com números, por favor digite um')
    else:
        if num == 0 or num == 1 or num == 2:
            break
        else:
            print('digite um dos valores selecionados.')
cpu = random.randint(0, 2)

time.sleep(1)
print('''
    \033[1;31mJO\033[m''', end='')
time.sleep(1)
print('''
        \033[1;32mKEN\033[m''', end = '')
time.sleep(1)
print('''
            \033[1;34mPO\033[m''')

if num == 0: #caso em que o usuário escolhe pedra
    if cpu == 0:#caso em que o computador escolhe pedra
        print('\033[1;33mtemos um empate!\033[m nós dois escolhemos pedra.')
    elif cpu == 1:#caso em que o computador escolhe papel
        print('OTARIO, \033[1;31mvocê perdeu!\033[m eu escolhi papel e você pedra.')
    else:#caso em que o computador escolhe tesoura
        print('droga, \033[1;32mvocê ganhou!\033[m eu escolhi tesoura e você pedra.')
elif num == 1: #caso em que o usuario escolhe papel
    if cpu == 0:
        print('droga, \033[1;32mvocê ganhou!\033[m eu escolhi pedra e você papel.')
    elif cpu == 1:
        print('\033[1;33mtemos um empate!\033[m nós dois escolhemos papel.')
    else:
        print('OTARIO, \033[1;31mvocê perdeu!\033[m eu escolhi tesoura e você papel.')
else: #caso em que o usuário escolhe tesoura
    if cpu == 0:
        print('OTARIO, \033[1;31mvocê perdeu!\033[m eu escolhi pedra e você tesoura.')
    elif cpu == 1:
        print('droga, \033[1;32mvocê ganhou!\033[m eu escolhi papel e você tesoura')
    else:
        print('\033[1;33mtemos um empate!\033[m nós dois escolhemos tesoura')


