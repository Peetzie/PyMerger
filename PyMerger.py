import os
from PyPDF2 import PdfFileMerger

# Get current source dir
source_dir = os.getcwd()

merger = PdfFileMerger()

# For every item in the source dir, with .pdf extension, add them to merger.
for item in os.listdir(source_dir):
    if item.endswith("pdf"):
        merger.append(item)

new_file_name = input("Enter the name you want for the combined PDF: \n")

print("Merging PDF's. This might take a while depeinding on the size")
merger.write(new_file_name + ".pdf")
merger.close()
print("PDF Sucessfully merged. \n The newly generated PDF should be in the source dir")
