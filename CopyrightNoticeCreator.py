import scribus
input = scribus.valueDialog("Enter Copyright Date and Author","Please enter the copyright date and author,use commas to seperate two parts.")
date,author = input.split(",")
info = u'Copyright \xa9 {} by {}\nAll Right Reserved.'.format(date,author)
scribus.createText(20,20,140,20,"Copyright")
scribus.setText(info,"Copyright")