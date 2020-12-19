#!/usr/bin/python3
'''Merge PDF's
Takes a folder and merges all PDF's within into one PDF'''

import argparse
import os
import sys
import PyPDF2

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir',
                    default='.',
                    help='Directory of PDF files to merge (default is .)')
parser.add_argument('-o', '--out',
                    default='merged.pdf',
                    help='Output filename')
args = parser.parse_args()
MERGEDIR = args.dir
OUTFILE = args.out

# Find all PDF's
pdfFiles = []
for filename in os.listdir(MERGEDIR):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key = str.lower)
print(f'Found {len(pdfFiles)} files.')
for filename in pdfFiles:
    print('    ', filename)
print(f'Will merge as {OUTFILE}')
proceed = input('Proceed? [Y/N]: ')
if not proceed.upper().startswith('Y'):
    sys.exit()

# Create Writer for output
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
print('Merging', end='')
for filename in pdfFiles:
    #with open(os.path.join(MERGEDIR, filename), 'rb') as pdfFileObj:
    pdfFileObj = open(os.path.join(MERGEDIR, filename), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    print('.', end='', flush=True)

print(f'Writing {OUTFILE}')
# Save the result to one PDF
with open(OUTFILE, 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
print('Complete')
