from src.arduino import arduino
from src.client import client
from src.movemotor import movemotor


class server:
    def __init__(self):
        # initialize clients
        self.arduino_client = arduino("COM3", 9600)
        self.ev3_client = client("robot", "admin", "maker")
        self.ev3_client.input("motor = movemotor()")
        self.data = []

    def start_experiment(self, speed, second):
        self.arduino_client.on()
        self.ev3_client.input("motor.move_for_seconds(" + speed + "," + second + ")")

        print(self.ev3_client.read_output())  # it would be "Success"

        self.arduino_client.readline
        self.arduino_client.off()


    def visualize_graph(self):
        pass
