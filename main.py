from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument('--start-fullscreen')
options.add_argument('disable-infobars')
options.add_argument('--disable-web-security')
options.add_argument('--disable-site-isolation-trials')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get('https://www.arealme.com/typing-test/zh/')
time.sleep(2)
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='secpick2']/b[1]")))
button.click()
time.sleep(1)
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='start']")))
button.click()
time.sleep(2)

def find_word():
    try:
        word_element = driver.find_element(By.XPATH, '//*[@id="typingSpeedTest"]/div[2]/div[2]/div/div[1]')
        word = word_element.text
        return word
    except Exception as e:
        print(f"Error finding word: {e}")
        return ""

def simulate_typing(char):
    try:
        script = """
        var inputField = document.querySelector('.input-editable');
        var event = new InputEvent('input', {{ bubbles: true }});
        inputField.textContent += '{}';
        inputField.dispatchEvent(event);
        """.format(char)
        driver.execute_script(script)
    except Exception as e:
        print(f"Error simulating typing: {e}")

script = """
document.addEventListener('keydown', function(event) {
    event.preventDefault();
    window.keyPressed = event.key;
});
"""

driver.execute_script(script)

while True:
    try:
        word = find_word()
        if word:
            for char in word:
                while True:
                    key_pressed = driver.execute_script("return window.keyPressed;")
                    if key_pressed:
                        driver.execute_script("window.keyPressed = null;")
                        break
                simulate_typing(char)
            space_script = """
            var inputField = document.querySelector('.input-editable');
            var spaceEvent = new KeyboardEvent('keydown', { key: ' ', keyCode: 32, code: 'Space', charCode: 32 });
            inputField.dispatchEvent(spaceEvent);
            inputField.dispatchEvent(new KeyboardEvent('keyup', { key: ' ', keyCode: 32, code: 'Space', charCode: 32 }));
            """
            time.sleep(0.2)
            driver.execute_script(space_script)
    except Exception as e:
        print(f"Error in main loop: {e}")
        break
