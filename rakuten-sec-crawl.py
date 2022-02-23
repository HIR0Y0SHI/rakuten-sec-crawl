import time, os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs


RAKUTEN_URL = 'https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html'
LOGIN_ID    = os.environ['LOGIN_ID']
LOGIN_PASS  = os.environ['LOGIN_PASS']

chrome_service = fs.Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=chrome_service)
driver.get(RAKUTEN_URL)
sleep(0.3)

# ログインフォームを取得
login_id_form   = driver.find_element(by=By.ID, value='form-login-id')
login_pass_form = driver.find_element(by=By.ID, value='form-login-pass')
login_btn       = driver.find_element(by=By.ID, value='login-btn')

# フォーム入力
login_id_form.send_keys(LOGIN_ID)
login_pass_form.send_keys(LOGIN_PASS)
sleep(0.3)

# ログイン（クリック）
login_btn.click()
sleep(0.5)

# 保有商品一覧へ遷移
asset_total_btn = driver.find_element(by=By.ID, value='asset_total_possess_btn')
asset_total_btn.click()

# 保有商品情報取得
## 資産合計
total_assets_element = driver.find_element(by=By.XPATH, value='//*[@id="table_balance_data"]/div/table/tbody/tr[2]/td[2]/span')
## 評価損益
valuation_profit_element = driver.find_element(by=By.XPATH, value='//*[@id="table_balance_data"]/div/table/tbody/tr[2]/td[3]/span[3]/span')

print("資産合計" + total_assets_element.text)
print("評価損益" + valuation_profit_element.text)



