from selenium import webdriver
import time
import os
from openpyxl import Workbook
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows

from links import links
from parsers.parsers import PageParser

'''
Files takes in list object from links.py
will take list object and then run chromedriver on each link in list 
take data [list object] from each individual page and add to dictionary 
take dictionary and write to excel file 
'''

data=[]
chrome = webdriver.Chrome(executable_path = '/Users/aidanpak/Compsci/drivers/chromedriver')

#loop iterates through each link.. goes to page.. and extracts info
for i in links:
    chrome.get(i)
    time.sleep(2)
    parser=PageParser(chrome)
    dealer = parser.extract_dealer_info
    data.append(dealer)
    time.sleep(1)

#converting data to dataframe
dataframe= pd.DataFrame(data=data)


#writing to excel file
i=0
file = f'cedia_dealers.xlsx'
while os.path.exists(file):
    i+=1
    file= f'cedia_dealers{i}.xlsx'


wb = Workbook()

ws = wb.active
ws.append(['Dealer Name', 'Address', 'City', 'Website', 'Description'])

for r in dataframe_to_rows(dataframe):
    ws.append(r)

wb.save(filename=file)