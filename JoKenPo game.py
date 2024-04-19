import random
computer = randint(0,2)

#a máquina sorteia um número aleatório e armazena isso na variável 'computer'.
#Mostro as opções de escolha para o usuário.
print('Pedra Papel e Tesoura game¨&¨&¨')
print('opções:')
print('0->pedra')
print('1->papel')
print('2->tesoura')

jogador = int(input('Escolha um valor:')) #o usuário escolhe e eu armazeno isso na variável 'jogador'.

print('JO')
print('KEN')
print('PÔ!!')

if (jogador == computer):
    print('Empate!')
else:
    if((jogador == 0 and computer == 1) or (jogador == 1 and computer == 2) or (jogador == 2 and computer == 0 )):
        print('o computador ganhou essa, ein. Vc perdeu!')
    else:
        print('Vc ganhou!')
                     
x = 'pedra'
y = 'papel'
z = 'tesoura'
if (computer == 0):
    computer = x
else:
    if (computer == 1):
        computer = y
        jogador = y
    if (computer == 2):
        computer = z
if (jogador == 0):
            jogador = x
else:
        if (jogador == 1):
            jogador = y
        if (jogador == 2):
            jogador = z


print('Vc escolheu', jogador)
print('A máquina escolheu', computer)