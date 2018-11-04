#!/usr/bin/python3

import time
import dataRegistrator

def loop():
    while True:
        data = dataRegistrator.getData()        
        print("Temperature: ", data["temperature"])
        print("Humidity: ", data["humidity"])
        print("Error", data["error"])
        time.sleep(5)

def destroy():   # When program ending, the function is executed. 
    dataRegistrator.cleanup()

if __name__ == '__main__':
        #rint_msg()
        #getData()''
    try:
        loop()  
    except KeyboardInterrupt:
        destroy()  

