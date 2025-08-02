import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 옵션 설정
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")

# 크롬 실행
driver = uc.Chrome(options=options, version_main=138)

# ▶ 1. 네이버 쇼핑 홈 접속
driver.get("https://shopping.naver.com/ns/home")
time.sleep(2)

# ▶ 2. 검색창 입력 및 RETURN
try:
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='상품명 또는 브랜드 입력'][type='text']")
        )
    )
    search_box.send_keys("RTX4060")
    search_box.send_keys(Keys.RETURN)
    print("✅ 검색어 입력 완료")

    WebDriverWait(driver, 10).until(
        lambda d: "search" in d.current_url
    )

    print(f"🔄 URL 변경 감지됨: {driver.current_url}")
    driver.get("https://search.shopping.naver.com/search/all?query=RTX4060")

    low_price_elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.subFilter_sort__4Q_hv[data-shp-contents-id='낮은 가격순']"))
    )
    
    driver.execute_script("arguments[0].click();", low_price_elem)

    time.sleep(2)


###
    from selenium.webdriver.common.by import By
    import time

    # ▶ 3. 스크롤 반복
    SCROLL_PAUSE_TIME = 1.0
    scroll_count = 10  # 몇 번 스크롤할지

    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

    # ▶ 4. 가격 정보 추출
    price_elements = driver.find_elements(By.CSS_SELECTOR, "span[class^='price_num__']")
    prices = []

    for elem in price_elements:
        text = elem.text.replace(",", "").replace("원", "").strip()
        if text.isdigit():
            prices.append(int(text))

    print(f"✅ 총 가격 수집: {len(prices)}개")
    print(prices)



except Exception as e:
    print("❌ 검색창 또는 URL 전환 실패:", e)
    print(e)
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    driver.save_screenshot("fail_search.png")
    driver.quit()
    exit()


# ▶ 7. 결과 스크린샷
driver.save_screenshot("final_result.png")
input('dddd')
driver.quit()
