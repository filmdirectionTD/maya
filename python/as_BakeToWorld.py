#-----------------------------------------
#    made by Alexandr Sknarin 18.08.2014
#    witcher.Lutojar@gmail.com
#
#    Select object transform nodes to use
#
#-----------------------------------------

import maya.cmds as cmds

def as_BakeToWorld():
  #get timeRange
  timeRangeMin = int(cmds.playbackOptions(q=True, minTime=True))
  timeRangeMax = int(cmds.playbackOptions(q=True, maxTime=True))
  
  currentObjList = cmds.ls( sl = True )
  for currentObj in currentObjList :
    cmds.select( currentObj, r=True )
    newObject = cmds.duplicate( rr = True )
    cmds.select( newObject[0], r=True )
    cmds.parent( w=True )
    #clean from constraints 
    newObjShapes = cmds.listRelatives( newObject[0], c=True, f=True)
    i=0
    for shape in newObjShapes:
        if( i>0 ):
            cmds.delete( shape )
        i += 1

    cmds.select( currentObj, r=True )
    cmds.select( newObject[0], add=True )
    newObjParentConstraint = cmds.parentConstraint( mo=True, weight=1 )
    cmds.select( newObject[0], r=True )
    cmds.bakeResults(#at=["tx", "ty", "tz", "rx", "ry", "rz" ]
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
    cmds.cutKey( newObject[0], cl=True, t=(timeRangeMin, timeRangeMax), at="sx")
    cmds.cutKey( newObject[0], cl=True, t=(timeRangeMin, timeRangeMax), at="sy")
    cmds.cutKey( newObject[0], cl=True, t=(timeRangeMin, timeRangeMax), at="sz")
    cmds.cutKey( newObject[0], cl=True, t=(timeRangeMin, timeRangeMax), at="v")
    cmds.select( newObject[0], r=True)
    cmds.setAttr( newObject[0]+".scaleX", 1 )
    cmds.setAttr( newObject[0]+".scaleY", 1 )
    cmds.setAttr( newObject[0]+".scaleZ", 1 )
    cmds.setAttr( newObject[0]+".visibility", 1 )
    cmds.delete( newObjParentConstraint )