#!/usr/bin/python

import time
import sys
import glob
import serial
import json

# print with format
def print_decorator(print_type, msg):
    print_color = {
        'HEADER': '\033[95m',
        'OKBLUE' : '\033[94m',
        'OKGREEN' : '\033[92m',
        'WARNING' : '\033[93m',
        'FAIL' : '\033[91m',
        'ENDC' : '\033[0m',
        'BOLD' : '\033[1m',
        'UNDERLINE' : '\033[4m',
    }.get(print_type, '\033[0m')
    print print_color + msg + '\033[0m'

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
    print_decorator('HEADER',data['title']+'\r\n')
    test_command = 'AT'.encode() + '\r\n'
    print_decorator('UNDERLINE','initialization....')
    # warming up serial port
    ser.write(test_command)
    time.sleep(2)
    for fixture in data['fixtures']:
        ser.flushInput()
        command_test = fixture['command'].encode('utf-8')
        assert_test = fixture['assert']
        expect_test = fixture['expect']
        result_test = True
        command_byte = command_test + '\r\n'
        print_decorator('BOLD',"-----------------------")
        print_decorator('WARNING',"command: "+command_test)
        ser.write(command_byte)
        incoming_msg = ''
        time.sleep(2)
        while ser.inWaiting() > 0:
          incoming_msg += ser.read(1)
        if incoming_msg != '':
          # init variable
          incoming_msg = incoming_msg.rstrip()
          print_decorator('OKBLUE',"reply:\r\n"+incoming_msg)
          # assertion
          if assert_test == 'exact':
            result_test = incoming_msg == expect_test 
          elif assert_test == 'contain':
            result_test = expect_test in incoming_msg
          elif assert_test == 'contains':
            for contain in expect_test:
                result_test = result_test and (contain in incoming_msg)
          else:
            result_test = False
          # test passed?
          test_color = 'OKGREEN' if result_test else 'FAIL'
          print_decorator(test_color,"test passed: "+str(result_test))
          # fixture passed?
          fixture_passed = fixture_passed and result_test
          print_decorator('BOLD',"-----------------------\r\n")
    ser.close()
    test_color = 'OKGREEN' if fixture_passed else 'FAIL'
    print_decorator(test_color,"fixtures passed: "+str(fixture_passed))
    exit()