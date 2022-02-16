from selenium import webdriver
import time

from password import login, password, image_path

# Opens an Edge browser
browser = webdriver.Edge('msedgedriver.exe')

def open_insta():  
    # Open Instagram
        time.sleep(10)
        browser.get('https://www.instagram.com/')


def login_insta():
    # This function log in Instagram an send you to the first page
    # Login  
    user_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
    password_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
    button_xpath = '//*[@id="loginForm"]/div/div[3]/button/div'
    time.sleep(2)
    browser.find_element_by_xpath(user_xpath).send_keys(login)
    time.sleep(2)
    browser.find_element_by_xpath(password_xpath).send_keys(password)
    time.sleep(3)
    browser.find_element_by_xpath(button_xpath).click()

    # "Save your login info" click in "Not now"
    button_xpath = '/html/body/div[1]/section/main/div/div/div/div/button'
    time.sleep(2)
    browser.find_element_by_xpath(button_xpath).click()
    
    # "Turn on Notifications" click in "Not Now"
    button_xpath = '/html/body/div[5]/div/div/div/div[3]/button[2]'
    time.sleep(2)
    browser.find_element_by_xpath(button_xpath).click()
    

def create_new_post():
    # Click on "Create new post"
    button_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div'
    time.sleep(3)
    browser.find_element_by_xpath(button_xpath).click()
    
    # Send the image
    form_xpath = '/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input'
    time.sleep(3)
    browser.find_elements_by_xpath(form_xpath)[0].send_keys(image_path)

    # Click on "Next"
    time.sleep(2)
    button_xpath = '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button'
    browser.find_element_by_xpath(button_xpath).click()

    # Click on "Next"
    time.sleep(2)
    button_xpath = '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button'
    browser.find_element_by_xpath(button_xpath).click()

    # Write the captions
    textarea_parh = '/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea'
    captions =  'Teclado de computador'
    time.sleep(1.8)
    browser.find_element_by_xpath(textarea_parh).click()
    time.sleep(0.5)
    browser.find_element_by_xpath(textarea_parh).send_keys(captions)

    # Click on "Share"
    button_xpath = '/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button'
    time.sleep(2)
    browser.find_element_by_xpath(button_xpath).click()
    
    # Click on the X
    button_xpath = '/html/body/div[6]/div[1]/button'
    time.sleep(10)
    browser.find_element_by_xpath(button_xpath).click()
    
    
def logout_insta():
    # Click on the X
    button_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img'
    time.sleep(2)
    browser.find_element_by_xpath(button_xpath).click()

    # Click on Logout
    button_xpath = '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div'
    time.sleep(2)
    browser.find_element_by_xpath(button_xpath).click()

    # Close the browser
    time.sleep(2)
    browser.quit()
