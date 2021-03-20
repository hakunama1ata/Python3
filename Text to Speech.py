import pyttsx3
import PyPDF2

#opening a pdf replace m3-hs300.pdf with necessary pdf name
book = open('m3-hs300.pdf', 'rb')
pdfReader= PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()