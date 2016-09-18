#!/usr/bin/python

import time
import sys
import glob
import serial
import json

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

fixture_passed = True
with open('./fixture.json') as data_file:    
    data = json.load(data_file)
    print data['title']+'\r\n'
    test_command = 'AT'.encode() + '\r\n'
    print 'initialization....'
    # warming up serial port
    ser.write(test_command)
    time.sleep(2)
    for fixture in data['fixtures']:
        ser.flushInput()
        command_test = fixture['command'].encode('utf-8')
        assert_test = fixture['assert']
        expect_test = fixture['expect']
        command_byte = command_test + '\r\n'
        print "-----------------------"
        print "command: "+command_test
        ser.write(command_byte)
        incoming_msg = ''
        time.sleep(2)
        while ser.inWaiting() > 0:
          incoming_msg += ser.read(1)
        if incoming_msg != '':
          # init variable
          incoming_msg = incoming_msg.rstrip()
          print "reply:"
          print incoming_msg
          # assertion
          if assert_test == 'exact':
            result_test = incoming_msg == expect_test 
          elif assert_test == 'contain':
            result_test = expect_test in incoming_msg
          else:
            result_test = False
          print "test passed: "+str(result_test)
          fixture_passed = fixture_passed and result_test
          print "-----------------------\r\n"
    ser.close()
    print "fixtures passed: "+str(result_test)
    exit()