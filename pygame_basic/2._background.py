import pygame

pygame.init()

#화면크키

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nadi")

#배경이미지
background = pygame.image.load("C:\\WB\\pygame_basic\\background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #창이 닫히는 이벤트가 발생하였는가

    screen.blit(background, (0,0))

    pygame.display.update() # 화면 다시 그리기

pygame.quit()