import scribus
import calendar
weekh = calendar.weekheader(2)
weekl = weekh.split(" ")
for i in range(7):
    scribus.createText(10+(20*i),20,10,30,"%s" % i)
    scribus.setText(weekl[i-1],"%s" % i)
