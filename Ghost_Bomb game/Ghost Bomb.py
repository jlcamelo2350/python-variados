#É um game simples em que um fantasma é bombardeado por vários tipos de objetos e deve simplesmente desviar deles durante um determinado período de tempo.

#Importa-se as bibliotecas
import pygame
import sys 
import random  
import gdown ##possibilita o download de arquivos do google drive (vou baixar um som para a mensagem de vitória/derrota)
import os

pygame.init()  # Inicializa o Pygame
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600  # Define a largura e altura da janela do jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Cria a janela do jogo com o tamanho especificado
pygame.display.set_caption("Explodam o fantasma")  # Define o título da janela

WHITE = (255, 255, 255)  # Define a cor branca
BLACK = (0, 0, 0)  # Define a cor preta

# Classe da Bola
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cria a imagem da bola (fantasma! uuuhh). Respectivamente, configura-se o fantasma, os olhos (esquerdo, depois direito) e a posição inicial dele
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (25, 25), 25)  
        pygame.draw.circle(self.image, BLACK, (15, 15), 5) 
        pygame.draw.circle(self.image, BLACK, (35, 15), 5)  
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))  
        self.speed = 5  # Define a velocidade de movimento da bola

# Classe dos Objetos que Caem
class FallingObject(pygame.sprite.Sprite):
    def __init__(self, player_x):
        super().__init__()
        # Cria a imagem do objeto que cai. Respectivamente, configura-se a largura, a altura, a posição daonde ele cairá e a velocidade de queda
        self.width = random.randint(20, 50)  
        self.height = random.randint(20, 50) 
        self.image = pygame.Surface((self.width, self.height)) 
        self.image.fill(WHITE)  
        self.rect = self.image.get_rect(center=(player_x, 0))  
        self.speed = random.randint(10, 11)  

    def update(self):
        self.rect.y += self.speed  # Atualiza a posição do objeto para fazê-lo cair

# Variáveis e Grupos
ball_group = pygame.sprite.Group()  # Cria um grupo para o fantasma
falling_objects_group = pygame.sprite.Group()  # Cria um grupo para os objetos que caem
clock = pygame.time.Clock()  # Cria um objeto Clock para controlar o FPS do jogo

ball = Ball()  # Cria uma instância da classe Ball
ball_group.add(ball)  # Adiciona a bola ao grupo de sprites da bola

player_x = WIDTH // 2  # Define a posição inicial do jogador no centro da tela

TIME_LIMIT = 3600  # Define o limite de tempo do jogo em frames (60 segundos * 60 FPS)
time = TIME_LIMIT  # Inicializa o tempo restante do jogo

# URL do arquivo MP3 no Google Drive (link de download direto) - caso de vitória
url = 'https://drive.google.com/uc?export=download&id=12st5I2ULE4jWAyauu9ecZ5K0l5mDM1Vt'

downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads') ##irei armazenar o arquivo na pasta download do jogador
caminhow = os.path.join(downloads_dir, 'game_Wmusic.wav')  ##esse arquivo se chamará game-Wmusic e estará em formato wav

# Faz o download da winner music
gdown.download(url, caminhow, quiet=False)

# URL do arquivo MP3 no Google Drive (link de download direto) - caso de derrota
url = 'https://drive.google.com/uc?export=download&id=1YLl-D0LQkY3qcWtPA780CXriHnQYA9kQ'

#Local onde o arquivo será guardado na pasta de downloads do jogador
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads') ##irei armazenar o arquivo na pasta download do jogador
caminhol = os.path.join(downloads_dir, 'game_Lmusic.wav')  ##esse arquivo se chamará game_Lmusic e estará em formato wav

 ##faz o download da musiquinha da derrota
gdown.download(url, caminhol, quiet=False)

# Loop Principal do jogo:
while True:
    screen.fill(BLACK)  # Preenche a tela com a cor preta

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  # Verifica se o evento é o de fechar a janela
            pygame.quit()  # Finaliza o Pygame
            sys.exit()  # Sai do programa

    keys = pygame.key.get_pressed()  # Obtém as teclas pressionadas pelo jogador

    # Movimentação da bola
    if keys[pygame.K_LEFT] and ball.rect.left > 0:  # Verifica se a tecla esquerda está pressionada e se a bola não está na borda esquerda
        ball.rect.x -= ball.speed  # Move a bola para a esquerda
        player_x -= ball.speed  # Atualiza a posição do jogador
    if keys[pygame.K_RIGHT] and ball.rect.right < WIDTH:  # Verifica se a tecla direita está pressionada e se a bola não está na borda direita
        ball.rect.x += ball.speed  # Move a bola para a direita
        player_x += ball.speed  # Atualiza a posição do jogador

    # Criação dos objetos que caem
    if random.randint(0, 100) < 2:  # Gera um número aleatório para decidir se um objeto deve ser criado
        falling_object = FallingObject(player_x)  # Cria um objeto que cai na posição atual do jogador
        falling_objects_group.add(falling_object)  # Adiciona o objeto ao grupo de objetos que caem

    # Atualização e verificação dos objetos que caem
    for obj in falling_objects_group:
        pygame.draw.rect(screen, WHITE, obj.rect)  # Desenha o objeto que cai na tela
        obj.update()  # Atualiza a posição do objeto que cai

        # Verifica se houve colisão entre o objeto que cai e o fantasma. Caso ocorra o jogo encerra
        if obj.rect.colliderect(ball.rect):
            # Mostra a mensagem de derrota na tela
            screen.fill(BLACK)  # Preenche a tela com a cor preta
            font = pygame.font.Font(None, 36)  # Define a fonte do texto
            text = font.render("Você perdeu!", True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect) #desenha o texto de derrota na tela
            pygame.mixer.music.load(caminhol)
            pygame.mixer.music.play()
            pygame.display.flip()  # Atualiza a tela
            pygame.time.wait(5000)  # Aguarda 5 segundos encerra
            pygame.quit() 
            sys.exit()  

        # Verifica se o objeto que cai ultrapassou a tela
        if obj.rect.y > HEIGHT:
            obj.kill()  # Remove o objeto que cai do grupo

    # Desenha a bola na tela
    pygame.draw.circle(screen, WHITE, (ball.rect.centerx, ball.rect.centery - 15), 5)  # Desenha o olho esquerdo da bola
    pygame.draw.circle(screen, WHITE, (ball.rect.centerx + 20, ball.rect.centery - 15), 5)  # Desenha o olho direito da bola

    ball_group.draw(screen)  # Desenha a bola na tela
    ball_group.update()  # Atualiza a posição da bola

    # Contagem regressiva do tempo
    time -= 1  # Decrementa o tempo restante do jogo
    if time <= 0:  # Verifica se o tempo acabou
        # Mostra a mensagem de vitória na tela
        screen.fill(BLACK)  
        font = pygame.font.Font(None, 36) 
        text = font.render("Você venceu!", True, WHITE) 
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Define a posição do texto no centro da tela
        screen.blit(text, text_rect)  # Desenha o texto na tela
        pygame.time.wait(1000)  # Aguarda 1 segundos
        pygame.mixer.music.load(caminhow)
        pygame.mixer.music.play()  ##aqui é dado o play na musiquinha da vitória
        pygame.display.flip()  # Atualiza a tela
        pygame.time.wait(10000)  # Aguarda 10 segundos
        pygame.quit()
        sys.exit() 

    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Limita o jogo a 60 FPS
