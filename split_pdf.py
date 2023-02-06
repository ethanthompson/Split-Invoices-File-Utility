import fitz
import os
import glob

# Create our output directory
os.mkdir('output')

filePrefix = "invoice"

# Find the PDF file in the folder
inputPDF = glob.glob("*.pdf")

# Open the PDF file
pdf = fitz.open(inputPDF[0])

# Term to key off of. This will be the word(s) that the script looks for to determine which page is the first one in a set. The word needs to be unique to the first page in the set for it to work.
searchTerm = "Transport"

# Check the number of pages in the PDF
pageCount = pdf.page_count

groupNum = 0
pageNum = 0

pageGroups = []

# Iterate over the pages in the input PDF
for page in pdf:
  # Check if the search term appears on the page
  if searchTerm in page.get_text("text"):
    # If search text is found, save the page number
    pageGroups.append(page.number)

numOfLoops = len(pageGroups)
i = 0

while (i < numOfLoops):
  print(i)

  if(i == 0):
    startingPage = 0
    endingPage = pageGroups[i]
    print(startingPage, endingPage)
  else:
    startingPage = pageGroups[i - 1] + 1
    endingPage = pageGroups[i]
    print(startingPage, endingPage)

  newPDF = pdf.convert_to_pdf(from_page=startingPage, to_page=endingPage, rotate=0)
  newPDF = fitz.open("pdf",newPDF)
  newPDF.save("output/" + filePrefix + "_" + str(i) + ".pdf")

  i+=1