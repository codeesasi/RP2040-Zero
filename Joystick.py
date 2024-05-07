import machine, neopixel, time

pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)


xAxis = machine.ADC(machine.Pin(26))
yAxis = machine.ADC(machine.Pin(27))
led = machine.Pin(25, machine.Pin.OUT)

uart = machine.UART(0, 4800)

pixel[0] = (0,0,0)
pixel.write()

def scale_value(value, in_min, in_max, out_min, out_max):
  scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 
  return int(scaled_value / 10)

def move_up():
    return "MU0001"

def move_down():
    return "MD0002"

def move_left():
    return "ML0003"

def move_right():
    return "MR0004"

def stop():
    return "ST0000"

while True:
    xValue = scale_value(xAxis.read_u16(),0,65535,0,1100)
    yValue = scale_value(yAxis.read_u16(),0,65535,0,1100)
    
    if(xValue in [0] and yValue in [0]):
        pixel[0] = (255,0,0)
        print("Move Forward")
        transmit_code = move_up()
        uart.write(transmit_code)
        print(uart)
        pixel.write()
        
    elif(xValue in [109] and yValue in [6,7,8,9]):
        pixel[0] = (0,255,0)
        print("Move Left")
        transmit_code = move_left()
        uart.write(transmit_code)
        print(uart)
        pixel.write()
        
    elif(xValue in [18,19,20,21,22] and yValue in [109]):
        pixel[0] = (0,0,255)
        print("Move Right")
        transmit_code = move_right()
        uart.write(transmit_code)
        print(uart)
        pixel.write()
        
    elif(xValue in [109] and yValue in [109]):
        pixel[0] = (100,255,100)
        print("Move Back")
        transmit_code = move_down()
        uart.write(transmit_code)
        print(uart)
        pixel.write()
        
    else:
        pixel[0] = (0,0,0)
        print("Stop")
        transmit_code = stop()
        uart.write(transmit_code)
        print(uart)
        pixel.write()
        
    print(xValue,yValue)
    time.sleep(0.2)
