Test Mikro
--------

To use (with caution), real packages still under development.  
For quick test, use `assert_serial.py`

# HOW TO USE
Copy `fixtures.json.template` and define fixtures for your tests.  
Assertion types:  
+ `exact`, will check exact string of given command and expect value.  
+ `contain`, will check string given of command and expect value.  
+ `contains`, will check series of string of given command and expect values.  

## assert_serial.py
`python assert_serial.py --help` or `python assert_serial.py -h` to show help options
### Example:
Assert device on */dev/ttyUSB0* with fixtures at *./fixtures.json* using *115200* baudrate.  
`python assert_serial.py --port '/dev/ttyUSB0' --fixtures './fixtures.json' --baudrate 115200`

## Default:
+ port, will use first connected device in slot.  
+ fixtures, will use *./fixtures.json* path.  
+ baudrate, will use *115200* value.  
So you just could run it with `python assert_serial.py`  

![](https://media.giphy.com/media/3oz8xzy70PJQs9jmb6/giphy.gif)