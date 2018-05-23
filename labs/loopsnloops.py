#!/usr/bin/env python3

# creating a dictionary with key:value pairs.
cisco_ios = {'device_type': 'cisco_ios_ssh', 'ip': '10.10.10.27', 'username': 'admin', 'password': 'passwd', 'port': 22}

# for loop iterating through dictionary values. 
for x in cisco_ios.values():
	print('\n CISCO LOGIN INFO ' + str(x))