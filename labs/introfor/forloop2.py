#!/usr/bin/env python3

# 2 seprate list of vendors
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'alta3', 'zach', 'stuart']
approved_vendors = ['cisco', 'juniper', 'big_ip']

# for loop going through list of vendors and printing to screen with a conditional statement. 
for x in vendors:
    print("\nThe vendors is " + x, end="")
    
# if statement looking for vendors that are not in the approved vendor list. 
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")