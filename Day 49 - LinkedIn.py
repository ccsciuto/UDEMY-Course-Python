from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/home")
sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()
username = driver.find_element(By.NAME, value="session_key")
username.send_keys("")
password = driver.find_element(By.NAME, value="session_password")
password.send_keys("")
sign_in_button = driver.find_element(By.CSS_SELECTOR, value="#organic-div > form > div.login__form_action_container > button")
sign_in_button.click()
jobs = driver.find_element(By.CSS_SELECTOR, value="#global-nav > div > nav > ul > li:nth-child(3) > a")
jobs.click()
job_search = driver.find_element(By.CSS_SELECTOR, "input.'jobs-search-box-keyword-id-ember')]")