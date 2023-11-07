import PyPDF2
import sys
import os

path = './pdfsToMerge'
output_path = './mergedPdfs'
merger = PyPDF2.PdfMerger()

for file in os.listdir(path):
    if file.endswith('.pdf'):
        pdf_path = os.path.join(path, file)
        with open(pdf_path, 'rb') as pdf_file:
            merger.append(pdf_file)

output_path_pdf = os.path.join(output_path, 'combinedPdfDocs.pdf')
merger.write(output_path_pdf)
merger.close()
