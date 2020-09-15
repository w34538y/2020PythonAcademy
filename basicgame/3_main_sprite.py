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

# 창이 꺼지지 않도록 이벤트 루프 대기 
running = True
while running:
    for event in pygame.event.get(): # 키보드 마우스 이벤트가 발생되는지 체크
        if event.type == pygame.QUIT: # 창닫기 이벤트가 발생했는가? 
            running = False

    #screen.fill((0,0,255)) # RGB 값으로 채움
    screen.blit(background,(0,0))

    # 캐릭터 그리기 
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update() # 게임 화면을 다시 그리기



# pygame 종료 
pygame.quit()