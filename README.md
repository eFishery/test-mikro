Test Mikro
--------

You could use this packages as python modules or command line.  
For simple packages, use branch `assert`  
TODO : Documentation for modules

# How To Use as Command Line
Copy `fixtures.json.template` and define fixtures for your tests.  
Command types:  
+ Non Params : `"command":"AT+TIME?"`  
+ Params : `"command":"AT+TIME={}"`, there you should put param wildcard `{}` and include params key respectivefully with ordered value in fixture object, like this:  
```
{
	"command":"AT+TIME={}",
	"params":["1474197975"],
	"assert":"contain",
	"expect":"OK"
}
```
Assertion types:  
+ `exact`, will check exact string of given command and expect value.  
+ `contain`, will check string given of command and expect value.  
+ `contains`, will check series of string of given command and expect values.  

## atduinotest
`atduinotest --help` or `atduinotest -h` to show help options
### Example:
Assert device on */dev/ttyUSB0* with fixtures at *./fixtures.json* using *115200* baudrate.  
`atduinotest --port '/dev/ttyUSB0' --fixtures './fixtures.json' --baudrate 115200`  
List ports opened
`atduinotest --list`  

## Default:
+ port, will use first connected device in slot.  
+ fixtures, will use *./fixtures.json* path.  
+ baudrate, will use *115200* value.  
So you just could run it with `atduinotest`  

![](https://media.giphy.com/media/3oz8xzy70PJQs9jmb6/giphy.gif)