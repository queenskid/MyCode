#!/usr/bin/env python3

#print('Please enter a Layer2 network protocol: ')


while(True):
   protocol = input('Please enter a Layer2 protocol: ')
   if protocol == 'eth':
    print('ethernet protocol allowed')
    break    

   if protocol == 'fc':
     print('fiber channel NOT allowed')     
     print('try again')
     continue     

   if protocol == 'ifb':
     print('infiniband NOT allowed')
     print('try again')
     continue
  
   if protocol == 'otn':
     print('Optical Network allowed')
     break     

   else:
     print('No idea what that technology that is')
     continue
			