#!/usr/bin/python

from test_mikro import send_command

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input=1
while 1 :
	# get keyboard input
	input = raw_input("write: ")
	if input == 'exit':
		exit()
	else:
         out = send_command('/dev/ttyUSB0',input)
         print out