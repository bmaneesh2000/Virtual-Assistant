import requests
from bs4 import BeautifulSoup
i=input()
url="https://en.wikipedia.org/wiki/"+i
r=requests.get(url) 
c=r.content
s=BeautifulSoup(c,'html.parser')
f=s.find("p", class_=False, id=False)
print(f.text)
