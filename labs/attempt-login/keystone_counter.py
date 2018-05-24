#!/usr/bin/env python3

# creating a program that goes line by line in a file and searches for a specific expression.

# counter
loginfail = 0
loginsuccess = 0
ip = []

# assigninig the file keystone to the variable below. 

keystone_file = open('keystone.common.wsgi','r')

# creating a list of lines (EACH) found in the keystone file to the assigned variable.

keystone_file_lines = keystone_file.readlines()

# for loop iterating thorugh the lines in the file and trying to find a condition.
# with counter after every found instance.

for i in range(len(keystone_file_lines)):
    if '- - - - -] Authorization failed' in keystone_file_lines[i]:
        ip.append(keystone_file_lines[i].split(' ')[-1])    
        loginfail += 1

    elif '-] Authorization failed' in keystone_file_lines[i]:
        loginsuccess += 1

print('The number of failed log in attempts is ' + str(loginfail) + ' from IPv4 ' + ip[0])
print('The number of succesful log in attempts is ' + str(loginsuccess))
print(ip)