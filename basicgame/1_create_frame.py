import pygame 
# 1. game 뼈대 작성
pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정 
screen_width = 480 # 가로크기 
screen_height = 640 # 세로크기 
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 
pygame.display.set_caption("### My Game V.1")

# 창이 꺼지지 않도록 이벤트 루프 대기 
running = True
while running:
    for event in pygame.event.get(): # 키보드, 마우스 이벤트가 발생되는지 체크 
        if event.type == pygame.QUIT: # 창닫기 이벤트 발생했는가? 
            running = False


# pygame 종료 
pygame.quit()