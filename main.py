import pygame
import settings
import math
import sys

def grav(ObPos, ObVel, TerPos):
    ObPos = list(ObPos)
    ObVel = list(ObVel)
    G = settings.G
    dX = ObPos[0] - TerPos[0]
    dY = ObPos[1] - TerPos[1]
    dist = math.dist(ObPos, TerPos)
    TerMas = settings.terrapeso
    ObMas = settings.objetopeso
    F = G * (TerMas * ObMas) / (dist*dist)
    Fx = F * math.sin(math.atan(dX/dY))
    Fy = F * math.cos(math.atan(dX/dY))
    AccX = Fx / ObMas
    AccY = Fy / ObMas
    ObVel[0] += AccX
    ObVel[1] += AccY
    ObPos[0] += ObVel[0]
    ObPos[1] += ObVel[1]

    return ObPos, ObVel

# Inicializa o Pygame
pygame.init()

# Configurações gerais
click = False
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
        
        if evento.type == pygame.MOUSEBUTTONDOWN and click == False:
            pos = pygame.mouse.get_pos()
            if math.dist(pos, TerraConfig[0]) >= (ObjetoConfig[1] + TerraConfig[2]):
                Velocidade += 5
                ObjetoPos[0].append(pos)
                ObjetoPos[1].append((Velocidade, 0))
                click = True

    # Preencher a tela com a cor de fundo
    tela.fill(cor_fundo)

    # Desenhar objetos
    pygame.draw.circle(tela, TerraConfig[1], TerraConfig[0], TerraConfig[2])
    
    # Verificar último objeto
    if len(ObjetoPos[0]) > 0:
        pygame.draw.circle(tela, ObjetoConfig[0], ObjetoPos[0][-1], ObjetoConfig[1])
        ObjetoPos [0][-1], ObjetoPos[1][-1] = grav(ObjetoPos[0][-1], ObjetoPos[1][-1], TerraConfig[0])

    # Atualizar a tela
    pygame.display.update()

    # Definir FPS (quadros por segundo)
    clock.tick(fps)