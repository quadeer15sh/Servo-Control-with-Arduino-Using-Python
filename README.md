# Servo Control with Arduino Using Python

## Circuit Diagram
1. Connect the servo to the arduino by connecting the power (red wire) to 5v.
2. Ground (black/brown wire) to gnd. 
3. Signal (yellow/orange wire) to one of the digital pwm points. 

Circuit should like the one given below.

![image](https://hacksterio.s3.amazonaws.com/uploads/attachments/1103236/stunning_borwo-elzing_1AxSYIVIKv.png)

## Code Files
1. servo.ino: runs the servo motor rotation in 180 degrees automatically
2. servo_ip.ino: runs the servo motor rotation in 180 degrees by getting inputs from arduino.py file
3. arduino.py: used for serial communication between the computer and arduino and to provide the serial inputs to the arduino based on the user's input.

Python libraries Required (for later projects)

```
pip install pyserial
pip install numpy
pip install mediapipe
pip install opencv-python
```
