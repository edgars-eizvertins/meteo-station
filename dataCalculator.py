#!/usr/bin/python3

import time
from decimal import *

import dataRegistrator

timeBetweenMeasures = 5

def averageValue(valuesArray):
    return round(Decimal(sum(valuesArray) / float(len(valuesArray))), 2)

def getCalculatedData():
    temperatureList = []
    humidityList = []

    for i in range(1,5):
        data = dataRegistrator.getData()
        temperature = data["temperature"]
        humidity = data["humidity"]
        error = data["error"]
        if not error:
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