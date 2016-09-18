import time
import serial
from . import list_ports

def send_command(port,command):
    if port == '':
        ports = list_ports()
        port = ports[0]
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port=port,
        baudrate=115200,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    if not ser.isOpen():
        ser.open()
    ser.write(command + '\r\n')
    out = ''
    # let's wait a moment reading output (let's give device time to answer)
    time.sleep(3)
    while ser.inWaiting() > 0:
      out += ser.read(1)

    return out