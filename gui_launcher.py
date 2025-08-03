import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from threading import Thread
from naver_crawler import Tester

class PriceCrawlerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("네이버 쇼핑 가격 크롤러")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("상품 코드를 입력하세요:")
        layout.addWidget(self.label)

        self.input = QLineEdit()
        self.input.setPlaceholderText("예: JP5TSU837MW")
        layout.addWidget(self.input)

        self.start_button = QPushButton("크롤링 시작")
        self.start_button.clicked.connect(self.start_crawling)
        layout.addWidget(self.start_button)

        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def start_crawling(self):
        keyword = self.input.text().strip()
        if not keyword:
            self.status_label.setText("❗ 상품 코드를 입력하세요.")
            return

        self.status_label.setText("🔍 크롤링 중... 창이 열릴 수 있어요.")
        self.start_button.setEnabled(False)
        tester = Tester()
        tester.keyword = keyword
        tester.start()
        self.status_label.setText("✅ 크롤링 완료! 콘솔을 확인하세요.")

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()

    app = QApplication(sys.argv)
    gui = PriceCrawlerGUI()
    gui.show()
    sys.exit(app.exec_())
