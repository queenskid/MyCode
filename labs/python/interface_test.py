#!/usr/bin/env python3

# helps us find the remote router connection, depending on interfcae being passed to the function.
def get_to_router(interface_index):
    interface = interface_index % 16
    if interface == 0:
        interface = 16
    return interface

# dentifies the tier inside the data center.
def define_tier(tier):
    if tier == 'T1':
        tier = 'T2'
    else:
        tier = 'T1'
    return tier

# identifies the direction of the interface connection
def get_direction(x):
    if x >= 17:
        x = 'North'
    else:
        x = 'South'
    return x

print('The correct direction is: ', get_direction(21))
print('The correct router is: ', get_to_router(15))
print('The correct tier is: ', define_tier('T2'))

def get_to_interface(router_index, direction):
    if dir = 'North':
        int_index = router_index
    else:
        int_index = router_index+16
        return intfc_index
#
# def get_other_end(device, interface):
#     to_device = get_to_router(interface_number)
#     to_interface = get_direction(int_index)
        # get_device_index(device_name)
        # get_int_index(int_name)
        # #this is an example of the log being passed in to get the name of the needed log
        # device_name = 'dc1-t2-r4'
        # to_int_name = 'JRP' + str(if_index)
        # tier = device_name.split('-')[1]
        # dc = get_dc(device_name)
        # to_tier = get_to_tier(tier)
        # device_name = to_tier + 'R' + to_device_index
        # return device_name, to_int_name



# opens the file and assigns it to the variable
mytext = open('C:\\python36\longbook.txt')
# this will grab all lines in the text file and assign them to the lines variable. 
lines = mytext.readlines()
mytxt.close()

# variable assigned with a regex find statement that searches for smile or smiteself.
# this variable will be used in a for loop to search and print matches by the regex
looking_for = re.compile(r'smi[lt]e\w*')

for bored in lines:
    #
    myvariable = looking_for.search(bored)
    # if something is found in the then print the
    if myvariable:
        # the .group() method, prints the word that was matched before printing the line where it was found.
        # example: if it watched on smile
        #smile *** this joke makes me smile (line returned)
        print(myvariable.group(), '***', bored, end='')
