import undetected_chromedriver as uc
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


options = uc.ChromeOptions()
options.add_argument("--user-data-dir=./user_data")  # 사용자 데이터 저장 위치
driver = uc.Chrome(options=options, version_main=138)
driver.get("https://shopping.naver.com")
input("✅ 네이버에 로그인하고 엔터를 누르세요.")
driver.quit()
