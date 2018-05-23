#!/usr/bin/env python3

# integer round initiated to 0
round = 0 

# sets up an infinite loop condition   
while(True):        
    print('What is the IPv4 address used to broadcast on a local network? ')
    # string answer collected from user
    answer = input()
    # increase the round counter
    round = round + 1     

    # logic to check if user gave correct answer
    if (answer == '255.255.255.255'): 
        print('Correct!')
        break             
    
    # logic to ensure round has not yet reached 3
    elif (round == 3):    
        print('Sorry, the answer was 255.255.255.255')
        break            

    # if answer was wrong, and round is not yet equal to 3
    else:                 
        print('Sorry. Try again!')