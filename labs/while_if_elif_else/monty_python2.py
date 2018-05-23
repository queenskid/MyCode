#!/usr/bin/env python3

# integer round initiated to 0
round = 0
name = input('Welcome to my guessing game, What is your name? ')

# sets up an infinite loop condition
while(True):
	
   # increase the round counter
   round = round + 1
   print( name + ' , finish the movie title, "Monty Python\'s The Life of _______"')
   # string answer collected from user
   answer = input() 

   # logic to check if user gave correct answer
   if (answer == 'Brian'):
      print('Correct')
      break

   # logic to ensure round has not yet reached 3
   elif(round==3):
      print('Sorry ' + name + ', the answer was Brian.')
      break

   # if answer was wrong, and round is not yet equal to 3
   else:
      print('Sorry! Try again')