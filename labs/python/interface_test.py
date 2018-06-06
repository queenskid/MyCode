#!/usr/bin/env python3

def get_to_router(interface_index):
    interface = interface_index % 16
    if interface == 0:
        interface = 16
    return interface

def get_to_tier(tier):
    if tier == 'T1':
        tier = 'T2'
    else:
        tier = 'T1'
    return tier

def get_direction(x):
    if x >= 17:
        x = 'North'
    else:
        x = 'South'
    return x

print('The correct direction is: ', get_direction(21))
print('The correct router is: ', get_to_router(15))
print('The correct tier is: ', get_to_tier('T2'))

# def get_to_interface(router_index, direction):
#     if dir = 'North':
#         int_index = router_index
#     else:
#         int_index = router_index+16
#         return intfc_index
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
        # device_name = to_tier + 'R' = + to_device_index
        # return device_name, to_int_name
