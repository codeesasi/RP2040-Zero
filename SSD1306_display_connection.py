from machine import Pin, ADC, I2C
import neopixel, utime
from ssd1306 import SSD1306_I2C


pixel_pin = 16
pixel = neopixel.NeoPixel(Pin(pixel_pin), 1)

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(14), sda = Pin(15), freq=400000)

display = SSD1306_I2C(128, 64, i2c)
pixel[0] = (0,0,0)
pixel.write()

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

while True:
    check_move = 0
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
        
    if xValue <= 350:
        xStatus = "Move left"
        check_move = 1
        display.fill(0)
        display.text(xStatus,0,30)
        display.show()
        print(xStatus)
        
    if xValue >= 60000:
        xStatus = "Move right"
        check_move = 1
        display.fill(0)
        display.text(xStatus,0,30)
        display.show()
        print(xStatus)
        
    if yValue <= 2000:
        yStatus = "Move up"
        check_move = 1
        display.fill(0)
        display.text(yStatus,0,30)
        display.show()
        print(yStatus)
        
    if yValue >= 60000:
        yStatus = "Move down"
        check_move = 1
        display.fill(0)
        display.text(yStatus,0,30)
        display.show()
        print(yStatus)
        
    if xValue >= 33500 and yValue >= 32000 and check_move == 0:
        yStatus = "stop !"
        display.fill(0)
        display.text(yStatus,40,0)
        display.show()
        print(yStatus)
        
    check_move = 0
    print("X: " + str(xValue) + ", Y: " + str(yValue))
    utime.sleep(0.1)
    
    
    

    

  
    

