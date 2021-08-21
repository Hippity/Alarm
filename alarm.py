from selenium import webdriver
from pyautogui import press
from time import sleep
from datetime import datetime


start=str("11:00")

while True:
    now= datetime.now()
    t=now.strftime('%H:%M')
    if t==start:
        driver = webdriver.Chrome(
            executable_path='put chromedriver path here')
        driver.get(str('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        sleep(3)
        press('space')
        break
