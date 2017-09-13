def as_render_array(input_array):
	import maya.cmds as cmds
	import maya.mel
	maya.mel.eval("source ulRenderMenu.mel;")
	frame_array=[]
	midArray=input_array.split(",")
	for i in range(len(midArray)):
		if midArray[i]!="," and "-" not in midArray[i]:
			frame_array.append(int(midArray[i]))
		if "-" in midArray[i]:
			tmpStr = midArray[i]
			splittmpStr = tmpStr.split("-")
			tmpRangeStart = int(splittmpStr[0])
			tmpRangeEnd = int(splittmpStr[-1])+1
			tmpRange = range(tmpRangeStart, tmpRangeEnd)
			for m in tmpRange:
				frame_array.append(m)
	for framen in frame_array:
		cmds.currentTime(framen)
		maya.mel.eval("ulRenderMainProc;")
		print("FRAME No " + str(framen) + " OK\n")