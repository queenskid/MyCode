#!/usr/bin/env python3

# variable x is being assigned the user input. 
x = int(input('Enter a number: '))

# variable assigned a value of 1
f = 1

# for loop through a range between 1 and a value input by the user. 
# the loop will iterate from 1 to established range and continue until last number while doing the logic below. 
for i in range(1, x+1):
    f = f * i

print(str(x) + '! = ' + str(f))