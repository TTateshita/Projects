from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#WebDriverインスタンスを作成
service = Service(executable_path='./scraping/chromedriver.exe')
driver = webdriver.Chrome(service=service)


#URLにアクセス
target_url = 'https://www.google.co.jp/'
driver.get(target_url)

#検索ボックスを見つけてキーワードを入力し、Enterを押す
serch_box = driver.find_element(By.ID,'APjFqb')
serch_box.send_keys("スクレイピング")
serch_box.send_keys(Keys.RETURN)

#ページが読み込まれるまで待機(最大で１０秒)
wait = WebDriverWait(driver, 20)
result = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "MjjYud")))

#検索結果の一覧からタイトルとURLを所持する
elements = driver.find_elements(By.CLASS_NAME, "MjjYud")

for element in elements:
    exclusion = element.find_elements(By.CLASS_NAME, "KFFQ0c xKf9F")
    if len(exclusion) > 0:
        continue
    
    
    print(element.find_element(By.CSS_SELECTOR, "h3.LC20lb.MBeuO.DKV0Md").text)
    
    
time.sleep(10)
driver.quit()