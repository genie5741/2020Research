from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_C, SpeedRPS


class movemotor:
    def __init__(self):
        self.flag = bool
        self.flag = 0
        self.motor = MoveTank(OUTPUT_A, OUTPUT_C)

    def move_for_seconds(self, speed, second):
        if self.flag:
            return "wait.."

        self.flag = 1
        self.motor.on_for_seconds(SpeedRPS(speed), SpeedRPS(speed), second)
        self.flag = 0

    def move(self, speed, second):
        if self.flag:
            return "wait.."

        self.flag = 1
        self.motor.on(SpeedRPS(speed), SpeedRPS(speed))
        self.flag = 0

    def stop(self):
        self.motor.stop()
