# preprocess.spec
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['preprocess.py'],
    pathex=['.'],
    binaries=[],
    datas=[('user_data', 'user_data')],
    hiddenimports=collect_submodules('undetected_chromedriver'),
    hookspath=[],
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
    name='PreProcessor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # 디버깅 시 True로! 최종 배포 시 False
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='PreProcessor'
)
