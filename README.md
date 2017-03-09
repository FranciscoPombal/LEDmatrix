# LEDmatrix

A 10 * 20 Pixel LED Matrix

Run the server:
	`python3 server/driver.py`

Run the client:
	`python3 -m client`

The serial paths are hardcoded for now.
So remember to boot the orange pi with the arduino plugged in,
wait a minute and only then plug in the HES controller (it all Just Works™)

The server is expecting `NUM_BYTES` (600) bytes to be written to the UNIX socket at `SOCK_PATH` ('/tmp/ledmatrix') per frame. Each three bytes represent a LED, and each of those three bytes are the color in standard RGB order. The first LED is the upper right corner, going left, then down, like so:

For driver: 
```
[
[00 01 02 03 04 05 06 07 08 09],
[10 11 12 13 14 15 16 17 18 19]
...
]
```
For arduino:
```
[
[09 08 07 06 05 03 03 02 01 00],
[10 11 12 13 14 15 16 17 18 19]
...
]
```
