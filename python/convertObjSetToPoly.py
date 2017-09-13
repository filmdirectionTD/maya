import maya.cmds as cmds

setname = cmds.ls(sl=True)

cmds.select(setname[0], r=True)

objList = cmds.ls(sl=True)

currentSetFaces=[]

print objList
for obj in objList:
    cmds.select(obj, r=True)
    faceCount = cmds.polyEvaluate(f=True)
    print faceCount
    for i in range(0, faceCount-1):
        currentSetFaces.append(obj+".f[" + str(i) + "]")

print currentSetFaces

cmds.select(currentSetFaces)

cmds.sets(name=(setname[0]+"_prim"))