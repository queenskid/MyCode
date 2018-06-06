#!/usr/bin/env python3

firewall_ports = [5060, 5061, 80, 443, 22, 25565]

def addTen(x):
    return x%10

print('Currently firewall_ports looks like this: ' + str(firewall_ports))
print('\nThe results of sorted(firewall_ports, key=addTen) function:', sorted(firewall_ports, key=addTen))
print('\nBut the firewall_ports array has not actually changed: ', firewall_ports)
