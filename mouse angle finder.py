import pygame
import sys
from numpy import sin, cos, arcsin, arccos, arctan, pi, mean
from random import random

pygame.init()
#screen = pygame.display.set_mode((800,600))
screen = pygame.display.set_mode()

print(screen)
#screen = pygame.display.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.event.set_grab(False)
pygame.display.toggle_fullscreen()

res = pygame.display.get_window_size()

my_font = pygame.font.SysFont('Bahnscrift', 30)

text = my_font.render('Faça movimentos APENAS horizontais com o mouse', True, (250, 0, 250))
text_exit = my_font.render('Pressione ESC para sair', True, (50,50,50))


theta_lapse = 0
cor_bola = (250,0,0)

x_cm = []
y_cm = []
ang_cm = []
len_total = 500
count_redtime = 0
angulo = 0
angtextdisplay = False



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    

    mouse_pos = pygame.mouse.get_pos()
    
    mouse_rel = pygame.mouse.get_rel() # mouse movement relative to last frame
    
    #print(f"Position: {mouse_pos}, Movement: {mouse_rel}")
    
    screen.fill((0, 0, 0))

    if not pygame.mouse.get_visible():
        pass
        #pygame.draw.circle(screen, (255, 255, 255), mouse_pos, 4)

    theta_lapse += 0.5 + 0.2*random()

    text_rect = text.get_rect(center=(res[0]/2 + 2*sin(theta_lapse/20), 1.5*cos(theta_lapse/15) + 100))
    screen.blit(text, text_rect)
    text_rect = text_exit.get_rect(center=(res[0] - 200, res[1] - 20))
    screen.blit(text_exit,text_rect)

    pygame.draw.circle(screen,(cor_bola),(res[0]/2 + 700*sin(pygame.time.get_ticks()/100), res[1]/2), 5)

    

    if abs(mouse_rel[0]) > 70:
        cor_bola = 'green'
        count_redtime = 0
        x_cm.append(mouse_pos[0]); y_cm.append(mouse_pos[1])
        angulo = arctan(mouse_rel[1]/mouse_rel[0])
        ang_cm.append(angulo)
    else:
        count_redtime += 1

    if len(ang_cm) > len_total:
        angm = mean(angulo) * 180 / pi
        angtextdisplay = True
        ang_cm.pop(0)
        x_cm.pop(0); y_cm.pop(0)

    text_angle = my_font.render(f'{round(len(ang_cm)/len_total,2)}', True, (250, 250, 250))
    text_rect = text_angle.get_rect(center=(res[0]/2, res[1] - 200))
    screen.blit(text_angle, text_rect)


    if angtextdisplay:
        text_angle_raw = f'Ângulo encontrado! {-round(angm,3)}'
        text_angle = my_font.render(text_angle_raw, True, (250, 250, 250))
        text_rect = text_angle.get_rect(center=(res[0]/2, res[1]/2 + 200))
        screen.blit(text_angle, text_rect)

    if count_redtime == 165:
        cor_bola = 'red'

    pygame.display.flip()
    clock.tick(165)

print(180*mean(ang_cm)/pi)

pygame.quit()
sys.exit()