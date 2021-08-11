import pygame
from config import BLACK,IMG_DIR,QUIT,GAME,FPS,WIDTH,HEIGHT,FNT_DIR,YELLOW,WHITE,RED
from os import path
from pontuacao import points
import os

def game_over(window):
    clock = pygame.time.Clock()
    tela_game_over = pygame.image.load(path.join(IMG_DIR, 'game_over.jpg')).convert()
    tela_game_over = pygame.transform.scale(tela_game_over, (WIDTH, int(HEIGHT/2)))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        clock.tick(FPS)
        window.fill(BLACK)
        window.blit(tela_game_over, (-13,0))
        dic = points()
        
        text_surface = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 13).render("Pontos feitos: {:08d}".format(dic['score_atual']), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  HEIGHT/2)
        window.blit(text_surface, text_rect)
        
        for i in range(1,len(dic['recorde'])+1):

            text_surface = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 13).render(f"{i}°: {dic['recorde'][-i]:08d}", True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (WIDTH / 2,  HEIGHT/2 + 50*i)
            window.blit(text_surface, text_rect)
        
        text_surface = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 10).render(f"Aperte qualquer tecla  para jogar novamente", True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  HEIGHT - 20)
        window.blit(text_surface, text_rect)
        
        pygame.display.update()        
    return state


def gameover_efeito():
    gameover = pygame.mixer.Sound('Game/assets/snd/Music_Game_Over.ogg')
    gameover.play()
