import PyPDF2
pdf_files = ['file1.pdf', 'file2.pdf', 'file3.pdf']
pdf_writer = PyPDF2.PdfWriter()

for filename in pdf_files:
    with open(filename , 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        pdf_writer.add_page(pdf_reader.pages[0])
        pdf_writer.add_page(pdf_reader.pages[1])
        
with open('combined.pdf', 'wb') as output_file:
    pdf_writer.write(output_file)
print("Files created sucessfully")
        