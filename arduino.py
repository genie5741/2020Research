from ssh.client import client


class arduino:
    def __init__(self):
        c = client()

    def start_sensor(self):
        self.c.input("1")

    def stop_sensor(self):
        self.c.input("0")
