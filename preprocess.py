import undetected_chromedriver as uc
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def main():
    options = uc.ChromeOptions()
    options.add_argument("--user-data-dir=./user_data")
    driver = uc.Chrome(options=options, version_main=138)
    driver.get("https://shopping.naver.com")
    input("✅ 네이버에 로그인하고 엔터를 누르세요.")
    
if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()