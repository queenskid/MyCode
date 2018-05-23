#!/usr/bin/env python3

# variable with a string value
message = 'The movie is about to begin, we recommend '

# capture user input for their connection speed
print('What is your connection speed in Mbps?')
connection = float(input())

# if statement using the user input to determine video streaming quality recommendation. 
if connection >= 25:
    message = message + 'setting video to 4k.'

elif connection >= 5:
    message = message + 'setting video to 1080p.'

elif connection >= 2:
    message = message + 'setting video to 720p.'

else:
    message = message + 'finding another access network.'

# Prints message with appropiate statement message
print(message)

print('')

# LAB CHALLENGE

assesment = 'Your age determines you are '

print('Please enter your age to receive my professional health assesment: ')
age = float(input())

if age >= 80:
	assesment= assesment + 'Old as Balls and about to kick the bucket.'

elif age >= 60:
	assesment = assesment + 'about ready to enjoy your retirement.'

elif age >= 40:
	assesment = assesment + 'close to hitting a midlife crisis. Keep telling yourself you are in your 30s.'

elif age >= 20:
	assesment = assesment + 'a naive and healthy idiot, walking through life without realizing how awesome your age is.'

else:
	assesment = assesment + 'too young to get an accurate assesment.'

print(assesment)

