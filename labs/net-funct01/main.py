#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime)
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds, end='\n')
            # we'll learn to write code that sends cmds to device here
            # print to create white space between loops
        print('')

def devicereboot(iplist):
    for x in iplist:
        print('Connecting to ..' + x)
    print('')
### Start our script
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run
commandpush(work2do) # call function to push commands to devices
devicereboot(work2do)

print('REBOOTING NOW!')
