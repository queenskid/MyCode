#!/usr/bin/env python3

vendors = ['cisco', 'juniper', 'big_ip', 'fs', 'arista', 'hp']
print('Currently the value of vendor:', vendors)
print('\nThe results of sorted() function:', sorted(vendors))
print('\nBut the value of the list has not actually changed:', vendors)

sortedvendors = sorted(vendors)
print('\nOur sorted vendor list looks like this: ', str(sortedvendors))

reverse_vedors = sorted(vendors, reverse=True)
print('\nOur reverse sorted vendor look like this:', reverse_vedors)

vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', 'fs', 'arista', 'HP', 'FS', 'hp', 'ARISTA']
print('\nOur new vendorsdeux list looks like this:', vendorsdeux)
print('\nOur second vendor list looks like this:', sorted(vendorsdeux))
