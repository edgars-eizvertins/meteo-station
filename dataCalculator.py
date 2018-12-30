#!/usr/bin/python3

import time
from decimal import *

import pigpio
import DHT22

timeBetweenMeasures = 2
measuresCount = 5

def averageValue(valuesArray):
    return round(Decimal(sum(valuesArray) / float(len(valuesArray))), 2)

def getCalculatedData():
    temperatureList = []
    humidityList = []

    pi = pigpio.pi()
    s = DHT22.sensor(pi, 18, LED=16, power=8)

    for i in range(1,measuresCount):
        s.trigger()
        time.sleep(0.2)

        humidity = s.humidity()
        temperature = s.temperature()

        temperatureList.append(temperature)
        humidityList.append(humidity)
        time.sleep(timeBetweenMeasures)

    averageTemperature = 0
    if len(temperatureList) > 0:
        averageTemperature = averageValue(temperatureList)
    averageHumidity = 0
    if len(humidityList) > 0:
        averageHumidity = averageValue(humidityList)

    return { "temperature": averageTemperature, "humidity": averageHumidity }