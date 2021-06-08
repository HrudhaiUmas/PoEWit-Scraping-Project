from selenium import webdriver
import time
import os
from openpyxl import Workbook
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

from links import links, country_name, zipcode, radius
from parsers.parsers import PageParser

'''
Files takes in list object from links.py
will take list object and then run chromedriver on each link in list 
take data [list object] from each individual page and add to dictionary 
take dictionary and write to excel file 
'''

data=[]
chrome = webdriver.Chrome(executable_path = 'C:/Users/mail_vfmdncr/Compsci/Drivers/chromedriver.exe')

#loop iterates through each link.. goes to page.. and extracts info
for i in links:
    chrome.get(i)
    time.sleep(2)
    parser=PageParser(chrome)
    dealer = parser.extract_dealer_info
    data.append(dealer)
    time.sleep(1)

#converting data to dataframe
dataframe= pd.DataFrame(data=data, columns=['Dealer Name', 'Address', 'City', 'Website'])


#writing to excel file
i=0
file = f'cedia_dealers_{country_name}_{zipcode}_{radius.strip()}.xlsx'
while os.path.exists(file):
    i+=1
    file= f'cedia_dealers{i}_{country_name}_{zipcode}_{radius.strip()}.xlsx'


wb = Workbook()

ws = wb.active
ws.column_dimensions['A'].width = 40
ws.column_dimensions['B'].width = 40
ws.column_dimensions['C'].width = 40
ws.column_dimensions['D'].width = 40
ws.column_dimensions['E'].width = 40






for r in dataframe_to_rows(dataframe):
    ws.append(r)

wb.save(filename=file)
chrome.close()
print(f'File Saved.. {file}')
