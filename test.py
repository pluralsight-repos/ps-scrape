from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\WebDrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
