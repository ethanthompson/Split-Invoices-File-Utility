import fitz
import os
import glob
import shutil

# Create our output directory
if os.path.exists('output'):
  shutil.rmtree('output',ignore_errors=True)
  os.mkdir('output')
else:
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
  page.wrap_contents()
  # Check if the search term appears on the page
  if searchTerm in page.get_text("text"):
    # If search text is found, save the page number
    pageGroups.append(page.number)

numOfLoops = len(pageGroups)
i = 0

while (i < numOfLoops):

  if(i == 0):
    startingPage = 0
    endingPage = pageGroups[i]
    # print(startingPage, endingPage)
  else:
    startingPage = pageGroups[i - 1] + 1
    endingPage = pageGroups[i]
    # print(startingPage, endingPage)
  
  # This page is the one you want to scrape for the filename.
  metadataPage = pdf[startingPage]

  # Grab the "metadata" from the first page. Use the hack mentioned on line 62 to make finding data a bit easier.
  saleNum = metadataPage.get_text("text",clip=fitz.Rect(125,321,150,521))[:-3] # Trim the string to get ride of the /X num at the end. Not sure what that digit even represents.
  accountName = metadataPage.get_text("text",clip=fitz.Rect(163,221,178,461))[:-1] # Trim the string to get ride of the newline character
  invoiceNum = metadataPage.get_text("text",clip=fitz.Rect(125,30,140,150))[:-1] # Trim the string to get ride of the newline character

  # Account name clean up
  accountName = accountName.replace("/","")
  
  # Drawing below left for debugging purposes. To make coordinates easier to identify, rotate the pdfs 90 degrees counter clock-wise first. For some reason the 0,0 origin is in the top right instead of the top left.
  # invoiceNumDraw = metadataPage.add_rect_annot(fitz.Rect(125,30,140,150))

  newPDF = pdf.convert_to_pdf(from_page=startingPage, to_page=endingPage, rotate=0)
  newPDF = fitz.open("pdf",newPDF)
  newPDF.save("output/" + saleNum + "_" + invoiceNum + "_" + accountName + ".pdf")

  i+=1