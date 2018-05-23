#!/usr/bin/env python3

# this line now prompts the user for input
ipchk = input('Apply an IP address: ') 

# if a match on '192.168.70.1' is entered, it will print the appropiate statement
if ipchk == '192.168.70.1': 
   print('\'WARNING\'Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.') 

# if any data is provided, this will test true
elif ipchk: 
   print('Looks like the IP address was set: ' + ipchk)

# if data is NOT provided
else: 
   print('You did not provide input.')

