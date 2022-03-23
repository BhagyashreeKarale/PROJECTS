import requests

data=requests.get("https://httpbin.org/get")
data_dict=data.json()
user_agent=data_dict["headers"]['User-Agent']
origin=data_dict["origin"]

print("ORIGIN :",origin)

print("USER AGENT :",user_agent)
