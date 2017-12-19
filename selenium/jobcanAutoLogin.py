from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.yahoo.co.jp/")

# 単一の要素を取得
driver.find_element_by_xpath("//*[@id='srchtxt']")
# このような指定方法もある
driver.find_element(By.XPATH, "//*[@id='srchtxt']")

# 複数の要素を取得する場合
driver.find_elements_by_xpath("//*[@class='srchtxt']")


actionChains = ActionChains(driver)
# テキストボックスに値を設定して、検索ボタンをクリックする
actionChains.send_keys_to_element(
    driver.find_element_by_xpath("//*[@id='srchtxt']"), "TESTETST")\
    .click(driver.find_element_by_xpath("//*[@id='srchbtn']")).perform()

# Shiftを押下しながら、abcを入力
actionChains.key_down(Keys.SHIFT)\
    .send_keys_to_element(
            driver.find_element_by_xpath("//*[@id='srchtxt']"), "abc")\
    .perform()
