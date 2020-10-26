#first ,we have to identify the librabry that processes the PDF files - pyPDF2
import PyPDF2#importing the module


#storing the contents of pdf and wartermark file 
pdf_file = 'super.pdf'
watermark = 'pdf3.pdf'
merged_file = 'merged.pdf'

#open and read the contents of the pdf and watermark file 
input_file = open(pdf_file,'rb')
input_pdf = PyPDF2.PdfFileReader(input_file)

watermark_file = open(watermark,'rb')
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

#Accessing the pages of the pdf file and the watermark file to be merged, Index 0 is used to access the first page.
pdf_page = input_pdf.getPage(0)

watermark_page = watermark_pdf.getPage(0)

#Merging the pages

pdf_page.mergePage(watermark_page)

#Saving our file in the output
output = PyPDF2.PdfFileWriter()
output.addPage(pdf_page)


#The final pdf file after adding the watermark is stored in merged_file
merged_file = open(merged_file,'wb')
output.write(merged_file)

#closing the files
merged_file.close()
watermark_file.close()
input_file.close()

    


