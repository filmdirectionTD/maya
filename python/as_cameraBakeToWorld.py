#-----------------------------------------
#    made by Alexandr Sknarin 15.07.2012
#    witcher.Lutojar@gmail.com
#
#    Select camera transform node to use
#    Note: script will
#
#    ToDo: add loop for work with mutiple cameras
#          check correct scales and other attrs from original camera
#          correct angle of view
#-----------------------------------------

import maya.cmds as cmds

def as_cameraBakeToWorld(fovOnly):
  currentCamera = cmds.ls(sl=True)
  newCamera = cmds.duplicate(rr=True)
  cmds.select(newCamera[0], r=True) 
  cmds.parent(w=True)
  cmds.select(currentCamera[0], r=True)
  cmds.select(newCamera[0], add=True)
  newCamParentConstrain = cmds.parentConstraint(mo=True, weight=1)
  currenCamShape = cmds.listRelatives(currentCamera[0], s=True, f=True)
  newCameraShape = cmds.listRelatives(newCamera[0], s=True, f=True)
  newCamFOVexpr = cmds.expression(s=(newCameraShape[0]+".focalLength = "+currenCamShape[0]+".focalLength;"), o=newCameraShape[0], ae=True, uc="All")
  cmds.select(newCamera[0], r=True)
  timeRangeMin = int(cmds.playbackOptions(q=True, minTime=True))
  timeRangeMax = int(cmds.playbackOptions(q=True, maxTime=True))
  cmds.bakeResults(#at=["tx", "ty", "tz", "rx", "ry", "rz", "focalLength"],
                   sm=True,
                   t=(timeRangeMin, timeRangeMax),
                   sampleBy=1,
                   disableImplicitControl=True,
                   preserveOutsideKeys=True,
                   sparseAnimCurveBake=False,
                   removeBakedAttributeFromLayer=False,
                   bakeOnOverrideLayer=False,
                   minimizeRotation=True,
                   controlPoints=False,
                   shape=True)
  cmds.cutKey(newCamera[0], cl=True, t=(timeRangeMin, timeRangeMax), at="sx")
  cmds.cutKey(newCamera[0], cl=True, t=(timeRangeMin, timeRangeMax), at="sy")
  cmds.cutKey(newCamera[0], cl=True, t=(timeRangeMin, timeRangeMax), at="sz")
  cmds.cutKey(newCamera[0], cl=True, t=(timeRangeMin, timeRangeMax), at="v")
  cmds.select(newCamera[0], r=True)
  cmds.setAttr(newCamera[0]+".scaleX", 1)
  cmds.setAttr(newCamera[0]+".scaleY", 1)
  cmds.setAttr(newCamera[0]+".scaleZ", 1)
  cmds.setAttr(newCamera[0]+".visibility", 1)
  cmds.delete(newCamParentConstrain)
  #cmds.delete(newCamFOVexpr)
  if(fovOnly==True):
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="horizontalFilmAperture")
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="verticalFilmAperture")
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="lensSqueezeRatio")
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="fStop")
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="focusDistance")
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="shutterAngle")
    cmds.cutKey(newCameraShape[0], cl=True, t=(timeRangeMin, timeRangeMax), at="centerOfInterest")

def as_check_chB(xxx):
  ccBB = cmds.checkBox(xxx, q=True, v=True)
  as_cameraBakeToWorld(ccBB)
   
def as_cameraBakeToWorld_GUI():
  as_cBTW_window = cmds.window(title="Camera Bake Options",
                               iconName="CBO",
                               topEdge=512,
                               leftEdge=512,
                               widthHeight=[200, 121],
                               sizeable=False)
  as_Laout_CBW = cmds.columnLayout(adj=True, nch=2, rs=10)
  as_fovOnly = cmds.checkBox(label="Keep FOV anim only", v=0, ann="If ON - all cameraShape animation except focal length will be deleted")
  as_command = "as_check_chB('"+as_fovOnly+"')"
  as_goButton = cmds.button(label="Bake camera to world", c=as_command)
  cmds.showWindow(as_cBTW_window)