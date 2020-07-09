from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_C, SpeedRPS


class movemotor:
    def __init__(self):
        self.flag = bool
        self.flag = 0
        self.motor = MoveTank(OUTPUT_A, OUTPUT_C)

    def move_for_seconds(self, speed, second):  # 각속도
        self.motor.on_for_seconds(SpeedRPS(speed), SpeedRPS(speed), second)
        print("Success")

    def move(self, speed):
        self.motor.on(SpeedRPS(speed), SpeedRPS(speed))
        print("Success")

    def stop(self):
        self.motor.stop()
        print("Stopped")

