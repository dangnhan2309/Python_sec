# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 32, 181, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 91, 21))
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 91, 21))
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 300, 81, 21))
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.en = QtWidgets.QPushButton(self.centralwidget)
        self.en.setGeometry(QtCore.QRect(140, 350, 75, 23))
        self.en.setObjectName("en")
        self.de = QtWidgets.QPushButton(self.centralwidget)
        self.de.setGeometry(QtCore.QRect(320, 350, 75, 23))
        self.de.setObjectName("de")
        self.plainText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainText.setGeometry(QtCore.QRect(160, 80, 271, 71))
        self.plainText.setObjectName("plainText")
        self.key = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(160, 160, 271, 71))
        self.key.setObjectName("key")
        self.cipher_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cipher_text.setGeometry(QtCore.QRect(170, 260, 271, 71))
        self.cipher_text.setObjectName("cipher_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.label_2.setText(_translate("MainWindow", "PLAIN TEXT"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", "CIPHER TEXT"))
        self.en.setText(_translate("MainWindow", "Encrypt"))
        self.de.setText(_translate("MainWindow", "Descrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
