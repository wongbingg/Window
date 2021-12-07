import pygame 

pygame.init()

#화면크키

screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nadi")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #창이 닫히는 이벤트가 발생하였는가

pygame.quit()