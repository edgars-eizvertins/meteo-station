#!/usr/bin/python3

import time
from datetime import datetime, date

import dataCalculator
import logger

def loop():
    while True:
        data = dataCalculator.getCalculatedData()
        temperature = data["temperature"]
        humidity = data["humidity"]

        print("Temperature: ", temperature)
        print("Humidity: ", humidity)

        logger.writeLatestValue(datetime.today(), temperature, humidity)        

def destroy():   # When program ending, the function is executed. 
    pass
 #   dataRegistrator.cleanup()

if __name__ == '__main__':
        #rint_msg()
        #getData()''
    try:
        loop()  
    except KeyboardInterrupt:
        destroy()  

