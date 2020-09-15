# 파이썬 마우스, 키보드 자동화 프로그램 (매크로)
# pyautogui 모듈 기초 사용법 
import pyautogui
import time
pyautogui.position()

pyautogui.moveTo(x=1989, y=288) # 이동 
# pyautogui.click(clicks=2, interval=2)
pyautogui.doubleClick()
pyautogui.moveTo(x=989, y=288) # 이동 
time.sleep(3) # 대기 시간
pyautogui.typewrite(["enter"])
pyautogui.typewrite(["h", "e", "l", "l", "o","enter"])
# pyautogui.moveRel() # 상대이동

