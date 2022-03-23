# 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
import requests
from bs4 import BeautifulSoup
import pprint

##################################################################################################################

#METHOD1
data=requests.get("https://api.github.com/users/BhagyashreeKarale")
data_dict=data.json()
repos_data=requests.get(data_dict["repos_url"])
n=1
for i in (repos_data.json()):
    print(str(n)+"."+i['name'])
    n+=1

##################################################################################################################

#METHOD2
r = requests.get('https://api.github.com/user', auth=('BhagyashreeKarale', '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'))
x=r.json()
repos=requests.get(x['repos_url'], auth=('BhagyashreeKarale', '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'))
n=1
for i in (repos.json()):
    print(str(n)+"."+i['name'])
    n+=1

##################################################################################################################

#WEB SCRAPING
data=requests.get('https://github.com/BhagyashreeKarale?tab=repositories')
x=BeautifulSoup(data.text,"html.parser")
main=x.find('div',id="user-repositories-list")
sub=main.find('ul')
all=sub.find_all('li')
sr=1
for i in all:
    print(sr,(" ").join((i.find('a').text).split()))
    sr+=1
