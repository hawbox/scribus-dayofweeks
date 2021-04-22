import scribus
pos = scribus.getPosition(scribus.getSelectedObject())
size = scribus.getSize(scribus.getSelectedObject())
scribus.createRect(pos[0],pos[1],size[0],size[1],"name")