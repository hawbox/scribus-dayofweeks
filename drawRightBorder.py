import scribus
x,y = scribus.getPosition(scribus.getSelectedObject())
sizex,sizey = scribus.getSize(scribus.getSelectedObject())
scribus.createLine(x+sizex,y,x+sizex,y+sizey,"line")