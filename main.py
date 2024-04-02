from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from progress.spinner import Spinner
from selenium import webdriver
from ctypes import windll
import subprocess
import pyautogui
import random
import time
import sys
import os

def LOGO():
    print("""
        ████████╗██╗░░░██╗██████╗░██╗███╗░░██╗░██████╗░░░░░░░████████╗███████╗░██████╗████████╗
        ╚══██╔══╝╚██╗░██╔╝██╔══██╗██║████╗░██║██╔════╝░░░░░░░╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
        ░░░██║░░░░╚████╔╝░██████╔╝██║██╔██╗██║██║░░██╗░█████╗░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
        ░░░██║░░░░░╚██╔╝░░██╔═══╝░██║██║╚████║██║░░╚██╗╚════╝░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
        ░░░██║░░░░░░██║░░░██║░░░░░██║██║░╚███║╚██████╔╝░░░░░░░░░██║░░░███████╗██████╔╝░░░██║░░░
        ░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░
        
                 ░█████╗░██╗░░██╗███████╗░█████╗░████████╗██╗███╗░░██╗░██████╗░
                 ██╔══██╗██║░░██║██╔════╝██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░
                 ██║░░╚═╝███████║█████╗░░███████║░░░██║░░░██║██╔██╗██║██║░░██╗░
                 ██║░░██╗██╔══██║██╔══╝░░██╔══██║░░░██║░░░██║██║╚████║██║░░╚██╗
                 ╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝
                 ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░""")
    
    
LOGO()
data = input("---------------------""\n"
             "模式:""\n"
             "---------------------""\n"
             "(1)預測速度""\n"
             "(2)直接修改結果數字""\n"
             "---------------------""\n"
             ":")

data = int(data) 
os.system("cls")
LOGO()
if data == 1:
    data = input("---------------------""\n"
             "速度:每分鐘/字母""\n"
             "---------------------""\n"
             "(1)70-80""\n"
             "(2)80-90""\n"
             "(3)90-100""\n"
             "(4)100-110""\n"
             "(5)110-120""\n"
             "(0)測試用選項""\n"
             "---------------------""\n"
             ":")

    data = int(data) 
    if data == 1:
        time_value = 0.44
    elif data == 2:
        time_value = 0.39
    elif data == 3:
        time_value = 0.34
    elif data == 4:
        time_value = 0.29
    elif data == 5:
        time_value = 0.24
    elif data == 0:
        time_value = 0

elif data == 2:
    data_1 = input("每分鐘單字(推薦量:18-30)""\n"":")#//*[@id="wordsPerMin"]
    data_2 = input("每分鐘字母(推薦量:80-125)""\n"":")#//*[@id="charsPerMin"]
    data_3 = input("精準度(推薦量:65-80)""\n"":")#//*[@id="accuracyPerMin"]
    time_value = 0

options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--start-fullscreen')
options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=options)

driver.get('https://www.arealme.com/typing-test/zh/')
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"secpick2\"]/b[1]")))
button.click()
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"start\"]")))
button.click()
time.sleep(2)

def space():
    time.sleep(time_value)
    pyautogui.press('space')
    word = find_word()
    return word

def Random_input():
    random_char = random.choice("abcdefghijklmnopqrstuvwxyz")
    pyautogui.typewrite(random_char)
    time.sleep(0.1)
    space()

def find_word():
    word_element = driver.find_element(By.XPATH,'//*[@id="typingSpeedTest"]/div[2]/div[2]/div/div[1]')
    word = word_element.text
    return word

while True:
    try:
        word = find_word()
        space_open = 0
        random_open = 0
        if random.randint(1,6) == 1:
            random_open = 1
            
        for char in word:
            time.sleep(time_value)
            pyautogui.typewrite(char)
            if random_open == 1:
                Random_input()
                space_open = 1
                break
        if space_open == 0:
            space()
    except:
        if data == 2:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"wordsPerMin\"]")))
            driver.execute_script(f"arguments[0].innerHTML = '{data_1}';", element)
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"charsPerMin\"]")))
            driver.execute_script(f"arguments[0].innerHTML = '{data_2}';", element)
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"accuracyPerMin\"]")))
            driver.execute_script(f"arguments[0].innerHTML = '{data_3}%';", element)
        pass