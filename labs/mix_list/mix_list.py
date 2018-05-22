#!/usr/bin/env python3

#Creating a listwith some values in it. 

my_list = ['192.168.0.5', 5060, 'UP']

# 3 print statements that will print each index in the list. 

print('The first item in the list (IP): ' + my_list[0] )
print('The second item in the list (port): ' + str(my_list[1]) )
print('The third item in the list (state): ' + my_list[2] )

new_list = [ 5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh' ]

print('When I tried to ' + new_list[5] + ' into both ' + new_list[3] + ', ' + new_list[4] + ' I am unable to ping ' + str(new_list[0]), str(new_list[1]), str(new_list[2]))