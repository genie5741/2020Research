from src.arduino import arduino
from src.client import client
from src.movemotor import movemotor
import pandas as pd


class server:
    def __init__(self):
        # initialize clients
        self.arduino_client = arduino("COM3", 9600)
        self.ev3_client = client("robot", "admin", "maker")
        self.ev3_client.input("motor = movemotor()")
        self.data = []

    def start_experiment(name, self, speed, second):
        self.arduino_client.on()
        self.ev3_client.input("motor.move_for_seconds(" + speed + "," + second + ")")

        print(self.ev3_client.read_output())  # it would be "Success"

        self.data += self.arduino_client.read_output()

        dataframe = pd.DataFrame(self.data)
        dataframe.to_csv(".\result\{0}.csv".format(name), header=False, index=False)

        self.arduino_client.off()

    def visualize_graph(self):
        pass
