import pygame
import settings
import sys

# Inicializa o Pygame
pygame.init()

# Configurações gerais
fps = settings.fps
largura = settings.larg
altura = settings.alt
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulado de Gravidade")

# Definição de cores (R, G, B)
cor_fundo = settings.fundo
cor_objeto = settings.objeto

# Criando os objetos
TerraConfig = [(largura / 2, altura / 2), settings.terra, 100, min([altura/3, largura/3])]


# Clock para controlar FPS
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preencher a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenhar objetos
    pygame.draw.circle(tela, TerraConfig[1], TerraConfig[0], TerraConfig[2])

    # Atualizar a tela
    pygame.display.update()

    # Definir FPS (quadros por segundo)
    clock.tick(fps)