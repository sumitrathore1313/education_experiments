import PyPDF2

file = "/home/sumit/PycharmProjects/education_experiments/NRP/data/ssc_cgl_students_marks.pdf"
# creating a pdf file object
pdfFileObj = open(file, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text = pageObj.extractText()

with open("ff.txt", "w") as file:
    file.write(text)

# closing the pdf file object
pdfFileObj.close()