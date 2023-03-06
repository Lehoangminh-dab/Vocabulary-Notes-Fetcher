import requests
from bs4 import BeautifulSoup
def get_vn_definitions(word_id):
    #Storing the definitions in vnTranslations
    vnTranslations=[]
    url = 'https://dictionary.cambridge.org/dictionary/english-vietnamese/'+word_id
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0','Connection':'keep-alive'})
    soup=BeautifulSoup(r.text,'html.parser')
    entries=soup.find_all('span', class_='trans dtrans')
    for entry in entries:
        vnTranslations.append(entry.text.capitalize())
    return vnTranslations
