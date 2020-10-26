#first ,we have to identify the librabry that processes the PDF files - pyPDF2
import PyPDF2


with open('pdf1.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages)
    #print(reader.getPage(0))#we get the page obj here
    page = reader.getPage(0)
    page.rotateCounterClockwise(180)#there are no change in the output it is in the computer memory as long as the program excutes

    #now we have to write and save
    writer = PyPDF2.PdfFileWriter()#this allows us to write the object into memory
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)
#this is kind of useflessbut the PDF merger is useful 
