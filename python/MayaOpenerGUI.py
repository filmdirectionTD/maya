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
import pymel.core as pm

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

        # Variables
        self.prj = os.environ["PRJ"]
        self.job = os.environ["JOB"]
        self.scenes = os.environ["SCENES"]
        self.layout = self.scenes + "/layout"
        self.camera = os.environ["CAMERA"]
        self.assets = os.environ["ASSETS"]
        # Custom worktype variable setup
        self.worktype = os.environ["RENDER"].split("/")[-1]
        self.worktypePath = os.path.join(self.scenes, self.worktype)

        # Fill Places
        places = [self.worktype.capitalize(), "PRJ", "JOB", "SCENES", "LAYOUT", "CAMERA", "ASSETS"]

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
        # show current scenes path
        self.FillByPlace(self.worktypePath)

    def setupUI(self):
        # icons
        self.iconFolder = QIcon(QPixmap('/home/asknarin/py_projects/icons/folder.png'))
        self.iconFile = QIcon(QPixmap('/home/asknarin/py_projects/icons/file.png'))
        self.iconUp = QIcon(QPixmap('/home/asknarin/py_projects/icons/up.png'))

        # Places column:
        labelPlaces = QLabel("Places:")
        self.listPlaces = QListWidget()
        self.listPlaces.setFixedWidth(150)
        self.listPlaces.setSpacing(2)
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
        self.filterFileType.addItem("*.ma  and *.mb")  # 0. Show both ma and mb files
        self.filterFileType.addItem("*.ma  - maya ASCII")  # 1. Show only ma
        self.filterFileType.addItem("*.mb  - maya binary")  # 2. Show only mb
        self.filterFileType.addItem("*.mel - MEL scripts")  # 3. Show only MEL scripts
        self.filterFileType.addItem("*.fbx")  # 4. Show only FBX
        self.filterFileType.addItem("*.obj")  # 5. Show only obj
        self.filterFileType.addItem("*.abc")  # 6. Show only abc
        self.filterFileType.addItem("*.* - all types")  # 7. show all files
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
        self.listPlaces.itemClicked.connect(self.PlaceSelected)
        self.filterFileType.currentIndexChanged.connect(self.ChangeFilter)
        self.listFiles.itemDoubleClicked.connect(self.IntoFolder)
        self.filterFileType.currentIndexChanged.connect(self.FilterChanged)
        self.buttonOpen.clicked.connect(self.OpenSelectedFile)

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

        # Get full list of folder items
        folderItems = os.listdir(pathInput)

        # To have files always appear after folders
        # Put folders and files into separate lists
        folderItemsfolders = []
        folderItemsfiles = []

        for folderItem in folderItems:
            fullPath = os.path.join(pathInput, folderItem)
            if (self.CheckType(fullPath) == "folder"):
                folderItemsfolders.append(folderItem)
            elif (self.CheckType(fullPath) == "file"):
                # if we have file we should filter them using self.filterFileType
                if (self.filterFileType.currentIndex() == 0):
                    if ((".ma" in folderItem) or (".mb" in folderItem)):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 1):
                    if (".ma" in folderItem):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 2):
                    if (".mb" in folderItem):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 3):
                    if (".mel" in folderItem):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 4):
                    if (".fbx" in folderItem):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 5):
                    if (".obj" in folderItem):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 6):
                    if (".abc" in folderItem):
                        folderItemsfiles.append(folderItem)
                elif (self.filterFileType.currentIndex() == 7):
                    folderItemsfiles.append(folderItem)

        # Sort both lists
        folderItemsfolders.sort()
        folderItemsfiles.sort()

        folderItemsFiltered = []
        folderItemsFiltered.extend(folderItemsfolders)
        folderItemsFiltered.extend(folderItemsfiles)

        self.listFiles.clear()
        self.listFiles.addItem("..")
        self.listFiles.item(0).setIcon(self.iconUp)

        for folderItem in folderItemsFiltered:
            self.listFiles.addItem(folderItem)

        count = 0
        for i in range(0, len(folderItemsFiltered) + 1):

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
            self.FillByPlace(self.prj)
        elif (item.text() == "JOB"):
            self.FillByPlace(self.job)
        elif (item.text() == "SCENES"):
            self.FillByPlace(self.scenes)
        elif (item.text() == "LAYOUT"):
            self.FillByPlace(self.layout)
        elif (item.text() == "CAMERA"):
            self.FillByPlace(self.camera)
        elif (item.text() == "ASSETS"):
            self.FillByPlace(self.assets)
        elif (item.text() == self.worktype.capitalize()):
            self.FillByPlace(self.worktypePath)

    def FilterChanged(self, index):
        # Get current path
        pathInput = self.lineFullPath.text()
        self.FillByPlace(pathInput)

    def OpenSelectedFile(self):
        # Get selected file name
        if (len(self.listFiles.selectedItems()) > 0):
            selectedFile = self.listFiles.currentItem().text()
            currentpath = self.lineFullPath.text()
            openPath = os.path.join(currentpath, selectedFile)
            # Check for unsaved changes:
            if (cmds.file(q=True, modified=True)):
                reaction = cmds.confirmDialog(title='Scene has unsaved changes!', message='What are you going to do?',
                                              button=['Save', 'Save+', 'Ignore and Open', 'Cancel'],
                                              defaultButton='Save Changes then Open')  # , cancelButton='Close Dialog')
                if (reaction == "Save"):
                    # Saving current scene
                    # Check if scene was ever saved
                    currentSceneName = cmds.file(q=True, sn=True)
                    if (currentSceneName == ""):
                        # Get new Filename
                        baseName = os.environ["JOB"].split("/")[-1] + "_" + os.environ["RENDER"].split("/")[
                            -1] + "_v001.mb"
                        newName = cmds.promptDialog(title='Enter scene name', message='Enter scene Name:',
                                                    text=baseName, button=['OK', 'Cancel'], defaultButton='OK',
                                                    cancelButton='Cancel', dismissString='Cancel')

                        print "Need to Save to the new file"
                    else:
                        print "just save current changes to the same file"
                elif (reaction == "Save+"):
                    print "Saving to new version"
                elif (reaction == "Ignore and Open"):
                    # Open selected file ignoring current changes
                    self.close()
                    cmds.file(openPath, open=True, force=True)
                elif (reaction == "Cancel"):
                    print "Closing current window"
            else:
                print "No need to save - open window"

# cmds.file(openPath, open=True)
