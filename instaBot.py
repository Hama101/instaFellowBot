from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time
import facebookInfos as f


PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")
driver.maximize_window()

#sleep method
def sleep( seconds ):
    time.sleep(seconds)

#log to facebook function
def FacebookLog ():
    print("Logging in to faceBook")
    username = driver.find_element_by_id("email")
    username.send_keys(f.info["user"])

    password = driver.find_element_by_id("pass")
    password.send_keys(f.info["pass"])
    password.send_keys(Keys.RETURN)

def fellow ():
    sleep(1)
    fellowButtons = driver.find_elements_by_tag_name("button")
    sleep(1)
    personFellowed = 0
    for fellowButton in fellowButtons:
        fellowButton.click()
        personFellowed += 1
        print (f"Fellowed {personFellowed} person !")
        sleep(2)

#click on log in with faceBook
sleep(2)
logToFacebook = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[5]/button/span[2]")
logToFacebook.click()
print(f"log in clicked !")

#loging in
sleep(2)
FacebookLog()

#wait to cancel the notifcation
sleep(8)
notNow = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
notNow.click()
print("Not Now clicked!")


#get the list of the people to fellow
sleep(4)
seeMore = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[2]/div[1]/a/div")
seeMore.click()
print("See more clicked!")

while True :
    try:
        fellow()
        driver.refresh();
    except :
        input("runing to some probelms")
        break





