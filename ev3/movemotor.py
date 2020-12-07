from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_C, SpeedRPS


class movemotor:
    def __init__(self):
        self.motor = MoveTank(OUTPUT_A, OUTPUT_C)

    def move_for_seconds(self, speed, second):  # 각속도
        self.motor.on_for_seconds(SpeedRPS(speed), SpeedRPS(speed), second)
