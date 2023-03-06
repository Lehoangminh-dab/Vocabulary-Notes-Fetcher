'''
Data formats:
en_data:{Word_Type1:[{'endef':'Gibberish','examples':['lorem','dog']},{...}],Word_Type2:}
vn_data:['Em yêu Bác Hồ','lắm']
Final data format:
{Word_Type1:[{'endef:'Gibberish','examples':['lorem','dog'],'vndef':['Em yêu Bác Hồ','lắm']},...],Word_Type2:
'''
from dic_data import get_dictionary_data
from update import word_update
import sys

def get_selection_total_input(data_length):
    try:
        selection_total = int(input())
    except ValueError:
        print("Please type a number from 0 to " + str(data_length))
        selection_total = get_selection_total_input(data_length)
    else:
        if selection_total < 0 or selection_total > data_length:
            print("Please type a number from 0 to " + str(data_length))
            selection_total = get_selection_total_input(data_length)
    return selection_total


def get_selections_input(selection_total,data_length):
    selections = []
    print("Which ones?")
    def get_select_input():
        try:
            selection = int(input())
        except ValueError:
            print("Please type a NUMBER from 1 to " + str(data_length))
            selection=get_select_input()
        else:
            if selection < 1 or selection > data_length:
                print("Please type a number from 1 to " + str(data_length))
                selection = get_select_input()
            if selection - 1 in selections:
                print("Please select an option that you haven't already selected")
                selection = get_select_input()
        return selection

    for i in range(selection_total):
        selections.append(get_select_input() - 1)#Actual index of selection in list 
    return selections    
    
#LOGIC starts here
def get_word_input():#All tests successful
    def check_if_exit(word_id):#Special case:EXIT
        if word_id == 'exit':
            sys.exit()

    def ask_word_input():
        word_input = input() 
        check_if_exit(word_input)
        return word_input

    #main    
    print("Please type the word on the following line:")
    print("Or type 'exit' to exit the program")
    word_input = ask_word_input()
    return word_input



def print_word_and_pronunciations(word_id,en_pronunciations):
    def print_word():
        print(word_id.capitalize()+':')
    
    def print_pronunciations():
        content = ''
        pronunciations = en_pronunciations
        pronunciation_count = 1
        for pronunciation in pronunciations:
            pronunciation_count += 1
            if pronunciation_count == len(pronunciations):
                content += pronunciation
                break
            content += pronunciation+';'
        print('/'+content+'/')
    
    #main
    def print_word_and_pronunciations_main():
        print_word()
        print_pronunciations()
    print_word_and_pronunciations_main()

def add_pronunciations(word_data,en_pronunciations):
    word_data['pronunciations'] = en_pronunciations

def print_en_data(en_data):
    print("English definitions:")
    print('-' * len("English definitions:"))#Underline
    for word_type in list(en_data):
        print('*' + word_type + ':')
        word_type_entries = en_data[word_type]
        definition_count = 0
        for word_type_entry in word_type_entries:
            definition_count += 1
            definition = word_type_entry['endef']
            print(str(definition_count) + '.' +definition)

            print(" ~Examples:")
            examples = word_type_entry['examples']
            example_count = 0
            for example in examples:
                indent = ' ' * 4  #4 Spaces
                example_count+=1
                print(indent + str(example_count) + ')' + example + '.')

    print('-'*len("English definitions:"))#Underline

def print_vn_definitions(vn_data):
    print("Vietnamese definitions:")
    print('-'*len("Vietnamese definitions:"))#Underline
    definition_count = 0
    for vn_definition in vn_data:
        definition_count += 1
        print(str(definition_count) + '.' + vn_definition)
    print('-'*len("Vietnamese definitions:"))#Underline
 
def select_word_types(word_data,en_data):
    def print_numbered_word_types():
        word_type_count = 0
        for word_type in list(en_data):
            word_type_count += 1
            print(str(word_type_count) + '.' + word_type)

    def select():
        word_type_selections=[]
        print("How many word types do you wanna write down?")
        WORD_TYPES_TOTAL = len(list(en_data))
        word_type_selection_total = get_selection_total_input(WORD_TYPES_TOTAL)
        if word_type_selection_total != WORD_TYPES_TOTAL:
            print_numbered_word_types()
            word_type_selections=get_selections_input(word_type_selection_total,WORD_TYPES_TOTAL)
        else:
            for i in range(word_type_selection_total):
                word_type_selections.append(i)
        return word_type_selections

    def add_selected_word_types(word_data,word_type_selections):
        for word_type_selection in word_type_selections:
            selected_word_type = list(en_data)[word_type_selection]
            word_data[selected_word_type] = []

    #main
    def select_word_types_main():
        print_numbered_word_types()
        word_type_selections = select()
        add_selected_word_types(word_data,word_type_selections)
    select_word_types_main()

