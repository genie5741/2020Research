import serial


class arduino:
    def __init__(self, port, baudrate):
        self.client = serial.Serial(port, baudrate)
        self.data = []

    def on(self):
        self.client.write('1'.encode())

    def off(self):
        self.client.write('0'.encode())

    def read_output(self):
        while True:
            temp = self.client.readline().decode()
            self.data.append(temp[:-2])
