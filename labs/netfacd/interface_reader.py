#!/usr/bin/env python3

# importing library
import netifaces
print(netifaces.interfaces())

def ipreturn(adapter):
    #for y in netifaces.interfaces():
    return netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr']

def macreturn(adapter):
    #for y in netifaces.interfaces():
    return netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]['addr']

for x in netifaces.interfaces():
    print('\n**********Details of Interface - ' + x + ' ***********')
    try:
        print(netifaces.ifaddresses(x)[netifaces.AF_LINK][0]['addr']) # Prints MAC
        print(netifaces.ifaddresses(x)[netifaces.AF_INET][0]['addr']) # Prints IP

    except:
        print('Could not collect adapter information')
    print('')

print('enter adapter name to be presented with IP address: ')
ip= input()
print('\nYour adapter has an IP of: ' + ipreturn(ip))

print('enter adapter name to be presented with MAC address: ')
mac = input()
print('\nYour adapter has a MACaddress of: ' + macreturn(mac))
