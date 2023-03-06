import sys
import os
sys.path.append(os.path.abspath('D:\Minh\Code\Translate god\Version 1.0\V1 Beta\Main'))
from package import get_dictionary_data,update
from pprint import pprint


#Tests
def EN_test():#not working
    print('Give me the input')
    word_id=input()
    en_data=get_dictionary_data.get_en_data(word_id)
    print(en_data)

def VN_test():
    print('Give me the input')
    word_id=input()
    vn_definitions=get_dictionary_data.get_vn_data(word_id)
    print(vn_definitions)



#Main
def main():
    def display_test_options():
        print('Which test you wanna run')
        print('1.EN')
        print('2.VN')

    def select_test():
        try:
            test_num=int(input())
        except ValueError:
            print("Invalid value, please type a number from 1 to 2")
            test_num=select_test()
        else:
            if(test_num<1 or test_num>2):
                print("Invalid value, please type a number from 1 to 2")
                test_num=select_test()
        return test_num

    def execute_test(test_num):
        if test_num==1:
            EN_test()
        elif test_num==2:
            VN_test()

    display_test_options()
    test_num=select_test()
    execute_test(test_num)

main()


