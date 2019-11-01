#Automated fb messaging bot for my groupchat with my friends
#source: https://www.guru99.com/selenium-python.html
#        https://stackoverflow.com/questions/51520/how-to-get-an-absolute-file-path-in-python
#        https://selenium-python.readthedocs.io/locating-elements.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import os

if __name__ == "__main__":

  username = ""                                                             #Input your messenger username as a string here
  password = ""                                                             #Input your messenger password as a string here

  driver = webdriver.Chrome(executable_path = "./chromedriver2")            #Initialize the webddriver
  driver.get("https://www.messenger.com")                                   #It directs your driver to this url
  time.sleep(5)                                                             #This waits for the page to load although it depends on your bandwidth
  element = driver.find_element_by_id("email")                              #This looks for the webpage element to which your username will be inputted
  element.send_keys(username)
  element = driver.find_element_by_id("pass")                               #This looks for the webpage element to which your password will be inputted
  element.send_keys(password)
  element.send_keys(Keys.RETURN)                                            #This emulates a return key input by the user

  #For my groupchat
  target_person = "https://www.messenger.com/t/2115558525138272"            #Enter the chat url you want to send a photo or message to
  photo = "bfast.jpg"                                                       #The name of the photo you want to upload

  driver.get(target_person)

  actions = ActionChains(driver)
  actions.send_keys("Good morning, humans!")
  actions.send_keys(Keys.RETURN)

  elements = driver.find_elements_by_name("attachment[]")
  elements[len(elements)-1].send_keys(os.path.abspath(photo))
  actions.send_keys(Keys.RETURN)
  actions.perform()
  actions.reset_actions()


  #For my girl
  target_person = ""
  photo = "me.jpg"

  driver.get(target_person)
  actions = ActionChains(driver)
  actions.send_keys("Hello there!")
  actions.send_keys(Keys.RETURN)

  elements = driver.find_elements_by_name("attachment[]")
  elements[len(elements)-1].send_keys(os.path.abspath(photo))
  actions.send_keys(Keys.RETURN)
  actions.perform()
  reset_actions()
