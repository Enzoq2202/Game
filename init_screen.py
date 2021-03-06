import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT,HEIGHT,WIDTH


def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'inicio.png')).convert()
    background_rect = background.get_rect()

    running = True
    contador = 0
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        if contador > 40:
            pygame.draw.rect(screen, BLACK, pygame.Rect(0,HEIGHT/2,WIDTH,HEIGHT/2))
            contador = 0 if contador > 50 else contador
        contador+=1 
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    dt = 0
    instrucoes = pygame.image.load(path.join(IMG_DIR, 'instrucoes.png')).convert()
    instrucoes = pygame.transform.scale(instrucoes, (WIDTH, int(HEIGHT/1.5)))
    while dt < 5000:
        t = clock.tick(FPS)
        dt+=t
        screen.fill((33,33,33))
        screen.blit(instrucoes,(0,HEIGHT/2 - instrucoes.get_height()/2))
        pygame.display.flip()
    return state
