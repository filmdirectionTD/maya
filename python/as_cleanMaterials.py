def as_cleanMaterials():
  import maya.cmds as cmds

  all_scene_geometry = cmds.ls( geometry=True, long=True )
  for geo in all_scene_geometry:
    cmds.select( geo, r=True )
    cmds.sets( e=True, forceElement="initialShadingGroup")
  
  import maya.mel
  maya.mel.eval( 'source cleanUpScene.mel;' )
  maya.mel.eval( 'scOpt_performOneCleanup({"shaderOption"})' )