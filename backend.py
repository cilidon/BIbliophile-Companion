import nltk
'''file_content = open("myfile.txt").read()
tokens = nltk.word_tokenize(file_content)
print tokens
'''
import PyPDF2
'''
pdfFileObject = open(r"synopsis.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

print(" No. Of Pages :", pdfReader.numPages)

pageObject = pdfReader.getPage(0)

print(pageObject.extractText())

pdfFileObject.close()
'''

pdffileobj=open('synopsis.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
x=pdfreader.numPages
pageobj=pdfreader.getPage(x-1)
text=pageobj.extractText()

print(text)