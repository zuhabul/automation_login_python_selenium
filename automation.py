from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
import time
from pytesseract import image_to_string
from io import BytesIO
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from decouple import config


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

username=config("USERNAME")
password=config("PASSWORD")
url = config("BASE_URL")

driver.get(url)

username_box = driver.find_element(By.NAME, "phone")
password_box = driver.find_element(By.NAME, "password")
captcha_box = driver.find_element(By.NAME, "code")

#solve simple captcha
# Link to captcha image.
# image_link= driver.find_element(By.CLASS_NAME, "codeimg").get_attribute("src")

# Download and load the image
# response = requests.get(image_link)
# img = Image.open(BytesIO(response.content))

# txt = image_to_string(img, lang = 'eng')
# print(txt)
# txt = txt.split("\n")
# for i in txt:
#     i = i.strip()
#     if i != '' and len(i) > 3:
#         print(i)


# For now let's implement manually
username_box.send_keys(username)
time.sleep(2)
password_box.send_keys(password)
time.sleep(2)
#Take input of the captcha value
val = input("Enter captcha value: ")
print(val)
captcha_box.send_keys(val)


# Do your other action afterwards
# Here I'm pressing a button to take me to a page
# login_button = driver.find_element(By.CLASS_NAME, "dldl")
# time.sleep(2) # Sleep for 3 seconds
# login_button.click()
# time.sleep(3) 

# maximize with maximize_window()
# driver.maximize_window()

# wait=WebDriverWait(driver, 10)

# username=username.lower()

# driver.find_element_by_partial_link_text('Send').click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Transfer"))).click()

# wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'body > div.kapianBox > div > div:nth-child(3)'))).click()


# chk = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]')))
# ActionChains(driver).move_to_element(chk).click().perform()

# wait.until(driver.find_element_by_partial_link_text('Transfer')).click()


# Going to a specific url and put some values in the input box and keep repeating
# for x in range(300): #run for 300 times
    # driver.get('https://test.com/index.php')
    # time.sleep(3) 
    # username_box = driver.find_element(By.NAME, "userName").send_keys('akief')
    # time.sleep(3) 
    # password_box = driver.find_element(By.NAME, "amount").send_keys("0.20000")
    # time.sleep(3) 
    # submit_button = driver.find_element(By.ID, "tijiao").click()
    # WebDriverWait(driver, 20).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    # driver.switch_to.alert.accept()
    # time.sleep(300) # repeat after 5 minutes

