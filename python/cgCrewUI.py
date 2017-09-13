import os, subprocess, random

import maya.OpenMaya as OpenMaya
import maya.mel as mel
import maya.cmds as cmds
from functools import partial

from mayaUiProc import *

selfPrefix = 'alfGen_'
MainWindowName = selfPrefix + 'MainWnd'

class cgcrewAlfGen(object):
    
    def __init__(self):
        self.a = 0
        
        self.rootDir = cmds.workspace(q=True, rootDirectory=True )[:-1]
        
        self.jobParam = dict()
        
        self.initParameters()
        
        self.ui = self.buildUI()
        
    def buildUI(self):
        
        cw1 = 120
        cw2 = 60
        cw3 = 20
        mr_hi = 8
        
        self.deleteUI(True)
        
        self.winMain = cmds.window(MainWindowName,
                                   title="Alfred script generator for Maya",
                                   menuBar=True,
                                   retain=False,
                                   widthHeight=(320, 190))
        
        self.mainMenu = cmds.menu(label="Commands", tearOff=False)
        cmds.menuItem(label="Render Globals ...", command = maya_render_globals)
        cmds.menuItem(label="Submit Job", command = self.submitJob)
        cmds.menuItem(divider=True)
        cmds.menuItem(label="Close", command = self.deleteUI)
        
        #form = cmds.formLayout('f0', numberOfDivisions=100)
        proj = cmds.columnLayout('c0', columnAttach=('left', 0), rowSpacing=2, adjustableColumn=True, height=50)
        cmds.textFieldGrp(cw =(1, 70), adj=2, label='Project Root :', text=self.rootDir, editable=False )
        
        #cmds.setParent('..')
        #cmds.setParent('..')
        
        #Setup Tabs
        #tab = cmds.tabLayout('t0', scrollable=True, childResizable=True)
        
        #Job Tab
        #tab_job = cmds.columnLayout('tc0', columnAttach=('left',0), rowSpacing=0, adjustableColumn=True)
        #cmds.frameLayout('fr1', label=' Parameters ', borderVisible=True, borderStyle='etchedIn', marginHeight=mr_hi)
        #cmds.columnLayout('fc1', columnAttach=('left', 0), rowSpacing=0, adjustableColumn=True)
        
        cmds.intFieldGrp ('job_range', cw=((1, cw1), (2, cw2), (3, cw2)), nf = 3,
                          label = 'Start/Stop/FPR ',
                          value1 = self.jobParam['job_start'],
                          value2 = self.jobParam['job_end'],
                          value3 = self.jobParam['job_size'],
                          cc = (partial(setDefaultIntValue3, selfPrefix, ('job_start', 'job_end', 'job_size'), self.jobParam)))
        
        cmds.checkBoxGrp ('start_paused', cw = ((1, cw1),(2, cw1*2)),
                          label = 'Start Paused ',
                          value1 = self.jobParam['start_paused'],
                          cc = partial(setDefaultIntValue, selfPrefix, 'start_paused', self.jobParam))
        
        cmds.checkBoxGrp ('to_top', cw = ((1, cw1),(2, cw1*2)),
                          label = 'To top Queue list ',
                          value1 = self.jobParam['to_top'],
                          cc = partial(setDefaultIntValue, selfPrefix, 'to_top', self.jobParam))
        
        cmds.checkBoxGrp ('submit_close', cw = ((1, cw1),(2, cw1*2)),
                          label = 'Close dialog after submit ',
                          value1 = self.jobParam['submit_close'],
                          cc = partial(setDefaultIntValue, selfPrefix, 'submit_close', self.jobParam))
        
        #cmds.setParent('..')
        #cmds.setParent('..')
        #cmds.setParent('..')
        
        #cmds.tabLayout(tab, edit=True,
        #               tabLabel=((tab_job, 'Job'),)
        #                )
        #cmds.setParent(form)
        
        cmds.separator(h=15)
        
        btn_sbm = cmds.button(label='Submit', command=self.submitJob, ann='Generate alfred script and submit to secretary')
        btn_cls = cmds.button(label='Close', command=self.deleteUI)
        
        cmds.showWindow(self.winMain)
        return 0
    
    def initParameters(self):
        self.jobParam['jobName'] = getMayaSceneName()
        self.jobParam['job_start'] = getDefaultIntValue(selfPrefix, 'job_start', 1)
        self.jobParam['job_end'] = getDefaultIntValue(selfPrefix, 'job_end', 100)
        self.jobParam['job_step'] = getDefaultIntValue(selfPrefix, 'job_step', 1)
        self.jobParam['job_size'] = getDefaultIntValue(selfPrefix, 'job_size', 5)
        self.jobParam['start_paused'] = getDefaultIntValue(selfPrefix, 'start_paused', 0)
        self.jobParam['to_top'] = getDefaultIntValue(selfPrefix, 'to_top', 0)
        self.jobParam['submit_close'] = getDefaultIntValue(selfPrefix, 'submit_close', True)
        self.jobParam['mayaSceneFile'] = os.path.join(self.rootDir, getMayaSceneName(withoutSubdir=False, withoutExt=False)).replace('\\', '/')
        self.jobParam['renderSequenceName'] = getRenderImageOptions()[0]
        self.jobParam['renderImageFormat'] = getRenderImageOptions()[2]
        self.jobParam['padding'] = getRenderImageOptions()[1]
        self.jobParam['renderOutputDir'] = getMayaOutputRenderDir()
        self.jobParam['mayaVersion'] = os.getenv('MAYA_VERSION')
        return 0
    
    def generateAlfScript(self):
        
        def createSubtask(start, end):
            curTask = '\t\tTask -title {maya.%s-%s} -subtasks {\n\t\t\t} -cmds {\n' % (start, end)
            curTask += '\t\t\t\t\tRemoteCmd {//server/bin/cmd/mayaBatch.cmd %s %s %s \"%s\" \
\"%s\" \"%s\"} -service {maya} -atmost 1 -tags {intensive}\n' % (self.jobParam['mayaVersion'],
                                                          start,
                                                          end,
                                                          self.jobParam['renderOutputDir'],
                                                          self.jobParam['mayaSceneFile'],
                                                          self.rootDir)

