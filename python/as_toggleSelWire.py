#ALexandr Sknarin 2010

def as_toggleSelWire():
  import maya.cmds as cmds
  mod_PN_switcher = 0;
  mod_PN1 = cmds.getPanel(typ="modelPanel")
  print mod_PN1[1]
  mod_switcher_v01 = cmds.modelEditor("modelPanel4", query=True, sel=True)
  print mod_switcher_v01

  if (mod_switcher_v01 == 0):
    for modPNsample in mod_PN1:
      cmds.modelEditor(modPNsample, edit=True, sel=True)
      print 1

  if (mod_switcher_v01 == 1):
    for modPNsample in mod_PN1:
      cmds.modelEditor(modPNsample, edit=True, sel=False)
      print 0