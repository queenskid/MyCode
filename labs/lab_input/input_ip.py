#!/usr/bin/env python3
# Author: Dre

# Collect IP address information from a user, and display it back to them.
    
## Collect input from the user

user_input = input('Please enter an IPv4 IP address:') 
# user_input stores the IPv4 ip address
    
## Print out the input collected from the user

print('You told me the IPv4 address is: ' + str(user_input))

## Collecr input from user for vendor information

vendor_input = input('What is the vendor\'s name? ')
print('The vendor\'s name is ' + str(vendor_input) + '.')