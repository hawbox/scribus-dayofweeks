import scribus
obj = scribus.getSelectedObject()
scribus.setText(scribus.getText(obj).replace("\t"," "))