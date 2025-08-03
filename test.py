import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Tester():
    def _sac(self):
        while True:
            # ⬇️ 스크롤 다운
            for _ in range(10):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1.0)
            # ⬇️ 현재 페이지의 가격 추출
            price_elements = self.driver.find_elements(By.CSS_SELECTOR, "span[class^='price_num__']")
            for elem in price_elements:
                text = elem.text.replace(",", "").replace("원", "").strip()
                if text.isdigit():
                    self.all_prices.append(int(text))
            print(f"✅ 현재까지 수집한 가격 개수: {len(self.all_prices)}")
            # ⬇️ "다음" 버튼 탐색
            try:
                next_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pagination_next__kh_cw"))
                )
                # "다음" 버튼이 비활성화되어 있는 경우 체크
                if "disabled" in next_button.get_attribute("class"):
                    print("🔚 마지막 페이지입니다.")
                    break
                # "다음" 버튼 클릭
                self.driver.execute_script("arguments[0].click();", next_button)
                print("➡️ 다음 페이지 이동")
                time.sleep(2)
            except Exception:
                print("🔚 '다음' 버튼 없음 또는 클릭 불가 → 크롤링 종료")
                break

    def _compare_prices_option(self):
        price_compare_li = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "li[data-shp-contents-id='가격비교'] > a")
            )
        )
        self.driver.execute_script("arguments[0].click();", price_compare_li)
        print("✅ 가격비교 탭 클릭 완료")

    def _ascending_prices(self):
        low_price_elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.subFilter_sort__4Q_hv[data-shp-contents-id='낮은 가격순']"))
        )
        self.driver.execute_script("arguments[0].click();", low_price_elem)
        print("✅ 낮은가격순 클릭 완료")

    def _initialize_chrome_options(self):
        self.options = uc.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--user-data-dir=./user_data")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-infobars")
        self.driver = uc.Chrome(options=self.options, version_main=138)
        self.all_prices = []
        self.keyword = 'JP5TSU837MW'
    
    def _find_exact_same_target(self):
        elements_list = list(self.driver.find_elements(By.CSS_SELECTOR, "a"))
        for item in elements_list:
            try:
                if '만 검색하기' in item.accessible_name:
                    print("✅ 타겟 찾음:", item.get_attribute("href"))
                    # JavaScript로 강제 클릭 (가려진 경우 대비)
                    self.driver.execute_script("arguments[0].click();", item)
                    break  # 이미 클릭했으니 루프 탈출
            except WebDriverException as e:
                print("⚠️ accessible_name 접근 실패:", e)

    def start(self):
        self._initialize_chrome_options()
        self.driver.get(f"https://search.shopping.naver.com/search/all?query={self.keyword}")
        try:
            self._find_exact_same_target()
            time.sleep(2)
            self._ascending_prices()
            time.sleep(2)
            self._sac()
            
        except Exception as e:
            print(e)
            with open("debug.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            self.driver.save_screenshot("fail_search.png")
            self.driver.quit()
            exit()

        self.driver.save_screenshot("final_result.png")
        print(self.all_prices)
        self.driver.quit()

if __name__ == '__main__':
    kyj = Tester()
    kyj.start()