from PyPDF2 import PdfFileReader

input1 = PdfFileReader(open("assets\\Consumer Physics General Terms and Conditions.pdf", "rb"))
print "document1.pdf has %d pages." % input1.getNumPages()
page1 = input1.getPage(0)
print str(page1)
