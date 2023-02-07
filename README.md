# How to Run Split Invoices

1. Install the latest version of Python for your operating system.
    1. For Windows (download the latest version [here](https://www.python.org/downloads/))
2. Install PyMuPDF
    1. For Windows
        1. Click on the windows seach bar.
        2. Search for "CMD". You should see "Command Prompt" listed in your search results.
        3. Click on "Command Prompt" to open the application.
        4. With Command Prompt open, install PyMuPDF by following these steps.
        5. Enter the following command `py -m pip install --upgrade pip` and wait for the command to complete. You will know it is finished when you see your cursor blinking again.
        6. Then enter this command into the command prompt `py -m pip install --upgrade pymupdf` and wait for the command to complete.
3. [Download this repository](https://github.com/ethanthompson/Split-Invoices-File-Utility/archive/refs/heads/main.zip) to your local machine.
4. Unzip the folder and place the contents somewhere that it is easily acessible, like your desktop.
5. Place the invoice PDF file inside of the folder you just downloaded. (See "sample-input-file.pdf" for an example of where the file should reside.)
6. Double-click on the file named "run.bat". This will briefly bring up a black Command Prompt window and will automatically close it.
7. When the script has finished running you will see a new folder named "output". This folder contains the files that have been split by the script.
