# -*- coding: utf-8 -*-33F639
# Created by DoSun on 2017/5/20
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.uic import *
from config import *
import os
import threading
import sqlite3
import random

__version__ = '1.0'
MAX_LENGTH = 140
# SIZEOF_UINT16 = 2

UiFile = 'Quiz_window.ui'


# Ui_Quiz, QtBaseClass = loadUiType(UiFile)


class ShadowWindow(QWidget):
    def __init__(self):
        super(ShadowWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.SHADOW_WIDTH = 15

    def drawShadow(self, painter):
        painter.drawPixmap(0,
                           0,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/left_top.png'))
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH,
                           0,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/right_top.png'))
        painter.drawPixmap(0,
                           self.height() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/left_bottom.png'))
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH,
                           self.height() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/right_bottom.png'))
        painter.drawPixmap(0,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/left_mid.png').scaled(self.SHADOW_WIDTH,
                                                                       self.height() - 2 * self.SHADOW_WIDTH))
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/right_mid.png').scaled(self.SHADOW_WIDTH,
                                                                        self.height() - 2 * self.SHADOW_WIDTH))
        painter.drawPixmap(self.SHADOW_WIDTH,
                           0,
                           self.width() - 2 * self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/top_mid.png').scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                                      self.SHADOW_WIDTH))
        painter.drawPixmap(self.SHADOW_WIDTH,
                           self.height() - self.SHADOW_WIDTH,
                           self.width() - 2 * self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH,
                           QPixmap(':/shadow/img/bottom_mid.png').scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                                         self.SHADOW_WIDTH))

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)



class QuizMainWindow(Ui_Quiz, ShadowWindow):
    updateClients = pyqtSignal(str)

    def __init__(self):
        super(QuizMainWindow, self).__init__()
        self.setupUi(self)
        self.__leftButtonPress = False
        self.__movePoint = QPoint()
        self.tooMany = False
        self.connection = sqlite3.connect('dbquestions.db')
        self.cursor = self.connection.cursor()
        self.questionlimit = 0
        self.score = 0
        self.respostaCerta = ''
        self.pressButtonclicked = ''
        self.today = QDate()
        self.list = []
        self.listquest = [self.quest1,self.quest2,self.quest3,self.quest4,self.quest5,self.quest6,self.quest7,self.quest8,self.quest9]
        self.cont = 1

        self.inicializao()


    def inicializao (self):
      bottom = ['optA','optB','optC','optD']
      self.start_Game.clicked.connect(self.startgame)
      self.optA.clicked.connect(lambda: self.pressbuttom(name="questA"))
      self.questA.clicked.connect(lambda: self.pressbuttom(name="questA"))
      self.optB.clicked.connect(lambda: self.pressbuttom(name="questB"))
      self.questB.clicked.connect(lambda: self.pressbuttom(name="questB"))
      self.optC.clicked.connect(lambda: self.pressbuttom(name="questC"))
      self.questC.clicked.connect(lambda: self.pressbuttom(name="questC"))
      self.optD.clicked.connect(lambda: self.pressbuttom(name="questD"))
      self.questD.clicked.connect(lambda: self.pressbuttom(name="questD"))

      self.returnHome.clicked.connect(self.returnhome)
      self.returnHome2.clicked.connect(self.returnhome)
      self.btnInfo.clicked.connect(self.returninfo)


    def returninfo(self):
      self.centerStackedWidget.setCurrentIndex(3)

    def returnhome(self):
      self.centerStackedWidget.setCurrentIndex(0)


    def startgame(self):
      self.centerStackedWidget.setCurrentIndex(1)
      for x in range(30):
          Pnumber = random.randint(1,20)
          if Pnumber not in self.list: self.list.append(Pnumber)
      self.reloadQuestion()


    def reloadQuestion(self):
      #label contadora de questoes
      quest = "Questões: {}/10".format(self.questionlimit)
      score = "Score: {}".format(self.score)
      self.labelScore.setText(score)
      self.labelquestion.setText(quest)
      if self.cont == 11:
        self.centerStackedWidget.setCurrentIndex(2)
        self.labelScorePrint.setText(score)
        self.score = 0
        self.questionlimit = 0
        self.list = []
        self.questList = []
        self.cont = 1
        self.clearpopups()
      else:
        #numero de perguntas de 1 a 10 sao 10 perguntas existentes
        #self.list
        #pergunta = random.randint(1,10)
        self.cursor.execute('SELECT pergunta,respostaA,respostaB,respostaC,respostaD,correta From questions  WHERE id="{}"'.format(self.list[self.cont]))
        check = self.cursor.fetchall()
        self.textQuestion.setText(check[0][0])
        self.questA.setText(check[0][1])
        self.questB.setText(check[0][2])
        self.questC.setText(check[0][3])
        self.questD.setText(check[0][4])
        self.respostaCerta = check[0][5]
        self.cont += 1
        self.questionlimit += 1



    def clearpopups(self):
      for i in range(9):
          self.listquest[i].setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")


    def animationsucess(self):
      for i in range(10):
        if self.questionlimit == i:
          luz = self.questionlimit - 1
          self.listquest[luz].setStyleSheet(".QLabel\n""{\n""background:#2AEC13\n""}")

    def animationError(self):
      for i in range(10):
        if self.questionlimit == i:
          luz = self.questionlimit - 1
          self.listquest[luz].setStyleSheet(".QLabel\n""{\n""background:#ff0000\n""}")

    def pressbuttom(self, name):
        self.pressButtonclicked = name
        self.checkRespo()

    def checkRespo(self):
      if self.pressButtonclicked == self.respostaCerta:
        self.score += 25
        self.animationsucess()
        self.reloadQuestion()
      else:
        self.animationError()
        self.reloadQuestion()

    #   event mouse
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.titleBar.rect().contains(event.pos()):
                self.__leftButtonPress = True
                self.__movePoint = event.pos()

    def mouseMoveEvent(self, event):
        if self.__leftButtonPress:
            globalPos = event.globalPos()
            self.move(globalPos - self.__movePoint)

    def mouseReleaseEvent(self, event):
        self.__leftButtonPress = False

    def maxAndNormal(self):
        """maximo/minimo windows"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Quiz = QuizMainWindow()
    Quiz.show()
    app.exec_()
