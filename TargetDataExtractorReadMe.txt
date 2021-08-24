Below is the explanation and setup of the program known as the Target Data Extractor.

This automated ETL pipeline was created to be able to pull the data from the retailer website then transform it before dropping it into a directory to be picked up by an SSIS package. It is completely hands free, all you do is launch it and sit back.

Target has bot protections in place, but it has a fatal flaw. When you login enough times and do the Captcha correctly, it passes you in and lets you bypass the captcha all together. This means that if you allow the browser that the automation program is running on to use your user data, Target thinks you are a human. It was difficult but it took some finesse.

The file needs to be transformed because target puts weird identifiers in the rows with 0's and also puts report information at the bottom. Rows 120-135 take care of that by deleting the report info and formatting the column so it doesn't cause issues when it is inserted by making it an integer.

After that it runs through and pulls the report out, formats it and plops it straight into the directory that the SSIS package will come looking for it.

Setup:

1. Download Python
2. Install ChromeDriver into the directory of the file.
3. Using Pypi, in your command prompt, pip install selenium, pandas, numpy. 
4. Change the username and passwords to your login for the Target vendor portal.
5. set user-data-dir to wherever you have your Chrome user data directory.
6. Set download.default_directory to where you want it to install the file.
7. At line 120, put the path where the program put the CSV file when it downloaded it.

The program is now finished and able to run.

Setup batch file to run autonomously:
1. In first directory, put where you have Python itself installed. This can be found by searching for Python in the search bar and right clicking and finding "Open file location"
2. In the second directory, put the full location of the python script.

You can now run this program autonomously using task scheduler or any other type of program executor.