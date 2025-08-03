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

## 📸 실행 예시

```
상품 코드를 입력하세요: JP5TSU837MW
🔍 크롤링 중... 창이 열릴 수 있어요.
✅ 크롤링 완료! 콘솔을 확인하세요.
```

---

## 🛠️ 설치 및 실행 방법

### 1️⃣ 필수 패키지 설치

```bash
pip install -r requirements.txt
```

또는:

```bash
pip install PyQt5 selenium undetected-chromedriver
```

### 2️⃣ GUI 실행

```bash
python main.py
```

---

## 🧊 PyInstaller로 실행 파일 만들기 (Windows용)

### `main.py` 내 필수 코드

```python
if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
```

### 빌드 명령어

```bash
pyinstaller main.py --noconfirm --onefile --windowed
```

### 크롬 창 무한 생성 방지

- PyInstaller 빌드시 반드시 `multiprocessing.freeze_support()`가 있어야 합니다.
- `undetected-chromedriver`는 내부적으로 재실행 로직이 있어 `.exe` 환경에서 무한 반복될 수 있습니다.

---

## 📁 프로젝트 구조

```
project-root/
├── main.py               # PyQt GUI 실행 파일
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
📧 email: [your_email@example.com]  
🔗 GitHub: [github.com/your_profile](https://github.com/your_profile)

---

## 🧾 라이선스

MIT License
