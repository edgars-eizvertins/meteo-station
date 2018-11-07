#!/usr/bin/python3

import os

sensorName = "living-room"
csvHeaderTemperature = "timestamp,temperature_in_celsius\n"
csvHeaderHumidity = "timestamp,relative_humidity\n"
csvEntryFormat = "{:%Y-%m-%d %H:%M:%S},{:0.2f}\n"

def getFilePath(time):
	path = "sensor-values/" + ("{0:%Y-%m}".format(time)) + "/"
	if not os.path.exists(path):
		os.makedirs(path)
	return path

def getTemperatureFilePath(time):
	return getFilePath(time) + "temperature_" + sensorName + "_" + ("{0:%Y-%m-%d}".format(time)) + ".csv"

def getHumidityFilePath(time):
	return getFilePath(time) + "humidity_" + sensorName + "_" + ("{0:%Y-%m-%d}".format(time)) + ".csv"

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
	with openFileEnsureHeader(getTemperatureFilePath(time), 'a', csvHeaderTemperature) as fileHandle:
		writeValue(fileHandle, time, temperature)
	with openFileEnsureHeader(getHumidityFilePath(time), 'a', csvHeaderHumidity) as fileHandle:
		writeValue(fileHandle, time, humidity)
