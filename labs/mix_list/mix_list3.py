#!/usr/bin/env python3

#
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)

#
list1.extend(['juniper'])
print(list1)

# appendig a list inside list1
# priting the 4th index in list1
# priting the first index[o] inside the list inside of list1
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print(list1[4])
print(list1[4][0])

# List with animal names and a print statement to display the values inside the list named "animals". 
animals = ['cat', 'dog', 'fly', 'bee', 'bug']
print(animals)