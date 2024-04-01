## Jogo simples utilizando a biblioteca pygame, em que se deve atingir o retângulo com a bola no tempo. No final das contas, se tratava apenas de uma declaração... 
import pygame
import random
import time
import gdown
import os
from pygame.locals import *
from sys import exit

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Configurações da janela
largura, altura = 640, 480
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo: nerd apaixonado 😏")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
preto = (0, 0, 0)

# Variáveis do jogador (bola)
bola_pos = [largura // 2, altura // 2]
bola_raio = 15
velocidade = 10

# Função para gerar uma posição aleatória da dentro da tela
def gerar_alvo():
    return [random.randint(0, largura - alvo_largura), random.randint(0, altura - alvo_altura)]

# Variáveis do alvo retangular
alvo_largura = 100
alvo_altura = 100
alvo_pos = gerar_alvo()

# Tempo limite inicial em segundos
tempo_limite = 40
tempo_extra = 5  # Tempo que será decrescido para cada acerto no alvo
rodada = 1  # Número da rodada

# Tempo inicial
tempo_inicial = time.time()

# Fonte para exibir o tempo
fonte = pygame.font.SysFont(None, 36)

# URL do arquivo MP3 no Google Drive (link de download direto)
url = 'https://drive.google.com/uc?id=1nvf6C1ztpVBNKzeS-MKhJvdVx7kiaVLX'


# Faça o download do arquivo MP3
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
caminho_arquivo_mp3 = os.path.join(downloads_dir, 'musica.wav')
gdown.download(url, caminho_arquivo_mp3, quiet=False)

# Carregar a música
pygame.mixer.music.load('C:/Users/Vitória/Downloads/musica.wav')

# Loop principal
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    # Movimento da bola
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        bola_pos[0] -= velocidade
    if teclas[pygame.K_RIGHT]:
        bola_pos[0] += velocidade
    if teclas[pygame.K_UP]:
        bola_pos[1] -= velocidade
    if teclas[pygame.K_DOWN]:
        bola_pos[1] += velocidade

    #Agora vem uma parte chave do código: uma condição que verifica se a bola acerta o alvo. 
#Se todas essas condições colocadas forem verdadeiras e o tempo limite for maior que zero, significa que a bola atingiu o alvo no tempo e, portanto, um novo alvo deve ser gerado (alvo_pos = gerar_alvo()).

#Exemplo explicativo de uma condição que deve ser satisfeita: bola_pos[0] - bola_raio <= alvo_pos[0] + alvo_largura: Isso verifica se a posição x da bola menos o raio da bola é menor 
    #ou igual à posição x do canto superior direito do alvo (alvo_pos[0] + alvo_largura). Ou seja, verifica se a bola está à esquerda ou sobre o limite direito do alvo.
#Perceba: bola_pos[0]: Essa variável representa a posição x da bola. Em um plano bidimensional, a posição x é a coordenada horizontal, e y a vertical, onde a bola está localizada.
     #enquanto, por exemplo, bola_pos[1], verifica a posição da bola em y
#Assim a localização da bola é representada por bola_pos[0][1], para (x,y).
    
    # Verifica se a bola atingiu o alvo:
    if (bola_pos[0] + bola_raio >= alvo_pos[0] and bola_pos[0] - bola_raio <= alvo_pos[0] + alvo_largura and
        bola_pos[1] + bola_raio >= alvo_pos[1] and bola_pos[1] - bola_raio <= alvo_pos[1] + alvo_altura) and tempo_limite >= 0:
        alvo_pos = gerar_alvo()

        if tempo_limite > 5:
            tempo_limite -= 5
        elif tempo_limite <= 5:
            tempo_limite -= 1
        rodada +=1
        if rodada == 13:
            texto_vitoria = fonte.render("Claro q cê venceu, tô morrendo de saudade Vida!!", True, (0, 0, 0), (255, 255, 255))
            pygame.time.delay(5000)
            texto_vitoria0 = fonte.render("Bora fazer as pazes, depois ir numa roda de samba?", True, (0, 0, 0), (255, 255, 255))
            pygame.time.delay(2000)
            pygame.mixer.music.play()

            # Mostra o texto em sequência
            janela.blit(texto_vitoria, (largura // 2 - texto_vitoria.get_width() // 2, altura // 2 - texto_vitoria.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)

            janela.blit(texto_vitoria0, (largura // 2 - texto_vitoria0.get_width() // 2, altura // 2 - texto_vitoria0.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)

            # Aguarda 40 segundos antes de encerrar o jogo
            pygame.time.delay(40000)
            running = False  # Encerra o jogo
    # Desenhar na tela
    janela.fill(branco)
    pygame.draw.rect(janela, verde, (alvo_pos[0], alvo_pos[1], alvo_largura, alvo_altura))
    pygame.draw.circle(janela, vermelho, bola_pos, bola_raio)

    # Exibir tempo restante na tela
    texto_tempo = fonte.render(f"Tempo: {tempo_limite}", True, preto)
    janela.blit(texto_tempo, (largura - 150, 20))

    pygame.display.update()

    # Espera para controlar a velocidade de atualização da tela
    pygame.time.delay(100)

# Encerramento do Pygame
pygame.quit()
