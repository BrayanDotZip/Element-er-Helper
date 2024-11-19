import os
import random

class Element:
  def __init__(self, name, symbol, atomic_number, state_of_matter, description, fun_fact):
    self.name = name
    self.symbol = symbol
    self.atomic_number = atomic_number
    self.state_of_matter = state_of_matter
    self.description = description
    self.fun_fact = fun_fact
  def display_element(self):
    clear_terminal()
    print(f"Element: {self.name}")
    print(f"Symbol: {self.symbol}")
    print(f"Atomic Number: {self.atomic_number}")
    print(f"State of matter: {self.state_of_matter}\n")
    print(f"Here's a short description about {self.name}: {self.description}\n")
    print(f'Fun fact! {self.fun_fact}')

#Used to create a neat and clear terminal.
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

#Create function for the introduction
def main():
    while True:
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
            break
        elif choice == '2':
            quiz()
            break
        elif choice == '3':
            combine()
            break
        else:
            clear_terminal()
            print('\nInput not recognized!!! Please choose from the listed options.'.upper())


#
def learn():
    clear_terminal()
    hydrogen = Element("Hydrogen", "H", "1", "Gas", "It is the lightest element and, at standard conditions, is a gas of diatomic molecules with the formula H 2, sometimes called dihydrogen, but more commonly called hydrogen gas, molecular hydrogen or simply hydrogen. It is colorless, odorless, non-toxic, and highly combustible.", "It is the best element in the universe!")
 
    elements = {
        '1': hydrogen,
    }
    
    while True:
        clear_terminal()
        print('In this section you can choose from the list of elements and learn neat facts about them!\n')
        choice = input('Please choose the number of the element you would like to learn about!\n\n1.Hydrogen   2. Helium\n\nEnter Here:')

        if choice in elements:
            clear_terminal()
            elements[choice].display_element()

            go_back = input("\nPress 1 to go back and select another element!")
            if go_back == 1:
              break
        else:
            print("Input not recognized!!! Please choose a valid option")

def quiz():
    clear_terminal()
    print('In this section random elements will be presented to you. All you need to do is figure out the mystery element with 3 hints!')

main()