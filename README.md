Test Mikro
--------

To use (with caution), real packages still under development.
For quick test, use `assert_serial.py`

# HOW TO USE
Copy `fixtures.json.template` and define fixtures for your tests.
Assertion types:\s\s
`exact`, will check exact string of given command and expect value\s\s
`contain`, will check string given of command and expect value\s\s
`contains`, will check series of string of given command and expect values\s\s

## assert_serial.py
`python assert_serial.py --help` or `python assert_serial.py -h` to show help options
### Example:
Assert device on */dev/ttyUSB0* with fixtures at *./fixtures.json* using *115200* baudrate\s\s
`python assert_serial.py --port '/dev/ttyUSB0' --fixtures './fixtures.json' --baudrate 115200`

## Default:
port, will use first connected device in slot\s\s
fixtures, will use *./fixtures.json* path\s\s
baudrate, will use *115200* value\s\s
So you just could run it with `python assert_serial.py`

![](https://media.giphy.com/media/3oz8xzy70PJQs9jmb6/giphy.gif)