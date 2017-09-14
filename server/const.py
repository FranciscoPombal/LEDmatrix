# Arduino
BAUD = 115200  # Match arduino's baud rate
PATH = '/dev/ttyUSB0'

# LED matrix
WIDTH = 10
HEIGHT = 20
NUM_LEDS = WIDTH * HEIGHT
NUM_BYTES = NUM_LEDS * 3
CHALL = b"We're living in..."
REPLY = "The Matrix."
MIN_PERIOD = 35e-3  # Writing to the matrix with period > MIN_PERIOD results in corruption.
PORT = 53777

# Simulator
SCALE = 32  # Scaling factor so it doesn't actually take only 20x10 pixels on the screen
FPS = 30
VERTICAL = True  # False rotates left to horizontal. VISUAL ONLY, COORDINATES DON'T CHANGE!
