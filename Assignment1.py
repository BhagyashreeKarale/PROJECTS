#IMPORTING REQUIRED MODULES AND LIBRARIES
import requests
from bs4 import BeautifulSoup
import pprint
import numpy as np
from prettytable import PrettyTable

#FETCHING DATA USING REQUEST MODULE(GET METHOD)
data=requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
data_dict=data.json()
main_data=data_dict['data']
mainlist=[]
n_dict={}
#CREATING NECESSARY DATA STRUCTURES FOR CREATING TABLE AND 2D ARRAY
for i in range(len(main_data)):
    tup=(main_data[i]['Nation'],main_data[i]['Year'],main_data[i]['Population'])
    mainlist.append(list(tup))
    n_dict[i+1]=tup


#TABLE
table = PrettyTable(['Country', 'Year', 'Population'])#TABLE HEADERS
for rec in mainlist:
    table.add_row(rec)#ADDING ROWS TO THE TABLE
print(table)#PRINTING TABLE

#ARRAY
new_keys = [i for i in range(1,len(main_data)+1)]

new_2d_arr = np.array([n_dict[i] for i in new_keys])#CREATING 2D ARRAY
#PRINTING 2D ARRAY
for row in new_2d_arr:
   for column in row:
      print(column,end = " ")
   print()
