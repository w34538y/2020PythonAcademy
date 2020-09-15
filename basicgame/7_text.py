import pygame
# 1. game 뼈대 작성 
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정 
screen_width = 480  # 가로크기 
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 
pygame.display.set_caption("### My game v.1")

# 배경이미지 불러오기 
background  = pygame.image.load("/Users/shin/Desktop/폴더/강의 자료/20-여름 계절학기 강의자료/파이썬/pyfiles/basicgame/bg.png")

# (스프라이트) 캐릭터 불러오기
character = pygame.image.load("/Users/shin/Desktop/폴더/강의 자료/20-여름 계절학기 강의자료/파이썬/pyfiles/basicgame/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
# 화면 가로의 절반 크기에 해당하는 곳에서 캐릭터의 절반만큼을 뺀 위치 
character_x_pos = (screen_width / 2) - (character_width / 2)
# 화면 세로의 절반 크기에 해당하는 곳에서 캐릭터의 절반만큼을 뺀 위치 
character_y_pos = screen_height - character_height


# 적 캐릭터 불러오기 
enemy = pygame.image.load("/Users/shin/Desktop/폴더/강의 자료/20-여름 계절학기 강의자료/파이썬/pyfiles/basicgame/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 적의 가로 크기
enemy_height = enemy_size[1] # 적의 세로 크기
# 화면 가로의 절반 크기에 해당하는 곳에서 적의 절반만큼을 뺀 위치 
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
# 화면 세로의 절반 크기에 해당하는 곳에서 적의 절반만큼을 뺀 위치 
enemy_y_pos = (screen_height/2) - (enemy_height/2)

# 이동할 좌표 
to_x = 0
to_y = 0

# fps
clock = pygame.time.Clock()

# 이동속도 
character_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 50) # 폰트 객체 정의 (폰트, 크기)

# 총 시간 
total_time = 10

# 시작 시간 정보 
start_ticks = pygame.time.get_ticks() # 현재 tick을 받아옴 

# 창이 꺼지지 않도록 이벤트 루프 대기 
running = True
while running:

    dt = clock.tick(120) # 게임 화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): # 키보드 마우스 이벤트가 발생되는지 체크
        if event.type == pygame.QUIT: # 창닫기 이벤트가 발생했는가? 
            running = False
        if event.type == pygame.KEYDOWN: # 키보드 키가 눌려졌다 
            if event.key == pygame.K_LEFT: # 왼쪽 방향키가 눌리면 왼쪽으로 5만큼 이동 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 오른쪽 방향키가 눌리면 오른쪽으로 5만큼 이동 
                to_x += character_speed
            elif event.key == pygame.K_UP: # 위쪽 방향키가 눌리면 위쪽으로 5만큼 이동 
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 아래쪽 방향키가 눌리면 아래쪽으로 5만큼 이동 
                to_y += character_speed
         
        if event.type == pygame.KEYUP: #  키보드 키를 눌렀다가 뗄때 발생하는 이벤트 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리 (화면 밖으로 나간 경우)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계값 처리 (화면 밖으로 나간 경우)
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    # 충돌 처리를 위한 캐릭터 rect 정보 (왼쪽, 오른쪽)
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 충돌 처리를 위한 캐릭터 rect 정보 (왼쪽, 오른쪽)
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 처리 
    if character_rect.colliderect(enemy_rect): # 사각형 기준으로 충돌 체크 
        print("충돌했어요.")
        running = False

    # 타이머 집어넣기 
    # 경과 시간 계산 
    elapsed_time = (pygame.time.get_ticks()  - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    # 배경화면 그리기
    #screen.fill((0,0,255)) # RGB 값으로 채움
    screen.blit(background,(0,0)) # 배경화면 이미지로 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기  
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))# 적 그리기
    screen.blit(timer, (20,10))

    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False
    
    # 게임 화면을 다시 그리기
    pygame.display.update() 

# 잠시 대기 모드 (delay())
pygame.time.delay(2000)
# pygame 종료 
pygame.quit()