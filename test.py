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

    WebDriverWait(driver, 100).until(
        lambda d: "search" in d.current_url
    )

    print(f"🔄 URL 변경 감지됨: {driver.current_url}")
    driver.get("https://search.shopping.naver.com/search/all?query=RTX4060")

    price_compare_li = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "li[data-shp-contents-id='가격비교'] > a")
        )
    )

    driver.execute_script("arguments[0].click();", price_compare_li)
    print("✅ 가격비교 탭 클릭 완료")

    time.sleep(2)

    low_price_elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.subFilter_sort__4Q_hv[data-shp-contents-id='낮은 가격순']"))
    )
    
    driver.execute_script("arguments[0].click();", low_price_elem)
    print("✅ 낮은가격순 클릭 완료")

    time.sleep(2)

    all_prices = []

    while True:
        # ⬇️ 스크롤 다운
        for _ in range(10):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.0)

        # ⬇️ 현재 페이지의 가격 추출
        price_elements = driver.find_elements(By.CSS_SELECTOR, "span[class^='price_num__']")
        for elem in price_elements:
            text = elem.text.replace(",", "").replace("원", "").strip()
            if text.isdigit():
                all_prices.append(int(text))

        print(f"✅ 현재까지 수집한 가격 개수: {len(all_prices)}")

        # ⬇️ "다음" 버튼 탐색
        try:
            next_button = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pagination_next__kh_cw"))
            )

            # "다음" 버튼이 비활성화되어 있는 경우 체크
            if "disabled" in next_button.get_attribute("class"):
                print("🔚 마지막 페이지입니다.")
                break

            # "다음" 버튼 클릭
            driver.execute_script("arguments[0].click();", next_button)
            print("➡️ 다음 페이지 이동")
            time.sleep(2)

        except Exception:
            print("🔚 '다음' 버튼 없음 또는 클릭 불가 → 크롤링 종료")
            break


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
print(all_prices)
input('dddd')
driver.quit()
