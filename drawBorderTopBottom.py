import scribus
pos = scribus.getPosition(scribus.getSelectedObject())
size = scribus.getSize(scribus.getSelectedObject())
scribus.createLine(pos[0],pos[1],pos[0]+size[0],pos[1],"line")
scribus.createLine(pos[0],pos[1]+size[1],pos[0]+size[0],pos[1]+size[1],"line2")