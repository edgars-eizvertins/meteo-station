#!/usr/bin/python3

import time
from datetime import datetime, date

import dataCalculator
import logger
import time

timeBetweenMeasures = 60

def loop():
    while True:
        data = dataCalculator.getCalculatedData()
        temperature = data["temperature"]
        humidity = data["humidity"]
        dateNow = datetime.today()

        print(dateNow.isoformat() + ": Temperature: ", temperature, " Humidity: ", humidity)

        logger.writeLatestValue(dateNow, temperature, humidity)

        time.sleep(timeBetweenMeasures)

def destroy():
    pass

if __name__ == '__main__':
    try:
        loop()  
    except KeyboardInterrupt:
        destroy()  

