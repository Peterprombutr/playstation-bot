from subprocess import check_output
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

PRODUCT = "https://www.bnn.in.th/en/p/gaming-gear/playstation/playstation-1/sony-playstation-5-digital-edition-4948872414999_dmj01d"
# PRODUCT = "https://www.bnn.in.th/en/p/it-accessories/logitech-gaming-keyboard-league-of-legends-edition-097855170774_d4x144" #test
USERNAME = ""
PASSWORD = ""


def click_button(button_text):
    try:
        element = driver.find_element(By.XPATH, button_text)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        return True
    except NoSuchElementException:
        return False

def login_mms(username, password):
    driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div[2]/div/div[2]/div/form/div[1]/input').send_keys(username)
    driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div[2]/div/div[2]/div/form/div[2]/div/input').send_keys(password)
    driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div[2]/div/div[2]/div/form/button').click()
    time.sleep(3)

#open web browser
driver = webdriver.Chrome()
driver.get(PRODUCT)

#close
driver.find_element(By.XPATH, f'//*[@id="close-button-1545222288830"]').click()

BUY = f'//*[@id="__layout"]/div/main/section/div[1]/div[2]/div[4]/div[2]/div[2]/button'
CHECKOUT = f'//*[@id="__layout"]/div/main/div/div/div/section[2]/div/div[2]/div/button'
while True:
    #buy
    click_button(BUY)
    if click_button(CHECKOUT):
        break
    driver.refresh()

#check out
# driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div/div/section[2]/div/div[2]/div/button').click()
login_mms(USERNAME, PASSWORD)
time.sleep(3)
driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div/div/section[2]/div/div[2]/div/button').click()
time.sleep(3)

#delivery 
driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/div/div[2]/div/div/section[1]/div[1]/div[2]/div/div/div/div[1]/div/div[1]/label/span[1]').click()

time.sleep(2)
driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/main/div/div[2]/div/div/section[1]/div[1]/div[2]/div/div/div/div[3]/section[4]/div/div/div[2]/label/span[1]').click()
time.sleep(2)

#click countinue to payment 
driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div[2]/div/div/section[1]/div[1]/div[2]/div/div/div/div[5]/div/button').click()
time.sleep(3)
#select payment 
driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div[2]/div/div/section[1]/div[2]/div[2]/div/div/div/div[4]/button/div[1]/label/span[1]').click()
#tick consent
driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div[2]/div/div/section[1]/div[2]/div[2]/div/div/div/div[9]/label/span[1]').click()
#select review order
driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div[2]/div/div/section[1]/div[2]/div[2]/div/div/div/div[10]/div/button').click()
time.sleep(2)
#place order 
driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/main/div/div[2]/div/div/section[2]/div[2]/div[2]/div/button').click()