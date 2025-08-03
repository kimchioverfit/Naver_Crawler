# gui_launcher.spec

from PyInstaller.utils.hooks import collect_submodules
from pathlib import Path
import sys

block_cipher = None

# 크롬 사용자 데이터 경로 (필요시)
# user_data_dir = './user_data'

a = Analysis(
    ['gui_launcher.py'],
    pathex=['.'],
    binaries=[],
    #datas=[
    #    (user_data_dir, 'user_data'),  # user_data 폴더 포함 (없으면 생략 가능)
    #],
    hiddenimports=[
        'undetected_chromedriver',
        'undetected_chromedriver.patcher',  # 중요!
    ] + collect_submodules('undetected_chromedriver'),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PriceCrawler',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # 콘솔 숨김 (GUI용)
    icon=None,      # 아이콘 추가시 'app.ico' 등으로 지정
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PriceCrawler'
)
