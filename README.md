# Wave_Generator
 wave generator for 2020 project  
 Code by Woojin Kim.



## Install
`pip install paramiko`  
`pip install python-ev3dev2`  

## References
[https://pypi.org/project/python-ev3dev2/](https://pypi.org/project/python-ev3dev2/)  
[https://github.com/ev3dev/vscode-ev3dev-browser](https://github.com/ev3dev/vscode-ev3dev-browser)  
[https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#move-tank](https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/motors.html#move-tank)  

## Notes
* If bluetooth of ev3 doesn't work: do firmware update. [reference](https://bricks.stackexchange.com/questions/7684/ev3-wont-connect-through-bluetooth-anymore)  


./Wave_Generator  
    /arduino  
        rangefinder.ino  # done  
    /ev3  
        movemotor.py  # done  
    /ssh  
        client.py  # done  
    arduino.py  
    ev3.py  # need to test  
    main.py