# RaspberryPi
programs associated with Raspberry Pi


## AverageAM2320
  This program imports the module am2320\-py of https://github.com/Gozem/am2320 to enable the I2C connection and reading from the AM2320     sensor.
  
  It pulls the t, h variables (temperature and humidity) from am2320 module as sensor readings to fill the lists with 'sr' number of         sensor readings and produces the average of the sampling. Also displayed is a time stamp and the time in seconds it took to obtain and     display the readings.  
