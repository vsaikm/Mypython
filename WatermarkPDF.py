#first ,we have to identify the librabry that processes the PDF files - pyPDF2
import PyPDF2#importing the module


template = PyPDF2.PdfFileReader(open('super.pdf','rb'))

watermark = PyPDF2.PdfFileReader(open('pdf3.pdf','rb'))

output = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf','wb') as file:
        output.write(file)
