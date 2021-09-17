import sys
import requests
from bs4 import BeautifulSoup


payload={
    'session-key' : 'ritikkumar99@outlook.in',
    'session-password' : 'Ritik000'
}

URL='https://www.linkedin.com/uas/login-submit'
s=requests.session()
s.post(URL,data=payload)

r=s.get('http://www.linkedin.com/nhome')
soup = BeautifulSoup(r.text,'html.parser')
print (soup.find('title'))
