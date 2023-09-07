# import webbrowser
# url="https://play.timepass.games/48qt"
# controller=webbrowser.get()
# controller.open_new_tab(url)
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://play.timepass.games/48qt")
time.sleep(25)