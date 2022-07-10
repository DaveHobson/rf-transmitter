from machine import Pin, UART
import utime

cmdShort   = 450 # Microseconds...
cmdLong    = 900 # Microseconds...
cmdGap     = 9   # Milliseconds...
cmdRepeat  = 5   # Times to repeat RF command...

serial     = UART(0, baudrate=19200, bits=8, parity=None, stop=1)
enable     = Pin(17, Pin.OUT)
tx         = Pin(18, Pin.OUT)

fanOff     = '001011111100011001101100100011'
speedOne   = '001011111100011001101111010000'
speedTwo   = '001011111100011001101110010001'
speedThree = '001011111100011001101101010010'
speedFour  = '001011111100011001101100010011'
speedFive  = '001011111100011001101011010100'
speedSix   = '001011111100011001101010010101'


def main():
  while True:
    if serial.any():
      rx = serial.readline()
      if 'Spd1' in rx:
        sendCommand(speedOne)
      elif 'Spd2' in rx:
        sendCommand(speedTwo)
      elif 'Spd3' in rx:
        sendCommand(speedThree)
      elif 'Spd4' in rx:
        sendCommand(speedFour)
      elif 'Spd5' in rx:
        sendCommand(speedFive)
      elif 'Spd6' in rx:
        sendCommand(speedSix)
      elif 'Off' in rx:
        sendCommand(fanOff)
      else:
        print(f'Incorrect command received: {rx.decode()}')
    utime.sleep_ms(200)


def sendCommand(_cmd):
  enable.on()
  utime.sleep_ms(10)
  for _ in range(cmdRepeat):
    for i in _cmd:
      if i == '0':
        tx.on()
        utime.sleep_us(cmdShort)
        tx.off()
        utime.sleep_us(cmdLong)
      else:
        tx.on()
        utime.sleep_us(cmdLong)
        tx.off()
        utime.sleep_us(cmdShort)
    utime.sleep_ms(cmdGap)
  enable.off()


if __name__ == '__main__':
  main()
