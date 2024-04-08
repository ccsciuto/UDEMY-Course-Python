from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--use_subprocess")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# driver.save_screenshot("screenshot.png")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cent}")
# x_path = driver.find_element(By.XPATH, value='//*[@id="productTitle"]')
# print(x_path.text)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--use_subprocess")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://disneyworld.disney.go.com/attractions/#/sort=alpha/")

name = driver.find_element(By.Link, value="Advanced Training Lab")
name.click()
driver.quit()