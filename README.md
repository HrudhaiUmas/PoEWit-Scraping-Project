# PoEWit-Scraping-Project
Using Selenium and the ChromeDriver to extract dealer information from Cedia.org that will be transferrred into an excel file. 



links.py 
  Establishes connection to cedia.org.. scrapes information to get number of dealers in search radius and returns a list item containing all individual dealer pages   href. 
  
write_to_excel.py 
  Iterates through each link returned by links.py.. Will then use parsers.py to scrape data from each page. Will then write data to an excel file. 
 
External Files in locators.. (dealers_page_locators.py and dealers_information_locators.py)
  dealers_page_locators.py --> Contain a class object with CSS selectors that will be called dealers_page.py.
  dealers_information_locators.py --> Contains a class object with CSS selectors that will be called in parsers.py
  
  
External Files in Pages..
  
External Files in Parsers..
  parser.py --> scrapes information from each individual dealer page and returns a list object of data



# Installation 
Make sure to download chromedriver your computer and edit the driver variable in the python scripts. 
To check out the required packages -- visit requirements.txt

