import pygame
import random
############################################
# 기본 초기화
pygame.init()

#화면크키

screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("nadi")
#FPS
clock = pygame.time.Clock()

####################################################

#1. 사용자 게임 초기화

#배경이미지
background = pygame.image.load("C:\\WB\\pygame_basic\\background.png")

#스프라이트 불러오기
character = pygame.image.load("C:\\WB\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width /2 - character_width/2
character_y_pos = screen_height - character_height

to_x = 0
# to_y = 0


character_speed = 0.7
enemy_speed = 5

#적
enemy = pygame.image.load("C:\\WB\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0,screen_width-enemy_width)
enemy_y_pos = 0

too_x = 0
too_y = 0

game_font = pygame.font.Font(None,40)

#시간
total_time = 20

#시작시간정보
start_ticks = pygame.time.get_ticks()


running = True
while running:
    dt = clock.tick(60)
    enemy_y_pos += enemy_speed
    if enemy_y_pos > 640:
        enemy_y_pos=0
        enemy_x_pos=random.randint(0,screen_width-enemy_width)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #창이 닫히는 이벤트가 발생하였는가

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
                
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        
            
            # elif event.key == pygame.K_UP:
            #     to_y -= character_speed
            # elif event.key == pygame.K_DOWN:
            #     to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     to_y =0
    
    character_x_pos += to_x *dt
    # character_y_pos += to_y *dt

#경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = (screen_width - character_width)

    if character_y_pos < 0:
        character_y_pos=0
    elif character_y_pos > (screen_height-character_height):
        character_y_pos = (screen_height-character_height)
    
#충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌체크

    if character_rect.colliderect(enemy_rect):
        print("GAME OVER")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))

    if total_time - elapsed_time <= 0:
        print("성공")
        running = False

    pygame.display.update() # 화면 다시 그리기



pygame.quit()