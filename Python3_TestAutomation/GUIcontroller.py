import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import sys
import os
import subprocess
import time


win_xpos = 200
win_ypos = 200
win_width = 1000
win_height = 800
app = QApplication(sys.argv)
win = QMainWindow()
win.setFixedSize(800, 600)
win.setWindowTitle("TestAutomation")
output_list = [".", ".", "."]


def heading(text, pos_x, pos_y, size_x, size_y, font_size):
    heading = QtWidgets.QLabel(win)
    heading.setText(str(text))
    heading.resize(size_x, size_y)
    heading.move(pos_x, pos_y)
    heading.setStyleSheet(
        "background-color: #fff; "
        "font-size: " + str(font_size) + "pt;"
        "font-weight: 1200;"
        "border: 8px solid #3d9dc0;"
        "border-radius: 50%;"
        "padding: 10px;"
    )


def label(text, pos_x, pos_y, size_x, size_y, font_size, color):
    label = QtWidgets.QLabel(win)
    label.setText(str(text))
    label.resize(size_x, size_y)
    label.move(pos_x, pos_y)
    label.update()
    label.setStyleSheet("font-size: " + str(font_size) + "pt;"
                        "font-weight: 900;"
                        f"color: {color};")


def panel(hex_color, pos_x, pos_y, size_x, size_y):
    panel = QtWidgets.QLabel(win)
    panel.resize(size_x, size_y)
    panel.move(pos_x, pos_y)
    panel.setStyleSheet("background-color: "+str(hex_color)+";")


def button(text, pos_x, pos_y, size_x, size_y, function):
    button = QtWidgets.QPushButton(win)
    button.setText(str(text))
    button.move(pos_x, pos_y)
    button.resize(size_x, size_y)
    button.clicked.connect(function)
    button.setStyleSheet("background-Color: #ffffff;"
                         "font-weight: 655;"
                         "font-size: 10pt;"
                         "font-family: Arial, Helvetica, sans-serif;")


def show_window():
    win.show()
    sys.exit(app.exec_())


def image_curved(path, pos_x, pos_y, size_x, size_y):
    img = QtWidgets.QLabel(win)
    pixmap = QPixmap(path)
    img.setPixmap(pixmap)
    img.move(pos_x, pos_y)
    img.resize(size_x, size_y)
    img.setStyleSheet("background-color: #fff;"
                      "border: 2px solid #ddd;"
                      "border-radius: 50%;"
                      "padding: 20px;"
                      "width: 150px;")


def output_box(path, pos_x, pos_y, size_x, size_y):
    img = QtWidgets.QLabel(win)
    pixmap = QPixmap(path)
    img.setPixmap(pixmap)
    img.move(pos_x, pos_y)
    img.resize(size_x, size_y)
    img.setStyleSheet("background-color: #fff;"
                      "border: 2px solid #ddd;"
                      "border-radius: 50%;"
                      "border: 8px solid #3d9dc0;"
                      "padding: 20px;"
                      "width: 150px;")


def image(path, pos_x, pos_y, size_x, size_y):
    img = QtWidgets.QLabel(win)
    pixmap = QPixmap(path)
    img.setPixmap(pixmap)
    img.move(pos_x, pos_y)
    img.resize(size_x, size_y)
    img.setStyleSheet("background-color: #fff;"
                      "width: 50px;")


def base_dataset_main():
    os.system('python 1.1mainMenuButtonsBase.py')
    output_list.insert(0, "Finished")


def test_dataset_main():
    os.system('python 1.2mainMenuButtonsTest.py')
    output_list.insert(0, "Finished")


def diff_dataset_main():
    os.system('python 1.3mainMenuButtonsDiff.py')
    output_list.insert(0, "Finished")


def show_user_base():
    subprocess.Popen(r'explorer /select,"screenShots\mainMenuButtonsBase\base1000000.png"')


def show_user_test():
    subprocess.Popen(r'explorer /select,"screenShots\mainMenuButtonsTest\test1000000.png"')


def show_user_diff():
    subprocess.Popen(r'explorer /select,"Results\MainButtonsDiff\b.Fail_21a.png"')


def refresh_ui():
    label1.setText(output_list[0])
    label2.setText(output_list[1])
    label3.setText(output_list[2])

    if len(output_list) > 4:
        output_list.pop(4)

    print(output_list)
    win.show()


while True:

    image("img/background1.png", 0, 0, 1000, 1000)

    heading("    \n"
            "     Test Automation Program", -45, -55, 650, 140, 25)

    label("Info: this is an auto tester that uses simple screenshots and comparisons to  \n"
          "check whether the base image is the same as the new tested state. This also  \n"
          "highlights the differences and at which point they break.", 15, 105, 920, 80, 14, "#fff")

    button("Collect Base Dataset",  80, 200, 160, 50, base_dataset_main)
    button("Collect Test Dataset", 330, 200, 160, 50, test_dataset_main)
    button("Calculate Differences",580, 200, 160, 50, diff_dataset_main)

    image_curved("img/file1.png",  80, 260, 160, 150)
    image_curved("img/file1.png", 330, 260, 160, 150)
    image_curved("img/file1.png", 580, 260, 160, 150)

    button("Show Base Dataset",  80, 420, 160, 50, show_user_base)
    button("Show Test Dataset", 330, 420, 160, 50, show_user_test)
    button("Show Differences",  580, 420, 160, 50, show_user_diff)

    # label("Output:", 45, 470, 920, 75, 14)

    output_box("img/output_box.png", 195, 500, 700, 220)

    label1 = QtWidgets.QLabel(win)
    label1.setText(output_list[0])
    label1.resize(80, 20)
    label1.move(245, 515)
    label1.setStyleSheet("font-size: " + str(10) + "pt;"
                                                   "font-weight: 900;"
                                                   "color: #cccccc;")

    label2 = QtWidgets.QLabel(win)
    label2.setText(output_list[1])
    label2.resize(80, 20)
    label2.move(245, 537)
    label2.setStyleSheet("font-size: " + str(10) + "pt;"
                                                   "font-weight: 900;"
                                                   "color: #cccccc;")

    label3 = QtWidgets.QLabel(win)
    label3.setText(output_list[2])
    label3.resize(80, 20)
    label3.move(245, 559)
    label3.setStyleSheet("font-size: " + str(10) + "pt;"
                                                   "font-weight: 900;"
                                                   "color: #cccccc;")

    timer = QTimer()
    timer.timeout.connect(refresh_ui)
    timer.start(1000)

    show_window()











