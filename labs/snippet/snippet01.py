#!/usr/bin/env python3

a = 'trying to split these string'
# split methos will split the string at the white space and put them in a list.
a = a.split(' ')
# print to screen the newly edited varible being split
print(a)

# the join method will join the words in the list a.
b = '-'.join(a)
print(b)

print('')

def remove():
    ip = []
    max_ip = 3
    while len(ip) < max_ip:
        entered = input('Enter a block of ip address: ')
        entered = entered.split('.')
        ip.append(entered)
        print(ip)
    else:
        print('All IPs have been reserved')


remove()
