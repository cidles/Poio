# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainAnalyzerQML.ui'
#
# Created: Tue May 28 11:30:41 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 12, 1, 1, 2)
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 11, 1, 1, 7)
        self.buttonRemoveFiles = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonRemoveFiles.sizePolicy().hasHeightForWidth())
        self.buttonRemoveFiles.setSizePolicy(sizePolicy)
        self.buttonRemoveFiles.setObjectName(_fromUtf8("buttonRemoveFiles"))
        self.gridLayout.addWidget(self.buttonRemoveFiles, 14, 2, 1, 1)
        self.listFiles = QtGui.QListView(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listFiles.sizePolicy().hasHeightForWidth())
        self.listFiles.setSizePolicy(sizePolicy)
        self.listFiles.setSizeIncrement(QtCore.QSize(1, 0))
        self.listFiles.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listFiles.setObjectName(_fromUtf8("listFiles"))
        self.gridLayout.addWidget(self.listFiles, 13, 1, 1, 2)
        self.lineeditQuickSearch = QtGui.QLineEdit(self.centralWidget)
        self.lineeditQuickSearch.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineeditQuickSearch.sizePolicy().hasHeightForWidth())
        self.lineeditQuickSearch.setSizePolicy(sizePolicy)
        self.lineeditQuickSearch.setObjectName(_fromUtf8("lineeditQuickSearch"))
        self.gridLayout.addWidget(self.lineeditQuickSearch, 14, 5, 1, 3)
        self.buttonSearch = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSearch.sizePolicy().hasHeightForWidth())
        self.buttonSearch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonSearch.setFont(font)
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.gridLayout.addWidget(self.buttonSearch, 3, 5, 1, 3)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabNewSearch = QtGui.QWidget()
        self.tabNewSearch.setObjectName(_fromUtf8("tabNewSearch"))
        self.tabWidget.addTab(self.tabNewSearch, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 2, 1, 1, 7)
        self.buttonAlignCenter = QtGui.QToolButton(self.centralWidget)
        self.buttonAlignCenter.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/aligncenter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAlignCenter.setIcon(icon)
        self.buttonAlignCenter.setIconSize(QtCore.QSize(24, 24))
        self.buttonAlignCenter.setCheckable(True)
        self.buttonAlignCenter.setAutoRaise(True)
        self.buttonAlignCenter.setObjectName(_fromUtf8("buttonAlignCenter"))
        self.gridLayout.addWidget(self.buttonAlignCenter, 12, 7, 1, 1)
        self.buttonAlignLeft = QtGui.QToolButton(self.centralWidget)
        self.buttonAlignLeft.setEnabled(False)
        self.buttonAlignLeft.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/alignleft.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAlignLeft.setIcon(icon1)
        self.buttonAlignLeft.setIconSize(QtCore.QSize(24, 24))
        self.buttonAlignLeft.setCheckable(True)
        self.buttonAlignLeft.setChecked(True)
        self.buttonAlignLeft.setAutoRaise(True)
        self.buttonAlignLeft.setObjectName(_fromUtf8("buttonAlignLeft"))
        self.gridLayout.addWidget(self.buttonAlignLeft, 12, 6, 1, 1)
        self.buttonClearThisSearch = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonClearThisSearch.sizePolicy().hasHeightForWidth())
        self.buttonClearThisSearch.setSizePolicy(sizePolicy)
        self.buttonClearThisSearch.setObjectName(_fromUtf8("buttonClearThisSearch"))
        self.gridLayout.addWidget(self.buttonClearThisSearch, 3, 1, 1, 1)
        self.declarativeviewResult = QtDeclarative.QDeclarativeView(self.centralWidget)
        self.declarativeviewResult.setFrameShape(QtGui.QFrame.StyledPanel)
        self.declarativeviewResult.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.declarativeviewResult.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.declarativeviewResult.setObjectName(_fromUtf8("declarativeviewResult"))
        self.gridLayout.addWidget(self.declarativeviewResult, 13, 3, 1, 5)
        self.buttonCloseThisSearch = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCloseThisSearch.sizePolicy().hasHeightForWidth())
        self.buttonCloseThisSearch.setSizePolicy(sizePolicy)
        self.buttonCloseThisSearch.setObjectName(_fromUtf8("buttonCloseThisSearch"))
        self.gridLayout.addWidget(self.buttonCloseThisSearch, 3, 2, 1, 1)
        self.buttonSaveSearches = QtGui.QPushButton(self.centralWidget)
        self.buttonSaveSearches.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSaveSearches.sizePolicy().hasHeightForWidth())
        self.buttonSaveSearches.setSizePolicy(sizePolicy)
        self.buttonSaveSearches.setObjectName(_fromUtf8("buttonSaveSearches"))
        self.gridLayout.addWidget(self.buttonSaveSearches, 3, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralWidget)
        self.label_8.setSizeIncrement(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 12, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 14, 3, 1, 1)
        self.buttonAddFiles = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddFiles.sizePolicy().hasHeightForWidth())
        self.buttonAddFiles.setSizePolicy(sizePolicy)
        self.buttonAddFiles.setObjectName(_fromUtf8("buttonAddFiles"))
        self.gridLayout.addWidget(self.buttonAddFiles, 14, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFiel = QtGui.QMenu(self.menuBar)
        self.menuFiel.setObjectName(_fromUtf8("menuFiel"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionNewProject = QtGui.QAction(MainWindow)
        self.actionNewProject.setEnabled(False)
        self.actionNewProject.setObjectName(_fromUtf8("actionNewProject"))
        self.actionSaveProject = QtGui.QAction(MainWindow)
        self.actionSaveProject.setEnabled(False)
        self.actionSaveProject.setObjectName(_fromUtf8("actionSaveProject"))
        self.actionSaveProjectAs = QtGui.QAction(MainWindow)
        self.actionSaveProjectAs.setEnabled(False)
        self.actionSaveProjectAs.setObjectName(_fromUtf8("actionSaveProjectAs"))
        self.actionEditWordClasses = QtGui.QAction(MainWindow)
        self.actionEditWordClasses.setEnabled(False)
        self.actionEditWordClasses.setObjectName(_fromUtf8("actionEditWordClasses"))
        self.actionSearches = QtGui.QAction(MainWindow)
        self.actionSearches.setEnabled(False)
        self.actionSearches.setObjectName(_fromUtf8("actionSearches"))
        self.actionAboutPoioAnalyzer = QtGui.QAction(MainWindow)
        self.actionAboutPoioAnalyzer.setObjectName(_fromUtf8("actionAboutPoioAnalyzer"))
        self.actionQuickSearch = QtGui.QAction(MainWindow)
        self.actionQuickSearch.setEnabled(False)
        self.actionQuickSearch.setObjectName(_fromUtf8("actionQuickSearch"))
        self.actionExportSearchResult = QtGui.QAction(MainWindow)
        self.actionExportSearchResult.setObjectName(_fromUtf8("actionExportSearchResult"))
        self.menuFiel.addAction(self.actionNewProject)
        self.menuFiel.addAction(self.actionSaveProject)
        self.menuFiel.addSeparator()
        self.menuFiel.addAction(self.actionExportSearchResult)
        self.menuFiel.addSeparator()
        self.menuFiel.addAction(self.actionSaveProjectAs)
        self.menuFiel.addAction(self.actionQuit)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionEditWordClasses)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSearches)
        self.menuEdit.addAction(self.actionQuickSearch)
        self.menuAbout.addAction(self.actionAboutPoioAnalyzer)
        self.menuBar.addAction(self.menuFiel.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.buttonClearThisSearch)
        MainWindow.setTabOrder(self.buttonClearThisSearch, self.buttonSearch)
        MainWindow.setTabOrder(self.buttonSearch, self.listFiles)
        MainWindow.setTabOrder(self.listFiles, self.buttonAlignLeft)
        MainWindow.setTabOrder(self.buttonAlignLeft, self.buttonAlignCenter)
        MainWindow.setTabOrder(self.buttonAlignCenter, self.buttonAddFiles)
        MainWindow.setTabOrder(self.buttonAddFiles, self.buttonRemoveFiles)
        MainWindow.setTabOrder(self.buttonRemoveFiles, self.lineeditQuickSearch)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PoioAnalyzer", None))
        self.label_7.setText(_translate("MainWindow", "Files:", None))
        self.buttonRemoveFiles.setText(_translate("MainWindow", "Remove files", None))
        self.buttonSearch.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNewSearch), _translate("MainWindow", "New Search...", None))
        self.buttonAlignCenter.setText(_translate("MainWindow", "...", None))
        self.buttonAlignLeft.setText(_translate("MainWindow", "...", None))
        self.buttonClearThisSearch.setText(_translate("MainWindow", "Clear This Search", None))
        self.buttonCloseThisSearch.setText(_translate("MainWindow", "Close This Search", None))
        self.buttonSaveSearches.setText(_translate("MainWindow", "Save Searches...", None))
        self.label_8.setText(_translate("MainWindow", "Result:", None))
        self.label_9.setText(_translate("MainWindow", "Quick Search:", None))
        self.buttonAddFiles.setText(_translate("MainWindow", "Add files...", None))
        self.menuFiel.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionNewProject.setText(_translate("MainWindow", "New Project", None))
        self.actionNewProject.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionSaveProject.setText(_translate("MainWindow", "Save Project", None))
        self.actionSaveProject.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSaveProjectAs.setText(_translate("MainWindow", "Save Project As...", None))
        self.actionEditWordClasses.setText(_translate("MainWindow", "Edit Word Classes...", None))
        self.actionSearches.setText(_translate("MainWindow", "Saved Searches...", None))
        self.actionAboutPoioAnalyzer.setText(_translate("MainWindow", "About PoioAnalyzer...", None))
        self.actionQuickSearch.setText(_translate("MainWindow", "Quick Search", None))
        self.actionQuickSearch.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionExportSearchResult.setText(_translate("MainWindow", "Export Search Result...", None))
        self.actionExportSearchResult.setShortcut(_translate("MainWindow", "Ctrl+E", None))

from PyQt4 import QtDeclarative
import poioanalyzer_rc
