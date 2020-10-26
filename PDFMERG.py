#first ,we have to identify the librabry that processes the PDF files - pyPDF2
import PyPDF2
import sys
#sys   - arguments

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')
    
pdf_combiner(inputs)

















#with open('pdf1.pdf','rb') as file:
#    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)
    #print(reader.getPage(0))#we get the page obj here
#    page = reader.getPage(0)
#    page.rotateCounterClockwise(180)#there are no change in the output it is in the computer memory as long as the program excutes

    #now we have to write and save
    #writer = PyPDF2.PdfFileWriter()#this allows us to write the object into memory
    #writer.addPage(page)
    #with open('tilt.pdf','wb') as new_file:
        #writer.write(new_file)
#this is kind of useflessbut the PDF merger is useful 
