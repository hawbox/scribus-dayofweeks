import scribus
scribus.setUnit(scribus.UNIT_MILLIMETERS)
l,r,t,b = scribus.getPageMargins()
w,h = scribus.getPageSize()
scribus.createText(l+((w-(l+r))/2)-120/2,(h-(t+b))/4,120,20,"journal")
scribus.setText("This journal belonging to:","journal")
scribus.setFontSize(29,"journal")
scribus.setFont("Liberation Serif Regular","journal")
scribus.setTextAlignment(scribus.ALIGN_CENTERED,"journal")
px,py = scribus.getPosition("journal")
for i in range(0,4):
  scribus.createLine(px,py+35+i*9,px+120,py+35+i*9)