# FileName: batch_install.py
# Brief: Python3 script for automating batch install/upgrade libraries.
# Author: Qing Yu
# CreateDate: 2020.10.04
# Functions:
#   - install libraries
#   - upgrade libraries

import os

LIBS = (
    "pip",
    "setuptools",
    "wheel",

    "numpy",
    "matplotlib",
    "scipy",
    "pandas",
    "pillow",  # PIL

    "pyinstaller",
    "pygame",
    "pyautogui",
    "pyserial",  # serial

    "wordcloud",
    "jieba",

    "requests",
    "beautifulsoup4",  # bs4

    "opencv-python",  # cv2, version conflict with easyocr

    "tensorflow",

    "jupyter",

    "autopep8",

    "colorama",

    "pyside6",  # PySide6
    "pyqt6",  # PyQt6

    "graph-tools",

    "objprint",
    "viztracer",

    "django",
    "djlint",
)

if __name__ == '__main__':
    for i in range(len(LIBS)):
        print(f"({i + 1}/{len(LIBS)}) Start install/upgrade {LIBS[i]}")
        os.system("python -m pip install --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple/ " + LIBS[i])
        print()

    print(f"A total of {len(LIBS)} libraries have been installed/upgraded.")
    input()
