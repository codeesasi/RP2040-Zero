import machine
import time
import neopixel

RX_PIN = machine.Pin(13)  # Receive pin (connected to the receiver module)
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

# Function to receive data
def receive_data():
    if uart.any():
        pixel[0] = (0,255,0)
        pixel.write()
        return uart.readline()
    else:
        pixel[0] = (255,0,0)
        pixel.write()
        return "No data"
		
while True:
	    received_data = receive_data()
    if received_data:
        print("Received:", received_data.strip())  # Print the received data
    time.sleep(0.1)  # Add a small delay to reduce CPU usage