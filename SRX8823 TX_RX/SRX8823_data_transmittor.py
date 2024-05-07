import machine
import time
import neopixel

# Define the UART pins (change these to match your setup)
TX_PIN = machine.Pin(0)  # Transmit pin (not used in receiver)
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

# Initialize UART
uart = machine.UART(0, baudrate=2400, tx=TX_PIN, rx=RX_PIN)
    
def send_data(data):
    try:
        uart.write(data)
        pixel[0] = (0,0,255)
        pixel.write()
    except Exception as err:
        print(err)
    
# Main loop
while True:
    send_data("{code:Hello world!}")
    time.sleep(0.1)
