#IMPORTING REQUIRED MODULES AND LIBRARIES
import requests

#FETCHING DATA
data=requests.get("https://httpbin.org/get")
#JSON CONTENT
data_dict=data.json()
#STORING REQUIRED DATA
user_agent=data_dict["headers"]['User-Agent']
origin=data_dict["origin"]
#PRINTING REQUIRED DATA
print("ORIGIN :",origin)
print("USER AGENT :",user_agent)
