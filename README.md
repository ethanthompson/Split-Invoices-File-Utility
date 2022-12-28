# How to Run Split Invoices

1. Install the latest version of Python for Windows (download the latest version [here](https://www.python.org/downloads/))
2. Open the Command Prompt application
    1. Click on Windows search bar
    2. Search for "CMD"
    3. Click on "Command Prompt"
3. While command prompt is open, install PyMuPDF.
    1. Paste the following into command prompt and hit "enter": py -m pip install --upgrade pip
    2. Wait for the script to stop running. You will know it is finished when you see your cursor blinking again.
    3. Paste the following into command prompt and hit "enter": py -m pip install --upgrade pymupdf
    4. Wait for the script to stop running. You will know it is finished when you see your cursor blinking again.
4. [Download this repository](https://github.com/ethanthompson/Split-Invoices-File-Utility/archive/refs/heads/main.zip) to your local machine.
5. Place the invoice file inside of the folder you just downloaded. (See "sample-input-file.pdf" for an example of where the file should reside.)
6. Double-click on the file named "split_invoices_run_me.bat". This will briefly bring up a black window and automatically close it.
7. When the script has finished running you will see a new folder named "output". This folder contains the files that have been split by the script.