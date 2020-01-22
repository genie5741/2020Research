import serial


arduino = serial.Serial('COM3', 9600)

while True:
    c = input()
    if c == 'q':
        break

    if c == 'on':
        arduino.write(b'1')

    if c == 'off':
        arduino.write(b'0')

    else:
        c = c.encode('utf-8')
        arduino.write()
