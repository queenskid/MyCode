#!/usr/bin/env python3

# capturing user input and making sure it is set to uppercase for error handling. 
hostname = input('What is your hostname? ').upper()

# if statement checking for hostname match. 
if hostname == 'MTG': 
	print('The hostname was found to be mtg')
	print('Hostname matches expected config')

else: 
	print('That is not your hostname, sorry, try again.')

print('Exiting the script')