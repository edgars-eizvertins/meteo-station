#!/usr/bin/python3

import os

sensorName                  = "living-room"
latestTemperatureFilePath = "sensor-values/temperature_" + sensorName + "_latest_value.csv"
latestHumidityFilePath    = "sensor-values/humidity_" + sensorName + "_latest_value.csv"
csvHeaderTemperature       = "timestamp,temperature_in_celsius\n"
csvHeaderHumidity          = "timestamp,relative_humidity\n"
csvEntryFormat             = "{:%Y-%m-%d %H:%M:%S},{:0.1f}\n"

def writeHeader(fileHandle, csvHeader):
	fileHandle.write(csvHeader)

def writeValue(fileHandle, datetime, value):
	line = csvEntryFormat.format(datetime, value)
	fileHandle.write(line)
	fileHandle.flush()

def openFileEnsureHeader(filePath, mode, csvHeader):
	f = open(filePath, mode, os.O_NONBLOCK)
	if os.path.getsize(filePath) <= 0:
		writeHeader(f, csvHeader)
	return f

def writeLatestValue(time, temperature, humidity):
	with openFileEnsureHeader(latestTemperatureFilePath, 'a', csvHeaderTemperature) as fileHandle:  #open and truncate
		writeValue(fileHandle, time, temperature)
	with openFileEnsureHeader(latestHumidityFilePath, 'a', csvHeaderHumidity) as fileHandle:  #open and truncate
		writeValue(fileHandle, time, humidity)