def select_word_type_entries(word_data,en_data,word_type,vn_data):
    word_type_entries = en_data[word_type]
    def print_en_definitions():
        print('*' + word_type + ':')
        definition_count = 0
        for word_type_entry in word_type_entries:
            definition_count += 1
            definition = word_type_entry['endef']
            print(str(definition_count) + '.' + definition)

    def select_en_definitions():
        en_definition_selections = []
        print("How many English definitions do you wanna write down?")
        DEFINITIONS_TOTAL = len(word_type_entries)
        en_definition_selection_total = get_selection_total_input(DEFINITIONS_TOTAL)
        if en_definition_selection_total != DEFINITIONS_TOTAL:
            print_en_definitions()
            en_definition_selections = get_selections_input(en_definition_selection_total,DEFINITIONS_TOTAL)
        else:
            for i in range(DEFINITIONS_TOTAL):
                en_definition_selections.append(i)
        return en_definition_selections
    
    def merge_examples_and_vn_definitions(word_data,en_definition_selections):
        en_definition_count = 0
        for en_definition_selection in en_definition_selections:
            en_definition_count += 1
            selected_en_definition = word_type_entries[en_definition_selection]['endef']
            examples = word_type_entries[en_definition_selection]['examples']
            print(str(en_definition_count) + '.' + selected_en_definition)
            def print_examples():
                print(" ~Examples:")
                example_count = 0
                for example in examples:
                    example_count += 1
                    indent = ' ' *  4  #4 Spaces
                    print(indent + str(example_count) + ')' + example + '.')

            def merge_examples():
                example_selections = []
                print_examples()
                print("How many examples do you want to merge with the definition?")
                EXAMPLES_TOTAL = len(examples)
                example_selection_total = get_selection_total_input(EXAMPLES_TOTAL)
                if example_selection_total != EXAMPLES_TOTAL:
                    print_examples()
                    example_selections = get_selections_input(example_selection_total,EXAMPLES_TOTAL)
                else:
                    for i in range(example_selection_total):
                        example_selections.append(i)

                selected_examples = []
                for example_selection in example_selections:
                    selected_example = examples[example_selection]
                    selected_examples.append(selected_example)
                return selected_examples
            
            def merge_vn_definitions():
                vn_definition_selections = []
                print_vn_definitions(vn_data)
                print("How many Vietnamese definitions do you want to merge with the definition?")
                VN_DEFINITIONS_TOTAL = len(vn_data)
                vn_definition_selection_total = get_selection_total_input(VN_DEFINITIONS_TOTAL)
                if vn_definition_selection_total != VN_DEFINITIONS_TOTAL:
                    print_vn_definitions(vn_data)
                    vn_definition_selections = get_selections_input(vn_definition_selection_total,VN_DEFINITIONS_TOTAL)
                else:
                    for i in range(VN_DEFINITIONS_TOTAL):
                        vn_definition_selections.append(i)
                
                selected_vn_definitions = []
                for vn_definition_selection in vn_definition_selections:
                    vn_definition = vn_data[vn_definition_selection]
                    selected_vn_definitions.append(vn_definition)
                return selected_vn_definitions
            
            selected_examples = merge_examples()
            selected_vn_definitions = merge_vn_definitions()
            word_data[word_type].append({'endef':selected_en_definition,'examples':selected_examples,'vndef':selected_vn_definitions})

    #main
    def select_word_type_entries_main():
        print_en_definitions()
        en_definition_selections = select_en_definitions()
        merge_examples_and_vn_definitions(word_data,en_definition_selections)
    select_word_type_entries_main()

def Dank_Translator():#main function
    word_data = {}#Dictionary for storing Word Data
    word_id = get_word_input()
    #Get English Data
    json_data = get_dictionary_data.get_json_data(word_id)
    if json_data == "Connection Error":
        print("Failed to establish connection, please check your internet and try again")
        Dank_Translator()
    if json_data == "Word not found":
        print("Word not found, please check your spelling and try again")
        Dank_Translator()


    en_pronunciations = get_dictionary_data.get_en_pronunciations(json_data)
    en_data = get_dictionary_data.get_en_data(json_data)

    #Get Vietnamese data
    vn_data = get_dictionary_data.get_vn_data(word_id)
    print_word_and_pronunciations(word_id,en_pronunciations)
    print_en_data(en_data) 
    print_vn_definitions(vn_data)
    select_word_types(word_data,en_data)
    for selected_word_type in list(word_data):
        select_word_type_entries(word_data,en_data,selected_word_type,vn_data)
    add_pronunciations(word_data,en_pronunciations)
    
    #update document
    document_name = 'G:\My Drive\Vocabulary\VOCABULARY  PRIDE AND PREJUDICE\Pride and Prejudice.docx'
    #test the data structure
    print(word_data)
    word_update.update(document_name,word_id,word_data)
    
while True:
    Dank_Translator()

                
                
                
                
                
    



    




    
        



def tests():
    import random
    test_word_values=['exit','action','123']
    def get_word_input_test():#Green
        word_input=get_word_input()
        print(word_input)

    def print_en_data_test():
        en_data=get_dictionary_data.get_en_data('action')
        print(en_data)
        print('\n'*2)
        print_en_data(en_data)
    
    def print_vn_definitions_test():
        vn_data=get_dictionary_data.get_vn_data('action')
        print(vn_data)
        print('\n'*2)
        print_vn_definitions(vn_data)

    def select_word_types_test():
        en_data=get_dictionary_data.get_en_data('action')
        print(en_data)
        print('\n'*2)
        select_word_types(en_data)


    def tests_main():
        get_word_input_test()
    tests_main()

