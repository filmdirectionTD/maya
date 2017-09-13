# made by Alexandr Sknarin 
# witcher.Lutojar@gmail.com 
# 31.03.2011
# version 0.4
# use on your own risk

# How to use:
# bind it to hotkey or marking menu or shelf button or enywhere else
# script works as toggle:
# select polygonal object you want to tweak then push hotkey/shelfbutton etc..
# text "Live edit mode ON" in lower left corner of viewport will indicate that you in Live Edit mode
# push same hotkey/shelfbutton etc.. to turn Live Edit mode off

# Note:
# - Works only with polygons
# - Worked only with objects what was selected when script has been evaluated
#     if you want tweak other objects first turn Live Edit offm select other objects, and then turn it on again

def as_live_edit ():
  import maya.cmds as cmds 

  #switcher check
  as_live_switch = cmds.objExists('as_tmp_obj_LE'); # if 0 - start liveEdit, if 1 - stop liveEdit and delete all stuff

  as_liveEdit_objects = cmds.ls(sl=1) #array of objects to liveEdit
  as_live_number_objects = len(as_liveEdit_objects) #length of array


  #start liveEdit
  if as_live_switch == 0:
    #making duplicates
    for i in range(len(as_liveEdit_objects)):
      as_tmp_obj = as_liveEdit_objects[i]
      print as_tmp_obj
      cmds.duplicate(as_tmp_obj, rr=True, n='as_tmp_obj'+str(i))
  
    #if here one object, rename it properly
    if as_live_number_objects == 1:
      cmds.select('as_tmp_obj0')
      cmds.rename('as_tmp_obj_LE')


    #if here multiple objects, combining and rename
    if as_live_number_objects > 1:
      #selecting tmp objects
      for i in range(len(as_liveEdit_objects)):
        if i == 0:
          cmds.select('as_tmp_obj'+str(i), r=True)
        if i > 0:
          cmds.select('as_tmp_obj'+str(i), tgl=True)
      cmds.polyUnite(ch=0, n='as_tmp_obj_LE')
  
    #Hiding, making live
    cmds.select('as_tmp_obj_LE')
    cmds.setAttr('as_tmp_obj_LE'+'.visibility', 0)
    cmds.makeLive()
    
    #turning on label
    cmds.headsUpDisplay('HUD_as_liveedit', section=5, block=1, label='Live Edit Mode ON')

    #Go Into TWEAK MODE
    import maya.mel
    maya.mel.eval("STRSTweakModeToggle;")
	
    #Selecting original objects
    cmds.select(as_liveEdit_objects)
    cmds.selectMode(component=True)
    cmds.selectType(smp=True, sme=False, smf=False, smu=False, pv=True, pe=False, pf=False, puv=False)

#delete tmp object
  if as_live_switch == 1:
    cmds.delete('as_tmp_obj_LE')
    #Delete label
    cmds.headsUpDisplay('HUD_as_liveedit', rem=True)
    import maya.mel
    maya.mel.eval("STRSTweakModeToggle;")
    cmds.selectMode(o=True)
