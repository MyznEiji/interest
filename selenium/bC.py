from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://news.bitcoin.com")

driver.find_element_by_class_name("td-module-thumb")
