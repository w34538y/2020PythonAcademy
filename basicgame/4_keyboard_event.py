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

# 이동할 좌표 
to_x = 0
to_y = 0

# 창이 꺼지지 않도록 이벤트 루프 대기 
running = True
while running:
    for event in pygame.event.get(): # 키보드 마우스 이벤트가 발생되는지 체크
        if event.type == pygame.QUIT: # 창닫기 이벤트가 발생했는가? 
            running = False
        if event.type == pygame.KEYDOWN: # 키보드 키가 눌려졌다 
            if event.key == pygame.K_LEFT: # 왼쪽 방향키가 눌리면 왼쪽으로 5만큼 이동 
                to_x -= 5
            elif event.key == pygame.K_RIGHT: # 오른쪽 방향키가 눌리면 오른쪽으로 5만큼 이동 
                to_x += 5
            elif event.key == pygame.K_UP: # 위쪽 방향키가 눌리면 위쪽으로 5만큼 이동 
                to_y -= 5
            elif event.key == pygame.K_DOWN: # 아래쪽 방향키가 눌리면 아래쪽으로 5만큼 이동 
                to_y += 5
         
        if event.type == pygame.KEYUP: #  키보드 키를 눌렀다가 뗄때 발생하는 이벤트 확인
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
    character_x_pos += to_x
    character_y_pos += to_y

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
    
    #screen.fill((0,0,255)) # RGB 값으로 채움
    screen.blit(background,(0,0))

    # 캐릭터 그리기 
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update() # 게임 화면을 다시 그리기



# pygame 종료 
pygame.quit()