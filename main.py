import pygame
import settings
import math
import sys

# Funções auxiliares

def grav(ObPos, ObVel, TerPos):
    ObPos = list(ObPos)
    ObVel = list(ObVel)
    G = settings.G
    dist = math.dist(ObPos, TerPos)
    TerMas = settings.terrapeso
    ObMas = settings.objetopeso
    F = G * (TerMas * ObMas) / (dist**2)
    AccX = ((TerPos[0] - ObPos[0]) / dist) * F
    AccY = ((TerPos[1] - ObPos[1]) / dist) * F
    ObVel[0] += AccX
    ObVel[1] += AccY
    ObPos[0] += ObVel[0]
    ObPos[1] += ObVel[1]

    return ObPos, ObVel

def desenhar(pos):
    for p in pos:
        pygame.draw.circle(tela, ObjetoConfig[0], p, ObjetoConfig[1])

# Inicializa o Pygame
pygame.init()

# Configurações gerais
clicks = 0
fps = settings.fps
largura = settings.larg
altura = settings.alt
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulado de Gravidade")

# Definição de cores (R, G, B)
cor_fundo = settings.fundo
cor_objeto = settings.objeto

# Criando os objetos
TerraConfig = [(largura / 2, altura / 2), settings.terra, min([altura/3, largura/3])]
ObjetoConfig = [settings.objeto, min([altura/50, largura/50])]
ObjetoPos = [[], []]
Velocidade = 0

# Clock para controlar FPS
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.MOUSEBUTTONDOWN and clicks == 0:
            pos = pygame.mouse.get_pos()
            if math.dist(pos, TerraConfig[0]) >= (ObjetoConfig[1] + TerraConfig[2]):
                Velocidade += 1
                ObjetoPos[0].append(pos)
                ObjetoPos[1].append((Velocidade, 0))
                clicks += 1
        elif evento.type == pygame.MOUSEBUTTONDOWN and clicks == 1:
            direc = pygame.mouse.get_pos()
            clicks += 1

    # Preencher a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenhar objetos
    pygame.draw.circle(tela, TerraConfig[1], TerraConfig[0], TerraConfig[2])
    
    # Verificar e aplicar gravidade no último objeto
    if len(ObjetoPos[0]) > 0:
        desenhar(ObjetoPos[0])
        if clicks == 2:
            ObjetoPos [0][-1], ObjetoPos[1][-1] = grav(ObjetoPos[0][-1], ObjetoPos[1][-1], TerraConfig[0])
            if math.dist(ObjetoPos[0][-1], TerraConfig[0]) <= (ObjetoConfig[1] + TerraConfig[2]):
                Velocidade += 1
                ObjetoPos[0].append(pos)
                ObjetoPos[1].append((Velocidade * (direc[0] - pos[0]) / (math.dist(pos, direc)), Velocidade * (direc[1] - pos[1]) / (math.dist(pos, direc)))) 

    # Atualizar a tela
    pygame.display.update()

    # Definir FPS (quadros por segundo)
    clock.tick(fps)