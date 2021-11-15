from random import randint
import pygame
pygame.init()
x = 400
y = 300
velocidade = 7

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Criando jogo com Python')
janela_aberta = True
larguraJanela = janela.get_width()
pxatual = 0

while janela_aberta:
    pygame.time.delay(1000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
        print(comandos)
    if comandos[pygame.K_LEFT]:
        x -= velocidade
        print(comandos)
    if comandos[pygame.K_RIGHT]:
        x += velocidade
        print(comandos)

    janela.fill((0,0,0))
    pygame.draw.circle(janela, (0, 255 ,0), (x, y), 50)


    xb = 0
    yb = 0

    for pxatual in range(0,800):
        pygame.draw.rect(janela, (randint(0, 255), randint(0, 255), randint(0, 255)), pygame.Rect(xb, yb, 8, 8))
        xb += 1

        pxatual += 1



    #pygame.draw.rect(janela, (255, 150, 100), pygame.Rect(0, 0, 60, 60))

    pygame.display.flip()

#pygame.quit()

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
