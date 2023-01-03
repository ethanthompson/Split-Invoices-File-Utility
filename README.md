# How to Run Split Invoices

1. Install the latest version of Python for Windows (download the latest version [here](https://www.python.org/downloads/))
2. Open the Command Prompt application
    1. Click on the windows seach bar.
    2. Search for "CMD". You should see "Command Prompt" listed in your search results.
    3. Click on "Command Prompt" to open the application.
3. With Command Prompt open, install PyMuPDF by following these steps.
    1. Enter the following command `py -m pip install --upgrade pip` and wait for the command to complete. You will know it is finished when you see your cursor blinking again.
    3. Then enter this command into the command prompt `py -m pip install --upgrade pymupdf` and wait for the command to complete.
4. [Download this repository](https://github.com/ethanthompson/Split-Invoices-File-Utility/archive/refs/heads/main.zip) to your local machine.
5. Unzip the folder and place the contents somewhere that it is easily acessible, like your desktop.
6. Place the invoice PDF file inside of the folder you just downloaded. (See "sample-input-file.pdf" for an example of where the file should reside.)
7. Double-click on the file named "split_invoices_run_me.bat". This will briefly bring up a black window and automatically close it.
8. When the script has finished running you will see a new folder named "output". This folder contains the files that have been split by the script.
