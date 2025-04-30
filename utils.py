# Path to your PDF file
pdf_file_path = 'document.pdf'

# Open the PDF file in binary mode ('rb')
with open(pdf_file_path, 'rb') as file:
    pdf_binary_data = file.read()

with open('ouput', 'wb') as output:
    output.write(bytearray(pdf_binary_data));

print(pdf_binary_data)
