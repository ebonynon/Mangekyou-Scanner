# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ebony/Coding/Qt-Cerator/port-scanner/port-scanner/gfxui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_gfxUI(object):
    def setupUi(self, gfxUI):
        gfxUI.setObjectName(_fromUtf8("gfxUI"))
        gfxUI.resize(750, 325)
        gfxUI.setWindowIcon(QtGui.QIcon("images/anonymous_mask1600.png"))
        self.centralWidget = QtGui.QWidget(gfxUI)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 571, 241))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 10, 161, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 281, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(600, 10, 131, 291))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        gfxUI.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(gfxUI)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        gfxUI.setStatusBar(self.statusBar)

        self.retranslateUi(gfxUI)
        QtCore.QMetaObject.connectSlotsByName(gfxUI)

    def retranslateUi(self, gfxUI):
        gfxUI.setWindowTitle(_translate("gfxUI", "Mangekyou-Scanner", None))
        self.label.setText(_translate("gfxUI", "Host Address:", None))
        self.pushButton.setText(_translate("gfxUI", "start", None))
    # self.label_2.setText(_translate("gfxUI", "<html><head/><body><p><img wide=\"131\" height=\"291\" src=\":/new/prefix1/images/Yc6657d.png\"/></p></body></html>", None))
        self.label_2.setPixmap(QtGui.QPixmap("images/compress-image.jpg"))
