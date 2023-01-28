import pygame

pygame.init() # 초기화 ( 반드시 필요 )

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("mogakso game") # 게임 제목 설정

# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("background.png")


# 캐릭터 ( 스프라이트 ) 불러오기
chitto = pygame.image.load("chitto.png")
chitto_size = chitto.get_rect().size # 이미지의 크기를 구해옴
chitto_width = chitto_size[0]  # 캐릭터의 가로 크기
chitto_height = chitto_size[1] # 캐릭터의 세로 크기
chitto_x_pos = (screen_width / 2 ) - (chitto_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
chitto_y_pos = screen_height - chitto_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도 
chractrer_speed  = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2 ) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = ( screen_height / 2 )- (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)



# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 ( 폰트, 크기)
 
# 총 시간 

total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 시작 tick 을 받아옴



# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    dt = clock.tick(120) # 게임화면의 초당 프레임 수를 설정 

# 캐릭터가 100 만크 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 몇 만큼 이동? 10만큼 ! 10 * 10 = 100
# 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 ! 5 * 20 = 100
    print("fps :" + str(clock.get_fps()))
    
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
                running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로 
                to_x -= chractrer_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로        
                to_x += chractrer_speed 
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= chractrer_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                to_y += chractrer_speed
                
        if event.type == pygame.KEYUP: # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    chitto_x_pos += to_x * dt
    chitto_y_pos += to_y * dt 
    
    # 가로 경계값 처리 
    if chitto_x_pos < 0 :
        chitto_x_pos = 0
    elif chitto_x_pos > screen_width - chitto_width :
        chitto_x_pos = screen_width - chitto_width
         
    # 세로 경계값 처리
    if chitto_y_pos < 0 :
        chitto_y_pos = 0
    elif chitto_y_pos > screen_height - chitto_height:
        chitto_y_pos =  screen_height - chitto_height
    
    # 충돌 처리를 위한 rect 정보 업데아트
    chitto_rect = chitto.get_rect()
    chitto_rect.left = chitto_x_pos
    chitto_rect.top = chitto_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos        
    
    # 충돌 체크
    
    if chitto_rect.colliderect(enemy_rect) :
        print("충돌 했어요")
        running = False

    #screen.fill((0 ,0 , 255))           
    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(chitto, (chitto_x_pos, chitto_y_pos)) # 캐릭터 그리기 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기
    
    #타이머 집어 넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks ) / 1000
    # 경과 시간 (ms) 을 1000으로 나누어서 초(s)로 표시
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True,(255,255,255))
    # 출력할 글자 , True, 글자 색상
    screen.blit(timer, (10,10))
    
    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0 :
        print('타임아웃')
        running = False 

    
    
    pygame.display.update() # 게임화면을 다시 그리기! 
# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

    
# pygame 종료
pygame.quit()