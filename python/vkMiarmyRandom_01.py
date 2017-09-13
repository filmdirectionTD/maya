from PySide import QtGui, QtCore
import maya.cmds as cmds
import random

class vk_crowd_Window1(QtGui.QWidget):
	pxSize = 50
	def __init__(self):
		super(vk_crowd_Window1, self).__init__()
		self.setupUi()
		
	
	def setupUi(self):
		#Labels
		label1 = QtGui.QLabel('Select objects:')
		label2 = QtGui.QLabel('Number of Textures:')
		label3 = QtGui.QLabel('Add and/or randomize:')
		label4 = QtGui.QLabel('Custom color Section:')
		separator1 = QtGui.QLabel('   ')
		
		#Select Buttons
		self.btnAxe1 = QtGui.QPushButton('Select all Axe1')
		self.btnSwordSW = QtGui.QPushButton('Select all SwordSW')
		self.btnShield4 = QtGui.QPushButton('Select all Shield4')
		self.btnShield6 = QtGui.QPushButton('Select all Shield6')
		self.btnShield7 = QtGui.QPushButton('Select all Shield7')
		self.btnJiroslav = QtGui.QPushButton('Selrct all Jiroslav')
		self.btnBajen = QtGui.QPushButton('Select all  Bajen')
		self.btnBjornWolf = QtGui.QPushButton('Select all  BjornWolf')
		#Custom Color Buttons
		self.btnAddCustomColorAttr = QtGui.QPushButton('Add Custom Color Attributes')
		self.btnRandomizeColors1 = QtGui.QPushButton('Randomize Colors 1 - RGB')
		self.btnRandomizeColors2 = QtGui.QPushButton('Randomize Colors 2 - HSV')		
		self.btnClearLog = QtGui.QPushButton('Clear Log -->')

		#setting up Icons
		iconAxe1 = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Axe1.png'))
		iconSwordSW = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/swordSW.png'))
		iconShield4 = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Shield04.png'))
		iconShield6 = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Shield06.png'))
		iconShield7 = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Shield07.png'))
		iconBajen = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Bajen.png'))
		iconJiroslav = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Jiroslav.png'))
		iconBjornWolf = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/Bjornwolf.png'))
		
		iconCustomColor = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/CustomColor.png'))
		iconRandomColor1 = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/RandomColor1rgb.png'))
		iconRandomColor2 = QtGui.QIcon(QtGui.QPixmap('//server/bin/icons/VIKING/RandomColor2hsv.png'))

		self.btnAxe1.setIcon(iconAxe1)
		self.btnAxe1.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnAxe1.setStyleSheet("text-align: left; padding: 4px;")
		self.btnSwordSW.setIcon(iconSwordSW)
		self.btnSwordSW.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnSwordSW.setStyleSheet("text-align: left; padding: 4px;")
		self.btnShield4.setIcon(iconShield4)
		self.btnShield4.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnShield4.setStyleSheet("text-align: left; padding: 4px;")
		self.btnShield6.setIcon(iconShield6)
		self.btnShield6.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnShield6.setStyleSheet("text-align: left; padding: 4px;")
		self.btnShield7.setIcon(iconShield7)
		self.btnShield7.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnShield7.setStyleSheet("text-align: left; padding: 4px;")
		self.btnJiroslav.setIcon(iconBajen)
		self.btnJiroslav.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnJiroslav.setStyleSheet("text-align: left; padding: 4px;")
		self.btnBajen.setIcon(iconJiroslav)
		self.btnBajen.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnBajen.setStyleSheet("text-align: left; padding: 4px;")
		self.btnBjornWolf.setIcon(iconBjornWolf)
		self.btnBjornWolf.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnBjornWolf.setStyleSheet("text-align: left; padding: 4px;")
		
		self.btnAddCustomColorAttr.setIcon(iconCustomColor)
		self.btnAddCustomColorAttr.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnAddCustomColorAttr.setStyleSheet("text-align: left; padding: 4px;")
		self.btnRandomizeColors1.setIcon(iconRandomColor1)
		self.btnRandomizeColors1.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnRandomizeColors1.setStyleSheet("text-align: left; padding: 4px;")
		self.btnRandomizeColors2.setIcon(iconRandomColor2)
		self.btnRandomizeColors2.setIconSize(QtCore.QSize(self.pxSize, self.pxSize))
		self.btnRandomizeColors2.setStyleSheet("text-align: left; padding: 4px;")

		
		#Texture count inputs
		self.inputAxe1 = QtGui.QLineEdit('1')
		self.inputSwordSW = QtGui.QLineEdit('1')
		self.inputShield4 = QtGui.QLineEdit('5')
		self.inputShield6 = QtGui.QLineEdit('4')
		self.inputShield7 = QtGui.QLineEdit('4')
		self.inputJiroslav = QtGui.QLineEdit('4')
		self.inputBajen = QtGui.QLineEdit('4')
		self.inputBjornWolf = QtGui.QLineEdit('8')
		#Add/Set texture random attribute
		self.btnAxe1Addrand = QtGui.QPushButton('Add/Randomize')
		self.btnSwordSWAddrand = QtGui.QPushButton('Add/Randomize')
		self.btnShield4Addrand = QtGui.QPushButton('Add/Randomize')
		self.btnShield6Addrand = QtGui.QPushButton('Add/Randomize')
		self.btnShield7Addrand = QtGui.QPushButton('Add/Randomize')
		self.btnJiroslavAddrand = QtGui.QPushButton('Add/Randomize')
		self.btnBajenAddrand = QtGui.QPushButton('Add/Randomize')
		self.btnBjornWolfAddrand = QtGui.QPushButton('Add/Randomize')

		
		gBox = QtGui.QGridLayout()
		
		gBox.addWidget(label1, 0, 1)
		gBox.addWidget(separator1, 0, 2)
		gBox.addWidget(label2, 0, 3)
		gBox.addWidget(separator1, 0, 4)
		gBox.addWidget(label3, 0, 5)
		gBox.addWidget(separator1, 0, 6)
		gBox.addWidget(label4, 0, 7)
		
		gBox.addWidget(self.btnAxe1, 1, 1)
		gBox.addWidget(self.btnSwordSW, 2, 1)
		gBox.addWidget(self.btnShield4, 3, 1)
		gBox.addWidget(self.btnShield6, 4, 1)
		gBox.addWidget(self.btnShield7, 5, 1)
		gBox.addWidget(self.btnJiroslav, 6, 1)
		gBox.addWidget(self.btnBajen, 7, 1)
		gBox.addWidget(self.btnBjornWolf, 8, 1)
		
		gBox.addWidget(self.inputAxe1, 1, 3)
		gBox.addWidget(self.inputSwordSW, 2, 3)
		gBox.addWidget(self.inputShield4, 3, 3)
		gBox.addWidget(self.inputShield6, 4, 3)
		gBox.addWidget(self.inputShield7, 5, 3)
		gBox.addWidget(self.inputJiroslav, 6, 3)
		gBox.addWidget(self.inputBajen, 7, 3)
		gBox.addWidget(self.inputBjornWolf, 8, 3)

		gBox.addWidget(self.btnAxe1Addrand, 1, 5)
		gBox.addWidget(self.btnSwordSWAddrand, 2, 5)
		gBox.addWidget(self.btnShield4Addrand, 3, 5)
		gBox.addWidget(self.btnShield6Addrand, 4, 5)
		gBox.addWidget(self.btnShield7Addrand, 5, 5)
		gBox.addWidget(self.btnJiroslavAddrand, 6, 5)
		gBox.addWidget(self.btnBajenAddrand, 7, 5)
		gBox.addWidget(self.btnBjornWolfAddrand, 8, 5)
		
		gBox.addWidget(self.btnAddCustomColorAttr, 1, 7)
		gBox.addWidget(self.btnRandomizeColors1, 2, 7)
		gBox.addWidget(self.btnRandomizeColors2, 3, 7)
		gBox.addWidget(self.btnClearLog, 8, 7)
		
		vbox = QtGui.QVBoxLayout()
		#TextEdit
		self.OutTextWindow = QtGui.QTextEdit('Log: ')
		self.OutTextWindow.append('------------------------------------------------')
		
		vbox.addItem(gBox)
		vbox.addWidget(self.OutTextWindow)
		
		#connect slots and signals
		self.btnAxe1.clicked.connect(self.selectAxe1)
		self.btnSwordSW.clicked.connect(self.selectSwordSW)
		self.btnShield4.clicked.connect(self.selectShield04)
		self.btnShield6.clicked.connect(self.selectShield06)
		self.btnShield7.clicked.connect(self.selectShield07)
		self.btnJiroslav.clicked.connect(self.selectJiroslav)
		self.btnBajen.clicked.connect(self.selectBajen)
		self.btnBjornWolf.clicked.connect(self.selectBjornWolf)
		self.btnClearLog.clicked.connect(self.clearLogWindow)
		self.btnAxe1Addrand.clicked.connect(self.randomizeTxAxe1)
		self.btnSwordSWAddrand.clicked.connect(self.randomizeTxSwordSW)
		self.btnShield4Addrand.clicked.connect(self.randomizeTxShield4)
		self.btnShield6Addrand.clicked.connect(self.randomizeTxShield6)
		self.btnShield7Addrand.clicked.connect(self.randomizeTxShield7)
		self.btnJiroslavAddrand.clicked.connect(self.randomizeTxJiroslav)
		self.btnBajenAddrand.clicked.connect(self.randomizeTxBajen)
		self.btnBjornWolfAddrand.clicked.connect(self.randomizeTxBjornWolf)
		self.btnAddCustomColorAttr.clicked.connect(self.addRandomColorAttributes)
		self.btnRandomizeColors1.clicked.connect(self.randomizeRGB)
		self.btnRandomizeColors2.clicked.connect(self.randomizeHSV)
		
		#main Window Properities
		self.setLayout(vbox)
		self.setGeometry(300, 300, 600, 900)
		self.setWindowTitle('VIKING CROWD RANDOMIZATION')
		self.show()

	def clearLogWindow(self):
		self.OutTextWindow.clear()
		self.OutTextWindow.append('Log: \n------------------------------------------------')
		
	
	def selectAxe1(self):
		shapesList = cmds.ls(shapes=True)
		Axe1Shapes = []
		for tmpShape in shapesList:
			if 'Axe1' in tmpShape:
				Axe1Shapes.append(tmpShape)
		cmds.select(Axe1Shapes)
		self.OutTextWindow.append('Selected Axe1 shapes: \n' + str(Axe1Shapes) + '\n--- Sumary:\nShape selected Axe1\n'+ str(len(Axe1Shapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def selectSwordSW(self):
		shapesList = cmds.ls(shapes=True)
		SwordSWShapes = []
		for tmpShape in shapesList:
			if 'SwordSW' in tmpShape:
				SwordSWShapes.append(tmpShape)
		cmds.select(SwordSWShapes)
		self.OutTextWindow.append('Selected SwordSW shapes: \n' + str(SwordSWShapes) + '\n--- Sumary:\nShape selected SwordSW\n'+ str(len(SwordSWShapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
		
	def selectShield04(self):
		shapesList = cmds.ls(shapes=True)
		Shield04Shapes = []
		for tmpShape in shapesList:
			if 'Shield4' in tmpShape:
				Shield04Shapes.append(tmpShape)
		cmds.select(Shield04Shapes)
		self.OutTextWindow.append('Selected Shield04 shapes: \n' + str(Shield04Shapes) + '\n--- Sumary:\nShape selected Shield04\n'+ str(len(Shield04Shapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def selectShield06(self):
		shapesList = cmds.ls(shapes=True)
		Shield06Shapes = []
		for tmpShape in shapesList:
			if 'Shield6' in tmpShape:
				Shield06Shapes.append(tmpShape)
		cmds.select(Shield06Shapes)
		self.OutTextWindow.append('Selected Shield06 shapes: \n' + str(Shield06Shapes) + '\n--- Sumary:\nShape selected Shield06\n'+ str(len(Shield06Shapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def selectShield07(self):
		shapesList = cmds.ls(shapes=True)
		Shield07Shapes = []
		for tmpShape in shapesList:
			if 'Shield7' in tmpShape:
				Shield07Shapes.append(tmpShape)
		cmds.select(Shield07Shapes)
		self.OutTextWindow.append('Selected Shield07 shapes: \n' + str(Shield07Shapes) + '\n--- Sumary:\nShape selected Shield07\n'+ str(len(Shield07Shapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())


	def selectJiroslav(self):
		shapesList = cmds.ls(shapes=True)
		JiroslavShapes = []
		for tmpShape in shapesList:
			if 'Jiroslav' in tmpShape:
				JiroslavShapes.append(tmpShape)
		cmds.select(JiroslavShapes)
		self.OutTextWindow.append('Selected Jiroslav shapes: \n' + str(JiroslavShapes) + '\n--- Sumary:\nShape selected Jiroslav\n'+ str(len(JiroslavShapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def selectBajen(self):
		shapesList = cmds.ls(shapes=True)
		BajenShapes = []
		for tmpShape in shapesList:
			if 'Bajen' in tmpShape:
				BajenShapes.append(tmpShape)
		cmds.select(BajenShapes)
		self.OutTextWindow.append('Selected Bajen shapes: \n' + str(BajenShapes) + '\n--- Sumary:\nShape selected Bajen\n'+ str(len(BajenShapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
		
	def selectBjornWolf(self):
		shapesList = cmds.ls(shapes=True)
		BjornWolfShapes = []
		for tmpShape in shapesList:
			if 'BjornWolf' in tmpShape:
				BjornWolfShapes.append(tmpShape)
		cmds.select(BjornWolfShapes)
		self.OutTextWindow.append('Selected BjornWolf shapes: \n' + str(BjornWolfShapes) + '\n--- Sumary:\nShape selected BjornWolf\n'+ str(len(BjornWolfShapes)) + ' shapes selected')
		self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
	
	#Randomize textures: (arring texnum attributes and randomize their values by given number)
	def randomizeTxAxe1(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'Axe1' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputAxe1.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputAxe1.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def randomizeTxSwordSW(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'SwordSW' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputSwordSW.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputSwordSW.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def randomizeTxShield4(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'Shield4' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputShield4.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputShield4.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def randomizeTxShield6(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'Shield6' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputShield6.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputShield6.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def randomizeTxShield7(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'Shield7' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputShield7.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputShield7.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
					
	def randomizeTxJiroslav(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'Jiroslav' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputJiroslav.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputJiroslav.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def randomizeTxBajen(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'Bajen' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputBajen.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputBajen.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())

	def randomizeTxBjornWolf(self):
		shapesList = cmds.ls(shapes=True)
		for tmpShape in shapesList:
			if 'BjornWolf' in tmpShape:
				if cmds.objExists(tmpShape + '.texnum'):
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputBjornWolf.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				else:
					cmds.select(tmpShape)
					cmds.addAttr(shortName='texnum', longName='texnum', at='byte', defaultValue=0, minValue=0, maxValue=100)
					self.OutTextWindow.append(tmpShape + '.texnum attribute Created')
					tmpAttrName = tmpShape + '.texnum'
					TxNumber = int(self.inputBjornWolf.text())
					tmpRandomNumber = random.randint(0, TxNumber)
					cmds.setAttr(tmpAttrName, tmpRandomNumber)
					self.OutTextWindow.append(tmpShape + '.texnum is set to ' + str(tmpRandomNumber))
					self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
					
	def addRandomColorAttributes(self):
		shapesList = cmds.ls(sl=True)
		for tmpShape in shapesList:
			if cmds.objExists(tmpShape + '.rmanCrandomColor1'):
				self.OutTextWindow.append(tmpShape + '.rmanCrandomColor1 already exists')
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
			else:
				cmds.select(tmpShape)
				cmds.addAttr( longName='rmanCrandomColor1', usedAsColor=True, attributeType='float3' )
				cmds.addAttr( longName='red_rmanCrandomColor1', attributeType='float', parent='rmanCrandomColor1' )
				cmds.addAttr( longName='green_rmanCrandomColor1', attributeType='float', parent='rmanCrandomColor1' )
				cmds.addAttr( longName='blue_rmanCrandomColor1', attributeType='float', parent='rmanCrandomColor1' )
				self.OutTextWindow.append(tmpShape + '.rmanCrandomColor1 created')
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
			
			if cmds.objExists(tmpShape + '.rmanCrandomColor2'):
				self.OutTextWindow.append(tmpShape + '.rmanCrandomColor2 already exists')
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
			else:
				cmds.select(tmpShape)
				cmds.addAttr( longName='rmanCrandomColor2', usedAsColor=True, attributeType='float3' )
				cmds.addAttr( longName='red_rmanCrandomColor2', attributeType='float', parent='rmanCrandomColor2' )
				cmds.addAttr( longName='green_rmanCrandomColor2', attributeType='float', parent='rmanCrandomColor2' )
				cmds.addAttr( longName='blue_rmanCrandomColor2', attributeType='float', parent='rmanCrandomColor2' )
		cmds.select(shapesList)

	def randomizeRGB(self):
		shapesList = cmds.ls(sl=True)
		for tmpShape in shapesList:
			if cmds.objExists(tmpShape + '.rmanCrandomColor1'):
				Rcolor = random.uniform(0.0, 1.0)
				Gcolor = random.uniform(0.0, 1.0)
				Bcolor = random.uniform(0.0, 1.0)
				tmpAttrNameR = tmpShape + '.red_rmanCrandomColor1'
				tmpAttrNameG = tmpShape + '.green_rmanCrandomColor1'
				tmpAttrNameB = tmpShape + '.blue_rmanCrandomColor1'
				cmds.setAttr(tmpAttrNameR, Rcolor)
				cmds.setAttr(tmpAttrNameG, Gcolor)
				cmds.setAttr(tmpAttrNameB, Bcolor)
				self.OutTextWindow.append(tmpShape + '.rmanCrandomColor1 is set to: ' + str(Rcolor) +' '+ str(Gcolor) +' '+ str(Bcolor))
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
			else:
				self.OutTextWindow.append(tmpShape + " hasn't rmanCrandomColor1 Attribute. Create it first.")
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
				
	def randomizeHSV(self):
		shapesList = cmds.ls(sl=True)
		for tmpShape in shapesList:
			if cmds.objExists(tmpShape + '.rmanCrandomColor2'):
				Hcolor = random.uniform(0.0, 1.0)
				Scolor = random.uniform(0.05, 0.15)
				Vcolor = random.uniform(1.0, 1.1)
				import colorsys
				tmpColorConverted = colorsys.hsv_to_rgb(Hcolor, Scolor, Vcolor)
				tmpAttrNameR = tmpShape + '.red_rmanCrandomColor2'
				tmpAttrNameG = tmpShape + '.green_rmanCrandomColor2'
				tmpAttrNameB = tmpShape + '.blue_rmanCrandomColor2'
				cmds.setAttr(tmpAttrNameR, tmpColorConverted[0])
				cmds.setAttr(tmpAttrNameG, tmpColorConverted[1])
				cmds.setAttr(tmpAttrNameB, tmpColorConverted[2])
				self.OutTextWindow.append(tmpShape + '.rmanCrandomColor2 is set to: ' + str(tmpColorConverted[0]) +' '+ str(tmpColorConverted[1]) +' '+ str(tmpColorConverted[2]))
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())
			else:
				self.OutTextWindow.append(tmpShape + " hasn't rmanCrandomColor2 Attribute. Create it first.")
				self.OutTextWindow.verticalScrollBar().setValue(self.OutTextWindow.verticalScrollBar().maximum())


