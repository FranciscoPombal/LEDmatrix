BAUD = 115200  # Match arduino's baud rate

WIDTH = 10
HEIGHT = 20
NUM_LEDS = WIDTH * HEIGHT
NUM_BYTES = NUM_LEDS * 3

PORT = 53777

BLACK = (0, 0, 0)
WHITE = (0xff, 0xff, 0xff)
RED = (0xff, 0, 0)
GREEN = (0, 0xff, 0)
BLUE = (0, 0, 0xff)

# Tetris
NO_ROTATE = 0

# Snake
UP = 2
DOWN = 0
LEFT = 3
RIGHT = 1

# Minimum time to sleep in between frames to avoid dropped frames.
# Calculated by trial and error!
# TODO: ????? why is it bigger than the server's MIN_PERIOD
MIN_PERIOD = 63e-3
