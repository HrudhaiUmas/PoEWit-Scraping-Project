import os

'''
File creates objects that will be called in app.py
- creates excel file
- data and writes to excel file
'''


i=0
while os.path.exists('cedia_dealers.txt'):
    i+=1


file = open(f'cedia_dealers{i}.txt',w)
file.write()