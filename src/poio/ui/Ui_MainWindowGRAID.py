# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGRAID.ui'
#
# Created: Tue Aug 21 11:04:20 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1014, 836)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(5, -1, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayoutMain = QtGui.QVBoxLayout()
        self.verticalLayoutMain.setObjectName(_fromUtf8("verticalLayoutMain"))
        self.horizontalLayoutEditArea = QtGui.QHBoxLayout()
        self.horizontalLayoutEditArea.setObjectName(_fromUtf8("horizontalLayoutEditArea"))
        self.textedit = PoioGraidTextEdit(self.centralWidget)
        self.textedit.setObjectName(_fromUtf8("textedit"))
        self.horizontalLayoutEditArea.addWidget(self.textedit)
        self.verticalLayoutMain.addLayout(self.horizontalLayoutEditArea)
        self.gridLayout.addLayout(self.verticalLayoutMain, 1, 2, 1, 1)
        self.openProject = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openProject.sizePolicy().hasHeightForWidth())
        self.openProject.setSizePolicy(sizePolicy)
        self.openProject.setMaximumSize(QtCore.QSize(20, 16777215))
        self.openProject.setObjectName(_fromUtf8("openProject"))
        self.verticalLayout = QtGui.QVBoxLayout(self.openProject)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.projectBtn = QtGui.QPushButton(self.openProject)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectBtn.sizePolicy().hasHeightForWidth())
        self.projectBtn.setSizePolicy(sizePolicy)
        self.projectBtn.setMaximumSize(QtCore.QSize(20, 16777215))
        self.projectBtn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.projectBtn.setCheckable(True)
        self.projectBtn.setAutoDefault(False)
        self.projectBtn.setDefault(False)
        self.projectBtn.setFlat(False)
        self.projectBtn.setObjectName(_fromUtf8("projectBtn"))
        self.verticalLayout.addWidget(self.projectBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.openProject, 1, 0, 1, 1)
        self.projectManager = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectManager.sizePolicy().hasHeightForWidth())
        self.projectManager.setSizePolicy(sizePolicy)
        self.projectManager.setMinimumSize(QtCore.QSize(130, 150))
        self.projectManager.setMaximumSize(QtCore.QSize(250, 16777215))
        self.projectManager.setObjectName(_fromUtf8("projectManager"))
        self.gridLayout_2 = QtGui.QGridLayout(self.projectManager)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.removefileBtn = QtGui.QPushButton(self.projectManager)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.removefileBtn.setIcon(icon)
        self.removefileBtn.setObjectName(_fromUtf8("removefileBtn"))
        self.gridLayout_2.addWidget(self.removefileBtn, 2, 1, 1, 1)
        self.addfileBtn = QtGui.QPushButton(self.projectManager)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addfileBtn.setIcon(icon1)
        self.addfileBtn.setObjectName(_fromUtf8("addfileBtn"))
        self.gridLayout_2.addWidget(self.addfileBtn, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.projectManager)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.listFiles = QtGui.QListView(self.projectManager)
        self.listFiles.setObjectName(_fromUtf8("listFiles"))
        self.gridLayout_2.addWidget(self.listFiles, 1, 0, 1, 2)
        self.saveprojectBtn = QtGui.QPushButton(self.projectManager)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.saveprojectBtn.setIcon(icon2)
        self.saveprojectBtn.setObjectName(_fromUtf8("saveprojectBtn"))
        self.gridLayout_2.addWidget(self.saveprojectBtn, 4, 0, 1, 2)
        self.openprojectBtn = QtGui.QPushButton(self.projectManager)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/fileopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.openprojectBtn.setIcon(icon3)
        self.openprojectBtn.setObjectName(_fromUtf8("openprojectBtn"))
        self.gridLayout_2.addWidget(self.openprojectBtn, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.projectManager, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpenFile = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/projectopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon4)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionSaveFile = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFile.setIcon(icon5)
        self.actionSaveFile.setObjectName(_fromUtf8("actionSaveFile"))
        self.actionSaveFileAs = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/filesaveas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFileAs.setIcon(icon6)
        self.actionSaveFileAs.setObjectName(_fromUtf8("actionSaveFileAs"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionNewFile = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFile.setIcon(icon7)
        self.actionNewFile.setObjectName(_fromUtf8("actionNewFile"))
        self.actionDeleteUtterance = QtGui.QAction(MainWindow)
        self.actionDeleteUtterance.setEnabled(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/removeutterance.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteUtterance.setIcon(icon8)
        self.actionDeleteUtterance.setObjectName(_fromUtf8("actionDeleteUtterance"))
        self.actionCopyUtterance = QtGui.QAction(MainWindow)
        self.actionCopyUtterance.setEnabled(False)
        self.actionCopyUtterance.setObjectName(_fromUtf8("actionCopyUtterance"))
        self.actionDeleteColumn = QtGui.QAction(MainWindow)
        self.actionDeleteColumn.setEnabled(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/removeword.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteColumn.setIcon(icon9)
        self.actionDeleteColumn.setObjectName(_fromUtf8("actionDeleteColumn"))
        self.actionAboutPoioGRAID = QtGui.QAction(MainWindow)
        self.actionAboutPoioGRAID.setObjectName(_fromUtf8("actionAboutPoioGRAID"))
        self.actionOptions = QtGui.QAction(MainWindow)
        self.actionOptions.setEnabled(False)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionInsertColumnBefore = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/insertcolumnbefore.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertColumnBefore.setIcon(icon10)
        self.actionInsertColumnBefore.setObjectName(_fromUtf8("actionInsertColumnBefore"))
        self.actionInsertColumnAfter = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/insertcolumnafter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertColumnAfter.setIcon(icon11)
        self.actionInsertColumnAfter.setObjectName(_fromUtf8("actionInsertColumnAfter"))
        self.actionInsertUtteranceBefore = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/insertutterancebefore.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertUtteranceBefore.setIcon(icon12)
        self.actionInsertUtteranceBefore.setObjectName(_fromUtf8("actionInsertUtteranceBefore"))
        self.actionInsertUtteranceAfter = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pixmaps/insertutteranceafter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertUtteranceAfter.setIcon(icon13)
        self.actionInsertUtteranceAfter.setObjectName(_fromUtf8("actionInsertUtteranceAfter"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionFindAndReplace = QtGui.QAction(MainWindow)
        self.actionFindAndReplace.setObjectName(_fromUtf8("actionFindAndReplace"))
        self.actionSave_Project = QtGui.QAction(MainWindow)
        self.actionSave_Project.setIcon(icon5)
        self.actionSave_Project.setObjectName(_fromUtf8("actionSave_Project"))
        self.actionSave_Project_as = QtGui.QAction(MainWindow)
        self.actionSave_Project_as.setIcon(icon6)
        self.actionSave_Project_as.setObjectName(_fromUtf8("actionSave_Project_as"))
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setIcon(icon3)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.menuFile.addAction(self.actionNewFile)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionSaveFile)
        self.menuFile.addAction(self.actionSaveFileAs)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addAction(self.actionSave_Project_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopyUtterance)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionInsertUtteranceAfter)
        self.menuEdit.addAction(self.actionInsertUtteranceBefore)
        self.menuEdit.addAction(self.actionDeleteUtterance)
        self.menuEdit.addAction(self.actionInsertColumnBefore)
        self.menuEdit.addAction(self.actionInsertColumnAfter)
        self.menuEdit.addAction(self.actionDeleteColumn)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindAndReplace)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionOptions)
        self.menuAbout.addAction(self.actionAboutPoioGRAID)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionNewFile)
        self.toolBar.addAction(self.actionOpenFile)
        self.toolBar.addAction(self.actionSaveFile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInsertUtteranceBefore)
        self.toolBar.addAction(self.actionInsertUtteranceAfter)
        self.toolBar.addAction(self.actionDeleteUtterance)
        self.toolBar.addAction(self.actionInsertColumnBefore)
        self.toolBar.addAction(self.actionInsertColumnAfter)
        self.toolBar.addAction(self.actionDeleteColumn)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.projectBtn, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.projectManager.setShown)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PoioGRAID", None, QtGui.QApplication.UnicodeUTF8))
        self.projectBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Show/hide Project Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.projectBtn.setText(QtGui.QApplication.translate("MainWindow", "P\n"
"r\n"
"o\n"
"j\n"
"e\n"
"c\n"
"t", None, QtGui.QApplication.UnicodeUTF8))
        self.removefileBtn.setText(QtGui.QApplication.translate("MainWindow", "Remove File", None, QtGui.QApplication.UnicodeUTF8))
        self.addfileBtn.setText(QtGui.QApplication.translate("MainWindow", "Add File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "    Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.saveprojectBtn.setText(QtGui.QApplication.translate("MainWindow", "Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.openprojectBtn.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setText(QtGui.QApplication.translate("MainWindow", "Open File...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setToolTip(QtGui.QApplication.translate("MainWindow", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFile.setText(QtGui.QApplication.translate("MainWindow", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFile.setToolTip(QtGui.QApplication.translate("MainWindow", "Save File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFileAs.setText(QtGui.QApplication.translate("MainWindow", "Save File as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFileAs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save File As", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveFileAs.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Alt+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFile.setText(QtGui.QApplication.translate("MainWindow", "New File...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFile.setToolTip(QtGui.QApplication.translate("MainWindow", "Create a new annotation file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteUtterance.setText(QtGui.QApplication.translate("MainWindow", "Delete utterance", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopyUtterance.setText(QtGui.QApplication.translate("MainWindow", "Copy utterance", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopyUtterance.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteColumn.setText(QtGui.QApplication.translate("MainWindow", "Delete column", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteColumn.setToolTip(QtGui.QApplication.translate("MainWindow", "Delete column", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteColumn.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutPoioGRAID.setText(QtGui.QApplication.translate("MainWindow", "About PoioGRAID...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutPoioGRAID.setToolTip(QtGui.QApplication.translate("MainWindow", "About PoioGRAID", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOptions.setText(QtGui.QApplication.translate("MainWindow", "Options...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertColumnBefore.setText(QtGui.QApplication.translate("MainWindow", "Insert empty column before", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertColumnAfter.setText(QtGui.QApplication.translate("MainWindow", "Insert empty column after", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertUtteranceBefore.setText(QtGui.QApplication.translate("MainWindow", "Insert empty utterance before", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertUtteranceBefore.setToolTip(QtGui.QApplication.translate("MainWindow", "Insert utterance before", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInsertUtteranceAfter.setText(QtGui.QApplication.translate("MainWindow", "Insert empty utterance after", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "Find...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindAndReplace.setText(QtGui.QApplication.translate("MainWindow", "Find and Replace...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindAndReplace.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Project.setText(QtGui.QApplication.translate("MainWindow", "Save Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Project_as.setText(QtGui.QApplication.translate("MainWindow", "Save Project as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Project.setText(QtGui.QApplication.translate("MainWindow", "Open Project", None, QtGui.QApplication.UnicodeUTF8))

from poio.ui.PoioGraidTextEdit import PoioGraidTextEdit
import poio.ui.poio_rc
