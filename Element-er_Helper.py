import os

#Used to create a neat and clear terminal.
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_terminal()

#Create function for the introduction
def menu():
    print('''                                                                                                 
  Z                                                         
 ZU  U                                                T  UZ 
 ZV  UUUT                             XTUUUUUUUUUUTTTTT  UZ 
 ZV     V        Welcome To The       WY                 UZ 
 ZV     V                             WY                 UZ 
 ZV     VZZZZZZZZZZZZZZZZZZZZZZZZZZZZZWY                 UZ 
 ZV                                                      UZ 
 ZV                                                      UZ 
 ZV                  Element-er                          UZ 
 ZV                    Helper!                           UZ 
 ZV                                                      UZ 
 ZV                                                      UZ 
 ZPSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSOZ 
         X                                             UZ 
         W                                             UZ 
         X                                             UZ 
         YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXVZ

                                                            
      ''') 
    
menu()