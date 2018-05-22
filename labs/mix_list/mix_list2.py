#!/usr/bin/env python3

# two list of protocols, to demostrate extend and append method. 

proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
print(proto[1])

# Using append and extend to see how the different methods execute. 

# Append will add 'dns' to the end of the list to both the proto and protoa list created. 
proto.append('dns')
protoa.append('dns')
print(proto)

# Creating a list of intergers to use extend and append method on the previous list. 

# list of port for the protocols above
proto2 = [22, 80, 443, 53] 

# The .extend method will add values of the proto2 list to the end of the proto list. 
proto.extend(proto2)
print(proto)

# the .append methos will add the proto2 list to the proto list as a list inside proto. 
protoa.append(proto2)
print(protoa)