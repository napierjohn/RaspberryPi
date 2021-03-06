import time
import am2320

# create the I2C shared bus   # this section only needed when using adafruit_am2320 module
# i2c = busio.I2C(board.SCL, board.SDA)
# am = am2320.AM2320(i2c)

tempL = []
humL = []
amT = am2320.t
amH = am2320.h
sr = int(10) #sample rate 

def tempHum():
    ti=time.time()
    for s in range(sr):
        ti=time.time()
        tempL.append(amT)
        humL.append(amH)
        time.sleep(.0001)
    print (time.asctime(time.localtime(ti)))
    print("Temperature: ",round(sum(tempL)/len(tempL),1))
    print("Humidity: ", round(sum(humL)/len(humL),1))
    print(time.time()-ti)
tempHum()
