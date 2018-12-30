# meteo-station
Small meteo station project for Raspberry PI

For installation:

Installation
Execute the following steps in the terminal:

wget abyz.me.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip 
cd PIGPIO
make
sudo make install
cd ~
wget http://abyz.me.uk/rpi/pigpio/code/DHT22_py.zip
unzip DHT22_py.zip

Run server
sudo pigpiod

Measure data
Now, humidity and temperature are measured by entering

python3 DHT22.py


To run meteostation
python3 start.py

Data will be logged inside sensor-values to folders grouped by months in files for each date
