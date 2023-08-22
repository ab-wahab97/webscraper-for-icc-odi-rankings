import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


url='https://icc-cricket.com/rankings/mens/team-rankings/odi'

html=requests.get(url).text

soup=BeautifulSoup(html,'lxml')

table=soup.find('table',class_='table')

headers=table.find_all('th')
head=[]
for i in headers:
    head.append(i.text)

head1=[re.sub(r'\n','',j)[:-1] for j in head]


df=pd.DataFrame(columns=head1)



rows=table.find_all('tr')
for i in rows[1:]:
    data=i.find_all('td')
    row=[td.text for td in data]
    row1=[re.sub(r'\n','',j) for j in row]
    row1[1]=row1[1][:-3]
    

    l=len(df)
    df.loc[l]=row1



df.to_csv("CricketRanking.csv")    
    
    










   

