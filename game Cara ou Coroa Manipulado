## Esse programa simula um jogo em que o usuário tenta adivinhar se vai se sair cara (0) ou coroa (1). 
# Ele segue a mesma lógica que os jogos de azar da internet de hje em dia! Ou seja, o usuário vai perder sempre que o algoritmo quiser😉
#Nessa versão, o usuário jamais ganhará acima de 30% das vezes

#Se quiser rodar o código, acesse: https://www.online-python.com/
#copie e cole o código abaixo, dê run e siga o passo a passo do joguinho!


import random
import pandas as pd

c = 0
n = int(input("Quantidade de jogadas: "))
valores_sorteados = []  # Lista com os valores sorteados
escolhas_usuario = []  # Lista com os valores escolhidos pelo usuário
print('No jogo, Cara = 0, Coroa = 1')

# Preenche a lista de escolhas do usuário
for i in range(1, n + 1):
    while True:
        escolha = int(input("Escolha um valor (0 ou 1): "))
        if escolha == 0 or escolha == 1:
            escolhas_usuario.append("cara" if escolha == 0 else "coroa")
            break
        else:
            print("Escolha inválida. Por favor, escolha 0 ou 1.")

# O programa repete a operação de preencher a lista de sorteados enquanto o percentual de vitórias do usuário for maior que 30%
while True:
    # Reinicia o contador de acertos e a lista de valores sorteados
    c = 0
    valores_sorteados = []

    # Preenche a lista de valores sorteados
    for i in range(1, n + 1):
        x = random.randint(0,1)
        valores_sorteados.append("cara" if x == 0 else "coroa")

        # Verifica se o valor sorteado é igual à escolha do usuário na posição i-1
        if valores_sorteados[i - 1] == escolhas_usuario[i - 1]:
            c += 1

    # Atualiza a probabilidade como a razão entre o número de acertos (c) e o número total de jogadas (n)
    prob = c / n

    # Se a probabilidade for menor ou igual a 30%, interrompe o loop
    if prob <= 0.3:
        break

# Monta e exibe os resultados como uma tabela:
df = pd.DataFrame({'jogada': escolhas_usuario,'valor sorteado': valores_sorteados})
print(df)


#Exibe o percentual de acertos:
print("Percentual de acertos do usuário:", prob,"%")
