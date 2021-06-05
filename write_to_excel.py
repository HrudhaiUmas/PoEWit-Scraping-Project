from selenium import webdriver
import time
import os
from openpyxl import Workbook

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
    parser=PageParser(chrome)
    time.sleep(3)
    dealer = parser.extract_dealer_info
    data.append(dealer)




#writing to excel file
i=0
file = f'cedia_dealers.xlsx'
while os.path.exists(file):
    i+=1
    file= f'cedia_dealers{i}.xlsx'


wb = Workbook()

ws = wb.active
ws.append('Dealer Name', 'Address', 'City', 'Website', 'Description')

ws.append(data)
wb.save(filename=file)