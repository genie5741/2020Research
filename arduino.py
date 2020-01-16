from ssh.client import client


class arduino:
    def __init__(self):
        c = client()

    def start_sensor(self):
        self.c.input("on")

    def stop_sensor(self):
        self.c.input("off")
