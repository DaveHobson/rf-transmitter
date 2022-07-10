# rf-transmitter

An RF transmitter to control 'The Big Fan' installed in my beer garden.
Will be expanded in future to control sunlight motorised blinds as well.

### main.py 
runs on a rpi PICO which has a Linx Technologies TXM-433-LR RF transmitter attached.
The PICO is wired to a rpi and receives commands over serial.

### serial.py 
is a Python script on the rpi which is executed via SSH, with the command passed in as the first argument.
This is executed from iOS shortcuts and my Audio Visual control system.
