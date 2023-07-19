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

  # OLD Coordinates

  # Grab the "metadata" from the first page. Use the hack mentioned on line 62 to make finding data a bit easier.
  # saleNum = metadataPage.get_text("text",clip=fitz.Rect(125,321,150,521))[:-3] # Trim the string to get ride of the /X num at the end. Not sure what that digit even represents.
  # invoiceNum = metadataPage.get_text("text",clip=fitz.Rect(125,30,140,150))[:-1] # Trim the string to get ride of the newline character
  # accountName = metadataPage.get_text("text",clip=fitz.Rect(163,221,178,461))[:-1] # Trim the string to get ride of the newline character

  # NEW Coordinates

  saleNum = metadataPage.get_text("text",clip=fitz.Rect(370,118,450,132))[:-3] # Trim the string to get ride of the /X num at the end. Not sure what that digit even represents.
  invoiceNum = metadataPage.get_text("text",clip=fitz.Rect(650,118,750,132))[:-1] # Trim the string to get ride of the newline character
  accountName = metadataPage.get_text("text",clip=fitz.Rect(365,150,620,165))[:-1] # Trim the string to get ride of the newline character

  # Debugging stuff

  # saleNum = "123"
  # invoiceNum = "123"
  # accountName = "Account_" + str(i)

  # saleNumDraw = metadataPage.add_rect_annot(fitz.Rect(370,118,450,132))
  # invoiceNumDraw = metadataPage.add_rect_annot(fitz.Rect(650,118,750,132))
  # accountNumDraw = metadataPage.add_rect_annot(fitz.Rect(365,150,620,165))

  # Account name clean up
  accountName = accountName.replace("/","").replace("*", "")

  newPDF = pdf.convert_to_pdf(from_page=startingPage, to_page=endingPage, rotate=0)
  newPDF = fitz.open("pdf",newPDF)
  newPDF.save("output/" + saleNum + "_" + invoiceNum + "_" + accountName + ".pdf")

  i+=1