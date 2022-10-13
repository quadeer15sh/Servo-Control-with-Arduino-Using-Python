import serial
import keyboard
import time

arduino = serial.Serial(port='COM11', baudrate=9600, timeout=.1)

while True:
    # data = arduino.readline()
    # s = data.decode('utf-8', 'ignore')
    # s = s.strip()
    if keyboard.is_pressed('4'):
        x = '4'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        
    
    if keyboard.is_pressed('6'):
        x = '6'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        

    if keyboard.is_pressed('8'):
        x = '8'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        
        
    if keyboard.is_pressed('2'):
        x = '2'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        
        
    if keyboard.is_pressed('9'):
        x = '9'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        
        
    if keyboard.is_pressed('7'):
        x = '7'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        
        
    if keyboard.is_pressed('3'):
        x = '3'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        
        
    if keyboard.is_pressed('1'):
        x = '1'
        print(f"Key pressed: {x}")
        arduino.write(bytes(x, 'utf-8'))
        