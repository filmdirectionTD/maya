# Import Pysid Libraries
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
# import os libraries
import os
import sys
# import maya libraries
import maya.cmds as cmds

# Get reference to mainMayaWindow
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QWidget)


# Class of Mayaopen/Import dialogue:
class MayaOpenSceneGUI(QWidget):
    # Constructor
    def __init__(self):
        super(MayaOpenSceneGUI, self).__init__()
        # SetupUI - generate all interface elements
        self.setupUI()
        # Fill Places
        places = ["PRJ", "JOB", "SCENES", "LAYOUT", "CAMERA", "ASSETS"]
        for place in places:
            self.listPlaces.addItem(place)

        # Fill Files with initial data and color lines
        count = 0
        for i in range(0, 55):
            if (count == 0):
                self.listFiles.addItem("..")
                count = 1
            else:
                self.listFiles.addItem("")
        count = 0
        for i in range(0, 55):
            if (count == 0):
                self.listFiles.item(i).setBackground(QColor("#272727"))
                count = 1
            else:
                self.listFiles.item(i).setBackground(QColor("#2b2b2b"))
                count = 0

    def setupUI(self):
        # icons
        self.iconFolder = QIcon(QPixmap('/home/asknarin/py_projects/icons/folder.png'))
        self.iconFile = QIcon(QPixmap('/home/asknarin/py_projects/icons/file.png'))
        self.iconUp = QIcon(QPixmap('/home/asknarin/py_projects/icons/up.png'))

        # Places column:
        labelPlaces = QLabel("Places:")
        self.listPlaces = QListWidget()
        self.listPlaces.setFixedWidth(150)
        placesLayout = QVBoxLayout()
        placesLayout.addWidget(labelPlaces, 0)
        placesLayout.addWidget(self.listPlaces, 1)

        # FullPath row
        labelFullPath = QLabel("Full Path:")
        self.lineFullPath = QLineEdit()
        self.lineFullPath.setAutoFillBackground(True)
        pathLayout = QHBoxLayout()
        pathLayout.addWidget(labelFullPath, 0)
        pathLayout.addWidget(self.lineFullPath, 1)

        # FileView
        self.listFiles = QListWidget()

        layoutpathFiles = QVBoxLayout()
        layoutpathFiles.setSpacing(8)
        layoutpathFiles.addItem(pathLayout)
        layoutpathFiles.addWidget(self.listFiles, 1)

        # Options Panel
        optionsLabel = QLabel("Browsing options:")
        sortByLabel = QLabel("Sort by:")
        sortByLabel.setFixedWidth(80)
        self.sortByCombobox = QComboBox(self)
        self.sortByCombobox.addItem("name")
        self.sortByCombobox.addItem("name_reverse")
        self.sortByCombobox.addItem("date")
        self.sortByCombobox.addItem("date_reverse")
        self.sortByCombobox.setFixedWidth(130)

        filterLabel = QLabel("Filter list:")
        filterLabel.setFixedWidth(80)

        self.listFilterLine = QLineEdit()
        self.listFilterLine.setFixedWidth(130)

        optionsBOX = QHBoxLayout()
        optionsBOX.setAlignment(Qt.AlignCenter)
        optionsBOX.addWidget(optionsLabel, 0)

        sortBox = QHBoxLayout()
        sortBox.addWidget(sortByLabel, 0)
        sortBox.addWidget(self.sortByCombobox, 1)

        filterBox = QHBoxLayout()
        filterBox.addWidget(filterLabel, 0)
        filterBox.addWidget(self.listFilterLine, 1)

        browseOptionsBOX = QVBoxLayout()
        browseOptionsBOX.addItem(optionsBOX)
        browseOptionsBOX.addItem(sortBox)
        browseOptionsBOX.addItem(filterBox)
        browseOptionsBOX.setAlignment(Qt.AlignTop)
        browseOptionsBOX.setSpacing(10)

        layoutPlacesPathFiles = QHBoxLayout()
        layoutPlacesPathFiles.setSpacing(10)
        layoutPlacesPathFiles.addItem(placesLayout)
        layoutPlacesPathFiles.addItem(layoutpathFiles)
        layoutPlacesPathFiles.addItem(browseOptionsBOX)

        # Buttons
        # FileType Filter Menu
        self.filterFileType = QComboBox(self)
        self.filterFileType.addItem("*.ma  and *.mb")
        self.filterFileType.addItem("*.ma - maya ASCII")
        self.filterFileType.addItem("*.mb - maya binary")
        self.filterFileType.addItem("*.fbx")
        self.filterFileType.addItem("*.* - ma, mb, fbx")
        self.filterFileType.setFixedWidth(150)

        # namespace
        labelnamespace = QLabel(" Add namespace: ")
        self.lineNamespace = QLineEdit()
        self.lineNamespace.setAutoFillBackground(True)

        # Buttons:
        self.buttonOpen = QPushButton("OPEN")
        self.buttonOpen.setFixedWidth(130)
        self.buttonImport = QPushButton("IMPORT")
        self.buttonImport.setFixedWidth(130)
        self.buttonReference = QPushButton("REFERENCE")
        self.buttonReference.setFixedWidth(130)

        layoutButtons = QHBoxLayout()
        layoutButtons.addWidget(self.filterFileType, 0)
        layoutButtons.addWidget(labelnamespace, 1)
        layoutButtons.addWidget(self.lineNamespace, 2)
        layoutButtons.addWidget(self.buttonOpen, 3)
        layoutButtons.addWidget(self.buttonImport, 4)
        layoutButtons.addWidget(self.buttonReference, 5)

        globalLayout = QVBoxLayout()

        globalLayout.addItem(layoutPlacesPathFiles)
        globalLayout.addItem(layoutButtons)

        # Signals and slots --------------------------------
        self.listPlaces.itemEntered.connect(self.PlaceSelected)
        self.filterFileType.currentIndexChanged.connect(self.ChangeFilter)
        self.listFiles.itemDoubleClicked.connect(self.IntoFolder)

        # general window setup---------------------------------
        self.setLayout(globalLayout)
        self.setGeometry(400, 300, 850, 500)
        self.setWindowTitle("FD Open File Dialog")
        self.show()

    def IntoFolder(self, item):
        clickedFileName = item.text()

        if (clickedFileName == ".."):
            fullPath = os.path.split(self.lineFullPath.text())[0]
            self.FillByPlace(fullPath)
        else:
            # check if it is folder or not
            fullPath = os.path.join(self.lineFullPath.text(), clickedFileName)
            if (os.path.isdir(fullPath)):
                self.FillByPlace(fullPath)
                self.listPlaces.clearSelection()

    def ChangeFilter(self, index):
        if (index == 3):
            self.buttonOpen.setEnabled(False)
            self.buttonReference.setEnabled(False)
        else:
            self.buttonOpen.setEnabled(True)
            self.buttonReference.setEnabled(True)

    def CheckType(self, path):
        if (os.path.isdir(path)):
            return "folder"
        else:
            return "file"

    def FillByPlace(self, pathInput):
        self.lineFullPath.setText(pathInput)

        folderItems = os.listdir(pathInput)

        self.listFiles.clear()
        self.listFiles.addItem("..")
        self.listFiles.item(0).setIcon(self.iconUp)

        for folderItem in folderItems:
            self.listFiles.addItem(folderItem)

        count = 0
        for i in range(0, len(folderItems) + 1):

            fullPath = os.path.join(pathInput, self.listFiles.item(i).text())
            if (self.CheckType(fullPath) == "file"):
                self.listFiles.item(i).setIcon(self.iconFile)
            elif (self.CheckType(fullPath) == "folder"):
                self.listFiles.item(i).setIcon(self.iconFolder)

            if (count == 0):
                self.listFiles.item(i).setBackground(QColor("#272727"))
                count = 1
            else:
                self.listFiles.item(i).setBackground(QColor("#2b2b2b"))
                count = 0

    def PlaceSelected(self, item):
        if (item.text() == "PRJ"):
            self.FillByPlace("/fd/projects/chernobyl")
        elif (item.text() == "JOB"):
            self.FillByPlace("/fd/projects/chernobyl/episodes/ep02/ep02-1250")
        elif (item.text() == "SCENES"):
            self.FillByPlace("/fd/projects/chernobyl/episodes/ep02/ep02-1250/scenes")
        elif (item.text() == "LAYOUT"):
            self.FillByPlace("/fd/projects/chernobyl/episodes/ep02/ep02-1250/scenes/layout")
        elif (item.text() == "CAMERA"):
            self.FillByPlace("/fd/projects/chernobyl/episodes/ep02/ep02-1250/scenes/tracking")
        elif (item.text() == "ASSETS"):
            self.FillByPlace("/fd/projects/chernobyl/assets")

