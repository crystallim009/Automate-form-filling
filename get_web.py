from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.by import By
import random

driver_location = r"C:\Users\thous\OneDrive\Desktop\automate\chromedriver"
driver = webdriver.Chrome(driver_location)

driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=xGm28JghaE-QAx9GPEtCwKRHWs7MeOhAueT992vUTY5UMjE0RFZBUVZFVUs2Mjk3UTRQQkhFUDFJRS4u')
_id = driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div/div/input")
# driver.implicitly_wait(10)
_id.send_keys('20000')

driver.find_element_by_xpath("//*[@id='e3']/div").click()
driver.find_element_by_xpath("//*[@id='e3']/ul/li[1]").click()

temp = driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[3]/div/div/div/input")
temp_range = random.choice(range(364, 370))
temp_range = str(temp_range/10)
temp.send_keys(temp_range)
driver.find_element_by_xpath("//*[@id='e7']/div").click()
driver.find_element_by_xpath("//*[@id='e7']/ul/li[5]").click()
driver.find_element_by_xpath("//*[@id='form-container']/div/div/div[1]/div/div[1]/div[2]/div[3]/div/button/div").click()
