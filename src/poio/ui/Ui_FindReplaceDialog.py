# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FindReplaceDialog.ui'
#
# Created: Tue May 28 11:30:42 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_FindReplaceDialog(object):
    def setupUi(self, FindReplaceDialog):
        FindReplaceDialog.setObjectName(_fromUtf8("FindReplaceDialog"))
        FindReplaceDialog.resize(342, 140)
        self.gridLayout = QtGui.QGridLayout(FindReplaceDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.findReplaceForm = FindReplaceForm(FindReplaceDialog)
        self.findReplaceForm.setObjectName(_fromUtf8("findReplaceForm"))
        self.gridLayout.addWidget(self.findReplaceForm, 0, 0, 1, 1)

        self.retranslateUi(FindReplaceDialog)
        QtCore.QMetaObject.connectSlotsByName(FindReplaceDialog)

    def retranslateUi(self, FindReplaceDialog):
        FindReplaceDialog.setWindowTitle(_translate("FindReplaceDialog", "Find/Replace", None))

from poio.ui.FindReplaceForm import FindReplaceForm
