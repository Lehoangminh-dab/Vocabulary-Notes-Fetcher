#Data format
#{Word_Type1:[{'def':,'vndef':,examples:[]},{...}],Word_Type2:}
from package import update
import sys
from package import VN,EN
#Vocab document name
document_name='demo.docx'
selected_word_data={}
word_id=None
en_definitions=EN.get_en_definitions()
vn_definitions=VN.get_vn_definitions()
def ask_for_word_input():
    print("Please type the word on the following line:")
    print("Or type 'exit' to exit the program")
    word_id=input()

def check_if_exit_typed():
    exit_typed=word_id=='exit'
    return exit_typed

def exit():
    sys.exit()

def check_if_word_exists():
    word_existence=EN.check_word_existence(word_id)
    return word_existence

def ask_again_for_valid_word():
    print("The word you have just entered isn't correct, please type again")
    word_id=input()

def retrieve_en_data():
    en_data=EN.get_en_translate()
    return en_data

def retrieve_vn_data():
    vn_data=VN.get_vn_translate()
    return vn_data

def print_all_en_definitions():
    print("English definitions:")
    print('-'*len("English definitions:"))
    for word_type_num in range (len(list(en_definitions))):
        print_selected_word_type(word_type_num)
        


def print_all_vn_definitions():
    print("Vietnamese definitions:")
    print('-'*len("Vietnamese definitions:"))
    for vn_definition in vn_definitions:
        vn_definition_num=str(vn_definitions.index(vn_definition)+1)
        print(vn_definition_num+'.'+vn_definition)

def print_numbered_word_types():
    for word_type in list(en_definitions):
        word_type_count=1
        print(str(word_type_count)+'.'+word_type)
        word_type_count+=1

def ask_word_type_selection():
    data_length=len(list(en_definitions))
    print('How many Word Types do you wanna write down?')
    ask_for_selection(data_length)
    selection_total=int(input())
    while check_selection_validity(selection_total,data_length)==False:
        print("Input not valid, please type a number from 1 to " + data_length)
        selection_total=int(input())
    selections=[]
    if check_if_all_selected(selection_total,data_length)==True:
        for i in range(0,data_length):
            selections.append(i+1)
    else:
        for i in range(selection_total):
            print("Which ones?")
            word_type_selection=int(input())
            while check_selection_validity(word_type_selection,selection_total)==False:
                print("Input not valid, please type a number from 1 to " + selection_total)
                word_type_selection=int(input())
            selections.append(word_type_selection)

            

#Start of mess
def check_selection_validity(user_input,data_length):
    if user_input<=data_length:
        return True
    if user_input>data_length:
        return False
    #missing input != int scenario

def receive_selection_input(data_length):
    selection_number=None
    def check_selection():
        try:
            selection_number=int(input())
        except ValueError:
            print("Input not valid, please type a number from 1 to " + data_length)
    while selection_number<1 or selection_number>data_length:
        print("Input not valid, please type a number from 1 to " + data_length)

def ask_for_selection(data_length):
    selection_total=None
    selections=[]
    def ask_for_selection_number():
        try:
            selection_total=int(input())
        except ValueError:
            print("Input not valid, please type a number from 1 to " + data_length)

    ask_for_selection_number()
    while check_selection_validity(selection_total,data_length)==False:
        print("Input not valid, please type a number from 1 to " + data_length)
        selection_total=int(input())

    if check_if_all_selected(selection_total,data_length)==True:
        for i in range(0,data_length):
            selections.append(i+1)
    else:
        for i in range(selection_total):
            print("Which ones?")
            try:
                selection_number=int(input())
            except ValueError:
                print("Input not valid, please type a number from 1 to " + selection_total)
            while check_selection_validity(selection_number,selection_total)==False:
                print("Input not valid, please type a number from 1 to " + selection_total)
                selection_number=int(input())
            selections.append(selection_number)

    return selections
    

def check_if_all_selected(user_input,data_length):
    if user_input==data_length:
        return True
    else:
        return False
#End of mess



def print_selected_word_type(word_type_num):
    word_type=list(en_definitions)[word_type_num]
    print('*'+word_type+':')

def print_selected_definition(word_type_num,definition_num):
    definition=en_definitions[list(en_definitions)[word_type_num]][
                              definition_num]['def']
    print(str(definition_num)+'.'+definition)

def print_definition_examples(word_type_num,definition_num):
    examples=en_definitions[list(en_definitions)[word_type_num]][  
                            definition_num]['examples']
    for example in examples:
        example_num=str(examples.index(example)+1)
        print(example_num+')'+example+'.')
     


  




