from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_C, SpeedRPS

motor1 = MoveTank(OUTPUT_A, OUTPUT_C)
motor1.on_for_degrees(SpeedRPS(15), 5)
