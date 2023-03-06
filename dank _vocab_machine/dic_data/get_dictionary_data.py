#Data format:
#{Word_Type1:[{'def':,'vndef':,examples:[]},{...}],Word_Type2:}
import requests
import json
from bs4 import BeautifulSoup

def get_json_data(word_id):
#Credentials and Parameters
    from requests.exceptions import ConnectionError
    app_id = 'ea922d64'
    app_key = 'edbfdb7a36ad5ddc74ff45f439367cf5'
    language = 'en-gb'
    fields = 'definitions,examples,pronunciations'
    strictMatch = 'false'
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
    try:
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        json_data=json.loads(r.text)
    except ConnectionError:
        connection_error="Connection Error"
        return connection_error
    if 'error' in json_data:
        json_data="Word not found"
    return json_data


def get_en_data(json_data):
    if json_data=="Connection Error":
        return json_data
    if json_data=="Word not found":
        return json_data

        
    en_data={}
    def get_en_definitions(json_data):
        en_definitions={}#Store data here
        results=json_data['results']
        for n in range(len(results)):#loop through results
            entries=results[n]['lexicalEntries']
            for i in range(len(entries)):#loop through entries
                word_type=entries[i]['lexicalCategory']['text']
                examples=[]
                #Loop through the main definitions
                definitions=entries[i]['entries'][0]['senses']
                for y in range(len(definitions)):
                    translation=definitions[y]['definitions'][0].capitalize()
                    #loop through the examples
                    if 'examples' in definitions[y]:
                        for m in range(len(definitions[y]['examples'])):
                            examples.append(definitions[y]['examples'][m]['text'].capitalize())
                    en_definitions.setdefault(word_type,[])
                    en_definitions[word_type].append({'endef':translation,'examples':examples})
                    examples=[]
        return en_definitions
    


    #main
    en_data=get_en_definitions(json_data)
    return en_data
    
def get_en_pronunciations(json_data):#Pronunciations:[]
    pronunciations=[]
    pronunciation_entries = json_data['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations']
    for i in range(len(pronunciation_entries)):
        pronunciations.append(pronunciation_entries[i]['phoneticSpelling'])
    return pronunciations


def get_vn_data(word_id):#Refactoring completed, fine so far
    #Storing the definitions in vn_definitions
    vn_definitions=[]
    url = 'https://dictionary.cambridge.org/dictionary/english-vietnamese/'+word_id
    r=requests.get(url,headers={'User-Agent':'Mozilla/5.0','Connection':'keep-alive'})
    soup=BeautifulSoup(r.text,'html.parser')
    entries=soup.find_all('span', class_='trans dtrans')
    for entry in entries:
        vn_definitions.append(entry.text.capitalize())
    return vn_definitions


def tests():
    word_id='action'
    en_data=get_en_data(word_id)
    print(en_data)



#Bug-tested, only Key-Error occurs when u type yo dumbass






























































