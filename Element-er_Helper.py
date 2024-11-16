import os
import random

#Used to create a neat and clear terminal.
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

#Create function for the introduction
def main():
    print('''                                                                                                     
  Z                                                         
 ZU  U                                                T  UZ 
 ZV  UUUT                             XTUUUUUUUUUUTTTTT  UZ 
 ZV     V                             WY                 UZ 
 ZV     V                             WY                 UZ 
 ZV     VZZZZZZZZZZZZZZZZZZZZZZZZZZZZZWY                 UZ 
 ZV                                                      UZ 
 ZV                  Welcome To The                      UZ 
 ZV                    Element-er                        UZ 
 ZV                      Helper!                         UZ 
 ZV                                                      UZ 
 ZV                                                      UZ 
 ZPSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSOZ 
         X                                             UZ 
         W                                             UZ 
         X                                             UZ 
         YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXVZ

                                                        
      ''') 
    print('Here you have 3 Options!\n')
    print('1. Learn - Choose from some of the coolest elements on the periodic table')
    print('2. Quiz - Test your knowledge by identifying random elements!')
    print('3. Combine - Choose and element to combine with another and see what new compound you create!\n')
    choice = input('Please choose from options 1, 2, and 3: ')
    if choice == '1':
        learn()
    elif choice == '2':
        quiz()
    elif choice == '3':
        combine()
    else:
        clear_terminal()
        print('\nInput not recognized!!! Please choose from the listed options.'.upper())
        main()

#Defining the learn function to use user input and dictionaries
def learn():
    clear_terminal()
    elements = {
        '1': 'Hydrogen\n-----\nAtomic number - 1\nState of matter - Gas',
        '2': 'Helium - '
    }
    print('In this section you can choose from the list of elements and learn neat facts about them!\n')
    choice = input('Please choose the number of the element you would like to learn about!\n\n1.Hydrogen   2. Helium\n\nEnter Here:')
    if choice in elements:
        clear_terminal()
        print(elements[choice])
    else:
        print("Input not recognized!!! Please choose a valid option")

def quiz():
    clear_terminal()
    print('In this section random elements will be presented to you. All you need to do is figure out the mystery element with 3 hints!')

main()
