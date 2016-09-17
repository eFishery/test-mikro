#!/usr/bin/python

import time
import sys
import glob
import serial


def list_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)

if not ser.isOpen():
	ser.open()

print ser.portstr

# print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

# input=1
# while 1 :
# 	# get keyboard input
# 	input = raw_input("write: ")
#         # Python 3 users
#         # input = input(">> ")
# 	if input == 'exit':
# 		ser.close()
# 		exit()
# 	else:
# 		# send the character to the device
# 		# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
# 		ser.write(input + '\r\n')
# 		out = ''
# 		# let's wait one second before reading output (let's give device time to answer)
# 		time.sleep(1)
# 		while ser.inWaiting() > 0:
# 			out += ser.read(1)
			
# 		if out != '':
# 			print "read: " + out