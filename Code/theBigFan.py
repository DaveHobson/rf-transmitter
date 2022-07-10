from serial import Serial
import sys

tx = Serial("/dev/ttyS0", 19200)

tx.write(f'{sys.argv[1]}\r'.encode())
