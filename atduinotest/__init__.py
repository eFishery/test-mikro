import time
import sys
import glob
import getopt
import serial
import json

#list ports
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

# constant
DELAY_MESSAGE = 2
CRLF = '\r\n'
DEFAULT_BAUDRATE = 115200
DEFAULT_PORT = list_ports()[0]
DEFAULT_FIXTURE = './fixtures.json'

def cli(argv=None):
    if argv == None:
      argv = sys.argv[1:]
    # get input
    port = ''
    fixtures_file = ''
    baudrate = 0
    fixture_passed = True
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["port=","fixtures=",'baudrate=','list'])
    except getopt.GetoptError:
      print_decorator('WARNING','--list | --port <port> --fixtures <fixtures_file> --baudrate <baudrate_value>')
      sys.exit(2)
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print_decorator('WARNING','--list | --port <port> --fixtures <fixtures_file> --baudrate <baudrate_value>')
         sys.exit()
      elif opt in ("-p", "--port"):
         port = arg
      elif opt in ("-f", "--fixtures"):
         fixtures_file = arg
      elif opt in ("-b", "--baudrate"):
         baudrate = arg
      elif opt in ("-l", "--list"):
         ports = list_ports();
         for port in ports:
             print(port)
         sys.exit(0)
         
    # default value
    port = port if (port != '') else DEFAULT_PORT
    fixtures_file = fixtures_file if (fixtures_file != '') else DEFAULT_FIXTURE
    baudrate = baudrate if (baudrate > 0) else DEFAULT_BAUDRATE
    # configure the serial connections (the parameters differs on the device you are connecting to)
    # the device use 8 data bit, none parity bit, and one stop bit setting.
    ser = serial.Serial(
        port=port,
        baudrate=baudrate
    )
    # check if serial is opened
    if not ser.isOpen():
        ser.open()
    # open fixtures
    with open(fixtures_file) as data_file:
        data = json.load(data_file)
        print_decorator('HEADER',data['title']+CRLF)
        test_command = 'AT'.encode() + CRLF
        print_decorator('UNDERLINE','initialization....')
        # warming up serial port
        ser.write(test_command)
        time.sleep(DELAY_MESSAGE)
        for fixture in data['fixtures']:
            ser.flushInput()
            command_test = fixture['command']
            if "{}" in command_test:
              params = fixture['params']
              command_test = command_test.format(*params)
            command_test = command_test.encode('utf-8')
            assert_test = fixture['assert']
            expect_test = fixture['expect']
            result_test = True
            command_byte = command_test + CRLF
            print_decorator('BOLD',"-----------------------")
            print_decorator('WARNING',"command: "+command_test)
            ser.write(command_byte)
            incoming_msg = ''
            time.sleep(DELAY_MESSAGE)
            while ser.inWaiting() > 0:
              incoming_msg += ser.read(1)
            if incoming_msg != '':
              # init variable
              incoming_msg = incoming_msg.rstrip()
              print_decorator('OKBLUE',"reply:"+CRLF+incoming_msg)
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
              if not result_test:
                if assert_test == 'contains':
                    expect_test = ", ".join(expect_test)
                print_decorator('OKBLUE'," ?expected: "+expect_test)
                print_decorator('FAIL'," !actual: "+incoming_msg)
              test_color = 'OKGREEN' if result_test else 'FAIL'
              print_decorator(test_color,"test passed: "+str(result_test))
              # fixture passed?
              fixture_passed = fixture_passed and result_test
              print_decorator('BOLD',"-----------------------"+CRLF)
        ser.close()
        test_color = 'OKGREEN' if fixture_passed else 'FAIL'
        print_decorator(test_color,"fixtures passed: "+str(fixture_passed))
        exit()
