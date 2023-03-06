#Data format:
#{Word_Type1:[{'endef':'Gibberish',examples:['lorem','dog']},{...}],Word_Type2:}
import requests
import json

def get_data(word_id):
    #Credentials and 
    app_id= "ea922d64"
    app_key = "edbfdb7a36ad5ddc74ff45f439367cf5"
    language="en-gb"
    fields="definitions,examples,pronunciations"
    strictMatch="false"
    data={}


    def get_json_data():
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
        json_data=json.loads(r.text)
        return json_data
    
    json_data=get_json_data()

    def get_en_definitions():                       
        en_definitions={}
        for n in range(len(json_data['results'])):#loop through results
            entries=json_data['results'][n]['lexicalEntries']
            for i in range(len(entries)):#loop through entries
                word_type=entries[i]['lexicalCategory']['text']
                example=[]
                #Loop through the main definitions
                definitions=entries[i]['entries'][0]['senses']
                for y in range(len(definitions)):
                    translation=definitions[y]['definitions'][0].capitalize()
                    #loop through the examples
                    if 'examples' in definitions[y]:
                        for m in range(len(definitions[y]['examples'])):
                            example.append(definitions[y]['examples'][m]['text'].capitalize())
                    en_definitions.setdefault(word_type,[])
                    en_definitions[word_type].append({'endef':translation,'examples':example})
                    example=[]
        return en_definitions
    
    def get_vn_definitions():


    def get_pronunciations():#Pronunciations:[]
        pronunciations=[]
        pronunciation_json=json_data['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations']
        for i in range(len(pronunciation_json)):
            pronunciations.append(pronunciation_json[i]['phoneticSpelling'])
        return pronunciations
    
    return data


#Bug-tested, only Key-Error occurs when u type yo dumbass






























































