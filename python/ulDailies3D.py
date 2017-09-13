import maya.cmds as cmds
from pymel.core import * 
from pymel.util import * 
import maya.mel as mm
import os

def ulDailies3D(mode, new=0):
	libPath=getEnv("ULITKALIB")
	fullName=sceneName()
	dirName=mm.eval("dirname( \""+fullName+"\")")
	
	tmpExportScene=dirName+'/killme.mb'
	
	if (selected()):
		exportSelected (exportPath=tmpExportScene, type='mayaBinary')
		if (mode=='modeling'):
			allFiles=os.listdir(dirName)
			if ('modelingDailies.mb' in allFiles and new==0): 
				openFile (dirName+'/modelingDailies.mb', force=1)
				select (allDagObjects=1)
				select ('dailies_scene', deselect=1)
				delete()
			else:
				
				openFile (libPath+"/3D/OUTPUT/FOR_DAILIES/MODELING/modeling_turnable.mb", force=1)
				saveAs (dirName+'/modelingDailies.mb', force=1)

			importFile (tmpExportScene)
			sysFile(tmpExportScene, delete=1)
			select (allDagObjects=1)
			select ('dailies_scene', deselect=1)
			mm.eval ("ulDailiesCmd(\"modeling\")")
	else:
		print ('plz, select something')


#ulDailies3D('modeling', 1)