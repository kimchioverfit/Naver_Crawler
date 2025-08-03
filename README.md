# 🛍️ 네이버 쇼핑 가격 크롤러 GUI

PyQt5 GUI 기반으로 동작하는 네이버 쇼핑 가격 수집기입니다.  
`undetected-chromedriver`와 `Selenium`을 활용해 네이버의 크롤링 차단을 우회하고, 원하는 상품의 가격 정보를 손쉽게 수집할 수 있습니다.

---

## 📌 주요 기능

- 상품 코드 입력만으로 네이버 쇼핑 검색 자동 실행
- 자동으로 가격 비교 탭 이동 및 낮은 가격순 정렬
- 페이지를 자동 스크롤 및 넘기며 가격 정보 수집
- PyQt5 GUI를 통한 직관적인 사용 방식
- 콘솔에 실시간 진행 로그 출력

---
## 실행 전 준비 

### 1️⃣ 필수 패키지 설치

```bash
pip install -r requirements.txt
```

현재 NAVER의 인증은 OCR check 가 아닌 사용자의 로그인정보 쿠키를 이용합니다. 

쿠키 이용해서 인증 과정을 스킵하시려면 

```bash
pyinstaller preprocessor.spec
```
실행파일로 쿠키 저장 후 아래의 네이버 크롤러를 이용해주세요. 

또는 

```bash
python3 preprocess.py
```

이용하여 쿠키 저장 후 사용해주세요.

---
## 📸 실행 예시

```
상품 코드를 입력하세요: JP5TSU837MW
🔍 크롤링 중... 창이 열릴 수 있어요.
✅ 크롤링 완료! 콘솔을 확인하세요.
```

---

## 🛠️ 설치 및 실행 방법

### Crawler 실행

```bash
python gui_launcher.py
```

또는 아래와 같이 exe 생성 후 이용하시기 바랍니다.

```bash
pyinstaller naver_crawler.spec
```

### 크롬 창 무한 생성 방지

- PyInstaller 빌드시 반드시 `multiprocessing.freeze_support()`가 있어야 합니다.
- `undetected-chromedriver`는 내부적으로 재실행 로직이 있어 `.exe` 환경에서 무한 반복될 수 있습니다.

---

## 📁 프로젝트 구조

```
project-root/
├── gui_launcher.py               # PyQt GUI 실행 파일
├── naver_crawler.py      # 크롤링 로직 클래스
├── requirements.txt      # 의존 패키지 목록
├── README.md             # 설명 문서
└── user_data/            # 크롬 사용자 세션 정보 저장 경로
```

---

## 📈 향후 개선 예정

- 가격 결과 CSV 저장 기능
- 가격 분포 시각화 기능 (히스토그램 등)
- 비동기 처리 개선 (QThread 사용)
- 크롬 headless 옵션 추가 설정

---

## 👨‍💻 개발자 정보

**Patrick Kim (김영준)**  
📧 email: [god102104@gmail.com]  
🔗 GitHub: [https://github.com/kimchioverfit)

---

## 🧾 라이선스

MIT License
