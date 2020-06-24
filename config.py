# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quiz_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Quiz(object):
    def setupUi(self, Quiz):
        Quiz.setObjectName("Quiz")
        Quiz.resize(650, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Quiz.sizePolicy().hasHeightForWidth())
        Quiz.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Quiz.setWindowIcon(icon)
        Quiz.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(Quiz)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QWidget(Quiz)
        self.titleBar.setMinimumSize(QtCore.QSize(0, 30))
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.titleBar.setMouseTracking(True)
        self.titleBar.setStyleSheet(".QWidget\n"
"{\n"
"background:transparent;\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background:#202020;\n"
"border:1px solid #202020;\n"
"}")
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titleBar)
        self.horizontalLayout.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_label = QtWidgets.QLabel(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setMouseTracking(True)
        self.title_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_label.setStyleSheet("background:#202020;\n"
"color:white;")
        self.title_label.setScaledContents(False)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setWordWrap(False)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.minBtn = QtWidgets.QPushButton(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minBtn.sizePolicy().hasHeightForWidth())
        self.minBtn.setSizePolicy(sizePolicy)
        self.minBtn.setMinimumSize(QtCore.QSize(18, 18))
        self.minBtn.setMaximumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.minBtn.setFont(font)
        self.minBtn.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"background-color:white;\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:white;\n"
"}")
        self.minBtn.setText("")
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout.addWidget(self.minBtn, 0, QtCore.Qt.AlignVCenter)

        self.closeBtn = QtWidgets.QPushButton(self.titleBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QtCore.QSize(18, 18))
        self.closeBtn.setMaximumSize(QtCore.QSize(18, 18))
        self.closeBtn.setStyleSheet("QPushButton\n"
"{\n"
"background: transparent;\n"
"background-color:red;\n"
"border-radius:9px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgba(255,140,140,255)\n"
"}")
        self.closeBtn.setText("")
        self.closeBtn.setIconSize(QtCore.QSize(18, 18))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout.addWidget(self.closeBtn, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout.addWidget(self.titleBar)
        self.centerStackedWidget = QtWidgets.QStackedWidget(Quiz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centerStackedWidget.sizePolicy().hasHeightForWidth())
        self.centerStackedWidget.setSizePolicy(sizePolicy)
        self.centerStackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centerStackedWidget.setStyleSheet("")
        self.centerStackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.centerStackedWidget.setObjectName("centerStackedWidget")
        self.loginPage = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginPage.sizePolicy().hasHeightForWidth())
        self.loginPage.setSizePolicy(sizePolicy)
        self.loginPage.setStyleSheet("QWidget\n"
"{\n"
"background-color:#202020;\n"
"}")
        
        self.loginPage.setObjectName("loginPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginPage)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 50)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        
        self.label = QLabel(self.loginPage) 
        self.pixmap = QPixmap('images/profile.png')
        self.label.setGeometry(QtCore.QRect(226, 100, 160, 160))
        self.label.setPixmap(self.pixmap)

        #menu de baixo da logo

        self.start_Game = QtWidgets.QPushButton(self.loginPage)
        self.start_Game.setMinimumSize(QtCore.QSize(50, 50))
        self.start_Game.setGeometry(QtCore.QRect(260, 280, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.start_Game.setFont(font)
        self.start_Game.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#202020;\n"
"border: 3px solid #e65035;\n"
"border-radius:10px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#e65035;\n"
"border: 3px solid #fff;\n"
"color: #fff\n"
"}")
        self.start_Game.setObjectName("start_Game")



#         self.btnScore = QtWidgets.QPushButton(self.loginPage)
#         self.btnScore.setMinimumSize(QtCore.QSize(50, 50))
#         self.btnScore.setGeometry(QtCore.QRect(260, 340, 100, 50))
#         font = QtGui.QFont()
#         font.setFamily("Baskerville Old Face")
#         font.setPointSize(10)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btnScore.setFont(font)
#         self.btnScore.setStyleSheet("QPushButton\n"
# "{\n"
# "background-color:#202020;\n"
# "border: 3px solid #e65035;\n"
# "border-radius:10px;\n"
# "color: #fff\n"
# "}\n"
# "QPushButton::hover\n"
# "{\n"
# "background-color:#e65035;\n"
# "border: 3px solid #fff;\n"
# "color: #fff\n"
# "}")
#         self.btnScore.setObjectName("btnScore")


        self.btnInfo = QtWidgets.QPushButton(self.loginPage)
        self.btnInfo.setMinimumSize(QtCore.QSize(50, 50))
        self.btnInfo.setGeometry(QtCore.QRect(260, 340, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnInfo.setFont(font)
        self.btnInfo.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#202020;\n"
"border: 3px solid #e65035;\n"
"border-radius:10px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#e65035;\n"
"border: 3px solid #fff;\n"
"color: #fff\n"
"}")
        self.btnInfo.setObjectName("btnInfo")

        self.verticalLayout_2.setStretch(0, 1)
        self.centerStackedWidget.addWidget(self.loginPage)
        #=======================Final da tela de principal============================#
        #=======================começo da tela do game============================#
        self.pageGame = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageGame.sizePolicy().hasHeightForWidth())
        self.pageGame.setSizePolicy(sizePolicy)
        self.pageGame.setStyleSheet("QWidget\n"
"{\n"
"background-color:#202020;\n"
"}")
        
        self.pageGame.setObjectName("pageGame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageGame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 50)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        #progressbar 
        self.quest1 = QLabel(self.pageGame) 
        self.quest1.setGeometry(QtCore.QRect(220, 40, 23, 23))
        self.quest1.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        self.quest2 = QLabel(self.pageGame) 
        self.quest2.setGeometry(QtCore.QRect(246, 40, 23, 23))
        self.quest2.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")


        self.quest3 = QLabel(self.pageGame) 
        self.quest3.setGeometry(QtCore.QRect(272, 40, 23, 23))
        self.quest3.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")


        self.quest4 = QLabel(self.pageGame) 
        self.quest4.setGeometry(QtCore.QRect(298, 40, 23, 23))
        self.quest4.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        self.quest5 = QLabel(self.pageGame) 
        self.quest5.setGeometry(QtCore.QRect(324, 40, 23, 23))
        self.quest5.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        self.quest6 = QLabel(self.pageGame) 
        self.quest6.setGeometry(QtCore.QRect(350, 40, 23, 23))
        self.quest6.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        self.quest7 = QLabel(self.pageGame) 
        self.quest7.setGeometry(QtCore.QRect(376, 40, 23, 23))
        self.quest7.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        self.quest8 = QLabel(self.pageGame) 
        self.quest8.setGeometry(QtCore.QRect(402, 40, 23, 23))
        self.quest8.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        self.quest9 = QLabel(self.pageGame) 
        self.quest9.setGeometry(QtCore.QRect(428, 40, 23, 23))
        self.quest9.setStyleSheet(".QLabel\n""{\n""background:#202020\n""}")

        #questoes processo
        self.labelquestion =  QtWidgets.QLabel(self.pageGame) 
        self.labelquestion.setGeometry(QtCore.QRect(20, 20, 170, 60))
        self.labelquestion.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelquestion.setFont(font)
        self.labelquestion.setStyleSheet(".QLabel\n"
"{\n"
"color:#FDCF24;\n"
"padding:5px;\n"
"text-align: center;\n"
"background:#202020\n"
"}")

        #questoes processo
        self.labelScore =  QtWidgets.QLabel(self.pageGame) 
        self.labelScore.setGeometry(QtCore.QRect(520, 20, 170, 60))
        self.labelScore.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelScore.setFont(font)
        self.labelScore.setStyleSheet(".QLabel\n"
"{\n"
"color:#FDCF24;\n"
"padding:5px;\n"
"text-align: center;\n"
"background:#202020\n"
"}")


        #questoes processo
        self.textQuestion =  QtWidgets.QLabel(self.pageGame) 
        self.textQuestion.setGeometry(QtCore.QRect(0, 150, 620, 80))
        self.textQuestion.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textQuestion.setFont(font)
        self.textQuestion.setStyleSheet(".QLabel\n"
"{\n"
"color:white;\n"
"padding:5px;\n"
"text-align: center;\n"
"background:#28AAF9\n"
"}")

#bolao de questao
        self.questA = QPushButton(self.pageGame) 
        self.questA.setGeometry(QtCore.QRect(78, 250, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.questA.setFont(font)
        self.questA.setStyleSheet(".QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:5px;\n"
"padding:10px;\n"
"border: solid 1px red;\n"
"background:#1D8FD5\n"
"}")



#bolao de questao
        self.questB = QPushButton(self.pageGame) 
        self.questB.setGeometry(QtCore.QRect(78, 320, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.questB.setFont(font)
        self.questB.setStyleSheet(".QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:5px;\n"
"padding:10px;\n"
"border: solid 1px red;\n"
"background:#1D8FD5\n"
"}")    

#bolao de questao
        self.questC = QPushButton(self.pageGame) 
        self.questC.setGeometry(QtCore.QRect(78, 390, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.questC.setFont(font)
        self.questC.setStyleSheet(".QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:5px;\n"
"padding:10px;\n"
"border: solid 1px red;\n"
"background:#1D8FD5\n"
"}")    


#bolao de questao
        self.questD = QPushButton(self.pageGame) 
        self.questD.setGeometry(QtCore.QRect(78, 460, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.questD.setFont(font)
        self.questD.setStyleSheet(".QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:5px;\n"
"padding:10px;\n"
"border: solid 1px red;\n"
"background:#1D8FD5\n"
"}")        

        #botoes do quiz (alternativas)

        self.optA = QtWidgets.QPushButton(self.pageGame)
        self.optA.setMinimumSize(QtCore.QSize(50, 50))
        self.optA.setGeometry(QtCore.QRect(35, 250, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.optA.setFont(font)
        self.optA.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#28AAF9;\n"
"border-radius:5px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#1D8FD5;\n"
"color: #000\n"
"}")
        self.optA.setObjectName("optA")

#bolao de questao


        self.optB = QtWidgets.QPushButton(self.pageGame)
        self.optB.setMinimumSize(QtCore.QSize(50, 50))
        self.optB.setGeometry(QtCore.QRect(35, 320, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.optB.setFont(font)
        self.optB.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#28AAF9;\n"
"border-radius:5px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#1D8FD5;\n"
"color: #000\n"
"}")
        self.optB.setObjectName("optB")


        self.optC = QtWidgets.QPushButton(self.pageGame)
        self.optC.setMinimumSize(QtCore.QSize(50, 50))
        self.optC.setGeometry(QtCore.QRect(35, 390, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.optC.setFont(font)
        self.optC.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#28AAF9;\n"
"border-radius:5px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#1D8FD5;\n"
"color: #000\n"
"}")
        self.optC.setObjectName("optC")



        self.optD = QtWidgets.QPushButton(self.pageGame)
        self.optD.setMinimumSize(QtCore.QSize(50, 50))
        self.optD.setGeometry(QtCore.QRect(35, 460, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.optD.setFont(font)
        self.optD.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#28AAF9;\n"
"border-radius:5px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#1D8FD5;\n"
"color: #000\n"
"}")
        self.optD.setObjectName("optD")
        self.centerStackedWidget.addWidget(self.pageGame)
        #=======================Final da tela de game============================#
        #=======================começo da tela do Score============================#
        self.pageScore = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageScore.sizePolicy().hasHeightForWidth())
        self.pageScore.setSizePolicy(sizePolicy)
        self.pageScore.setStyleSheet("QWidget\n"
"{\n"
"background-color:#202020;\n"
"}")
        
        self.pageScore.setObjectName("pageScore")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageScore)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 50)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        #questoes processo
        self.labelScorePrint =  QtWidgets.QLabel(self.pageScore) 
        self.labelScorePrint.setGeometry(QtCore.QRect(230, 100, 170, 60))
        self.labelScorePrint.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelScorePrint.setFont(font)
        self.labelScorePrint.setStyleSheet(".QLabel\n"
"{\n"
"color:#FDCF24;\n"
"padding:5px;\n"
"text-align: center;\n"
"background:#202020\n"
"}")

        #questoes processo
        self.labelusername =  QtWidgets.QLabel(self.pageScore) 
        self.labelusername.setGeometry(QtCore.QRect(80, 175, 170, 60))
        self.labelusername.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelusername.setFont(font)
        self.labelusername.setStyleSheet(".QLabel\n"
"{\n"
"color:#fff;\n"
"padding:5px;\n"
"text-align: center;\n"
"background:#202020\n"
"}")




        self.username = QtWidgets.QLineEdit(self.pageScore)
        self.username.setGeometry(QtCore.QRect(230, 193, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.username.setFont(font)
        self.username.setStyleSheet("background:transparent;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"padding:0 10px")
        self.username.setText("")
        self.username.setObjectName("username")


        self.returnHome2 = QtWidgets.QPushButton(self.pageScore)
        self.returnHome2.setMinimumSize(QtCore.QSize(50, 50))
        self.returnHome2.setGeometry(QtCore.QRect(260, 260, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.returnHome2.setFont(font)
        self.returnHome2.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#28AAF9;\n"
"border-radius:5px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#1D8FD5;\n"
"color: #000\n"
"}")


        self.centerStackedWidget.addWidget(self.pageScore)
        #=======================Final da tela de Score============================#

        #=======================começo da tela do info============================#
        self.pageinfo = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageinfo.sizePolicy().hasHeightForWidth())
        self.pageinfo.setSizePolicy(sizePolicy)
        self.pageinfo.setStyleSheet("QWidget\n"
"{\n"
"background-color:#202020;\n"
"}")
        
        self.pageinfo.setObjectName("pageinfo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageinfo)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 50)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QLabel(self.pageinfo) 
        self.pixmap = QPixmap('images/info.png')
        self.label.setGeometry(QtCore.QRect(100, 50, 467, 373))
        self.label.setPixmap(self.pixmap)





        self.returnHome = QtWidgets.QPushButton(self.pageinfo)
        self.returnHome.setMinimumSize(QtCore.QSize(50, 50))
        self.returnHome.setGeometry(QtCore.QRect(270, 460, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.returnHome.setFont(font)
        self.returnHome.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#28AAF9;\n"
"border-radius:5px;\n"
"color: #fff\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:#1D8FD5;\n"
"color: #000\n"
"}")
        self.returnHome.setObjectName("returnHome")

        self.centerStackedWidget.addWidget(self.pageinfo)
        #=======================Final da tela de info============================#



        #fcarregamento das barras de cima e baixo do programa
        self.verticalLayout.addWidget(self.centerStackedWidget)
        self.statusBar = QtWidgets.QWidget(Quiz)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 30))
        self.statusBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.statusBar.setStyleSheet(".QWidget\n"
"{\n"
"background:transparent;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:8px;\n"
"border-bottom-left-radius:8px;\n"
"background:#202020;\n"
"border:1px solid #202020;\n"
"}")
        self.statusBar.setObjectName("statusBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.statusBar)
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ipInfo = QtWidgets.QLabel(self.statusBar)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(11)
        self.ipInfo.setFont(font)
        self.ipInfo.setStyleSheet(".QLabel\n"
"{\n"
"color:white;\n"
"background:#202020\n"
"}")
        self.ipInfo.setObjectName("ipInfo")
        self.horizontalLayout_3.addWidget(self.ipInfo, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Info = QtWidgets.QLabel(self.statusBar)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.Info.setFont(font)
        self.Info.setStyleSheet(".QLabel\n"
"{\n"
"color:rgba(70, 70, 70, 255);\n"
"background:transparent\n"
"}")
        self.Info.setText("")
        self.Info.setObjectName("Info")
        self.horizontalLayout_3.addWidget(self.Info, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.statusBar)
        

        self.retranslateUi(Quiz)
        self.centerStackedWidget.setCurrentIndex(0)
        self.closeBtn.clicked.connect(Quiz.close)
        self.minBtn.clicked.connect(Quiz.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(Quiz)
        Quiz.setTabOrder(self.optA, self.optB)
        Quiz.setTabOrder(self.optB, self.optC)
        Quiz.setTabOrder(self.optC, self.optD)
        Quiz.setTabOrder(self.optD, self.start_Game)
        Quiz.setTabOrder(self.start_Game, self.minBtn)
        Quiz.setTabOrder(self.minBtn, self.closeBtn)

    def retranslateUi(self, Quiz):
        _translate = QtCore.QCoreApplication.translate
        Quiz.setWindowTitle(_translate("Quiz", "Quiz"))
        self.title_label.setText(_translate("Quiz", "      QuizPY"))
        self.ipInfo.setText(_translate("Quiz", "Version 0.1                                                                                                   Create by: @londarks"))
        self.start_Game.setText(_translate("Quiz","Start Game"))
        # self.btnScore.setText(_translate("Quiz","Score"))
        self.btnInfo.setText(_translate("Quiz","Info"))
        #page game
        self.textQuestion.setText(_translate("Quiz",""))
        self.optA.setText(_translate("Quiz","A"))
        self.questA.setText(_translate("Quiz",""))
        self.optB.setText(_translate("Quiz","B"))
        self.questB.setText(_translate("Quiz",""))
        self.optC.setText(_translate("Quiz","C"))
        self.questC.setText(_translate("Quiz",""))
        self.optD.setText(_translate("Quiz","D"))
        self.questD.setText(_translate("Quiz",""))
        self.labelquestion.setText(_translate("Quiz",""))
        self.labelScore.setText(_translate("Quiz",""))
        #pageScore end game
        self.labelScorePrint.setText(_translate("Quiz","SCORE: 10000"))
        self.labelusername.setText(_translate("Quiz","Username:"))
        self.returnHome2.setText(_translate("Quiz","Concluir"))
        #pageinfo
        self.returnHome.setText(_translate("Quiz","Back"))

import resource
