import serial


class arduino:
    def __init__(self, port, baudrate):
        self.client = serial.Serial(port, baudrate)

    def on(self):
        self.client.write('1')

    def off(self):
        self.client.write('0')