#            curTask += '\t\t\t} -preview {sv.cmd \
#\"%s/%s.%s.%s:%s:%s:1\"\n\t\t\t}\n' % (self.jobParam['renderOutputDir'],
#                                          self.jobParam['renderSequenceName'],
#                                          self.jobParam['padding'],
#                                          self.jobParam['renderImageFormat'],
#                                          start,
#                                          end)

            curTask += '\t\t\t}\n'
            return curTask
        
        tempDir = os.getenv('TEMP')
        alfScriptFileName = self.jobParam['jobName'] + '_' + str(random.randrange(1, 65535)) + '.alf'
        alfScriptFilePath = os.path.join(tempDir, alfScriptFileName)
        alfScriptFile = open(alfScriptFilePath, mode='w')
        header = '##AlfredToDo 3.0\n\
Job -title {%s(maya job)} \
-comment {#Created by CGCrew Alf Start Author:Vladimir Moskalenko} \
-envkey {} \
-metadata {} -dirmaps {} -service {maya} -tags {} -atleast 1 -atmost 1 -init {\n\
} -subtasks {\n' % (self.jobParam['jobName'])
        footer = '} -cleanup {\n}'
        alfScriptFile.write(header)
        start = self.jobParam['job_start']
        end = self.jobParam['job_end']+1
        inc = self.jobParam['job_size']
        for i in range(start, end, inc):
            curTaskStart = str(i)
            curTaskEnd = str(i + inc - 1)
            if int(curTaskEnd) >= end:
                taskStroke = createSubtask(curTaskStart, str(end))
            else:
                taskStroke = createSubtask(curTaskStart, curTaskEnd)
            
            alfScriptFile.write(taskStroke)
        
        alfScriptFile.write(footer)
        alfScriptFile.close
        
        return alfScriptFilePath
    
    def submitJob(self, param):
        self.initParameters()
        alfScriptFilePath = self.generateAlfScript()
        cmd = ['comrade64.exe', alfScriptFilePath]
        if self.jobParam['start_paused']:
            cmd.append('--paused')
        if self.jobParam['to_top']:
            cmd.append('--totop')
        subprocess.call(cmd)
        os.remove(alfScriptFilePath)
        
        if self.jobParam['submit_close']:
            self.deleteUI(True)
        return 0
    
    def deleteUI(self, param):
        winMain = MainWindowName
        if cmds.window(MainWindowName, exists=True):
            cmds.deleteUI(MainWindowName, window=True)
        if cmds.windowPref(MainWindowName, exists=True):
            cmds.windowPref(MainWindowName, remove=True)
        return 0
    

def getRenderGlobals():
    mel.eval("unifiedRenderGlobalsWindow")
    
print 'AlfGen sourced ...'
