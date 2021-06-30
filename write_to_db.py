from selenium import webdriver
import time
import pandas as pd
import mysql.connector

from links import links, country_name, zipcode, radius
from parsers.parsers import PageParser
from credentials import db_password

'''
Files takes in list object from links.py
will take list object and then run chromedriver on each link in list 
take data [list object] from each individual page and add to datagram 
take dataframe and write to db 
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
#dataframe= pd.DataFrame(data=data, columns=['dealer_name', 'address', 'city', 'website'])



#establishing database connection and cursor
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = db_password,
    database = 'PoEWitScrapingDB'
)
cursor = db.cursor()

#creating database table
TABLE = (
    "CREATE TABLE IF NOT EXISTS `dealers` ("
    "`id` INT AUTO_INCREMENT PRIMARY KEY,"
    "`dealer_name` varchar(20) NOT NULL UNIQUE,"
    "`address` varchar(50),"
    "`city` varchar(20),"
    "`website` varchar(50),"
    "`created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    ")"
)

cursor.execute(TABLE)

#adding to DB -- add_dealer -> where data goes
# TO RESET ID -- ALTER TABLE dealers AUTO_INCREMENT = 1;
# TO DELETE -- DELETE FROM dealers where id = '4';
add_dealer = (
    "INSERT IGNORE INTO dealers "
    "(dealer_name, address, city, website) "
    "VALUES (%s, %s, %s, %s)"
)
#iterating through dataframe and appending row
for list in data:
    cursor.execute(add_dealer, list)

#committing and closing DB connection
db.commit()
db.close()
print('Data Saved to mySQL "PoEWitScrapingDB"')



#writing to mysql