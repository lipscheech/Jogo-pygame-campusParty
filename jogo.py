# coding: utf-8
import pygame
pygame.init()

tela = pygame.display.set_mode((700,500))

dragao = pygame.image.load('imagens/dragao.png')
cenario = pygame.image.load('imagens/cenario.png')
seta = pygame.image.load('imagens/seta.png')
fonte = pygame.font.Font(None, 60)
texto = fonte.render('#CPBSB3: ', True, (0,0,0))

rodando = True

x_inicia = -300
x = x_inicia
y = 380
y_dragao = 50
disparando = False
pontos = 0
acerto = False


while rodando:
    tela.fill([255,255,255])
    tela.blit(cenario, (0,0))
    tela.blit(dragao, (x,y_dragao))
    tela.blit(seta,(340, y))
    tela.blit(texto, (10,20))
    placar = fonte.render(str(pontos), True, (0,0,0))
    tela.blit(placar, (600,30))


    if acerto:
        y_dragao = y_dragao + 2
    if disparando:
        y = y - 5
    pygame.display.flip()

    x = x + 5

    if x > 700:
        x = x_inicia
        acerto = False
        dragao = pygame.image.load('imagens/dragao.png')
        y_dragao = 50
    if y < -200:
        y = 380
        disparando = False
        if not acerto:
            pontos = pontos - 5
    if x > 100 and x < 340 and y < 50:
        #x = x_inicia
        pontos  = pontos + 50
        if not acerto:
            acerto = True
            dragao = pygame.transform.flip(dragao, True, acerto)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            disparando = True
print(pontos)

