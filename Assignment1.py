import requests
from bs4 import BeautifulSoup
import pprint
import numpy as np
from prettytable import PrettyTable

data=requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
data_dict=data.json()
l=[]
n_dict={}
for i in range(len(data_dict['data'])):
    tup=(data_dict['data'][i]['Nation'],data_dict['data'][i]['Year'],data_dict['data'][i]['Population'])
    l.append(list(tup))
    n_dict[i+1]=tup


#TABLE
table = PrettyTable(['Country', 'Year', 'Population'])
for rec in l:
    table.add_row(rec)
# print(table)

#ARRAY
new_keys = [i for i in range(1,len(data_dict)+1)]

new_2d_arr = np.array([n_dict[i] for i in new_keys])
# pprint.pprint(new_2d_arr)
