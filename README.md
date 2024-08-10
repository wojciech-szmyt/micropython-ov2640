
# MicroPython class for OV2640 Camera - working with Raspberry Pico / Pico W

I adapted the code written by namato (https://github.com/namato/micropython-ov2640) to make it work with Raspberry Pico / Pico W or potentially other RP2040 devices. I changed the frequency and baud rate and added the required ID field for the I2C initialization. I increased the sleep time in line 41 of the 'ov2640.py' file, which prevented the first picture coming out corrupted. The first picture always comes out not well exposed though, I have no idea how to fix this.

You may want to experiment a bit with the frequencies and timeouts, I believe this has the potential to be better optimized.

Namato wrote:

"""

This is a basic interface to the [ArduCAM OV2640](http://www.arducam.com/camera-modules/2mp-ov2640/) under MicroPython for the ESP8266.  I wrote this because I could not find any good camera interfaces with MicroPython on the ESP8266.

Using this class you can:
* Initiate still pictures up to 1600x1200 resolution
* Read them from the camera
* Save them to flash on the ESP8266

After saving the image you can use other modules to post it to a REST API,
or save a (short) history of pictures on the flash for later retrieval.

"""

## Usage - Hardware Setup

This particular camera has both an i2c and spi interface for setup and
getting data on/off the camera.  A good way to wire up the camera to
the Pico / Pico W is as follows (note Vcc and GND pins are omitted here):

 Camera Pin | Pico (W) Pin  |
| --------- | ------------- |
| CS        | GPIO13        |
| MOSI      | GPIO11        |
| MISO      | GPIO12        |
| SCK       | GPIO10        |
| SDA       | GPIO14        |
| SCL       | GPIO15        |

This configuration is for I2C and SPI both with ID=1. If you want to change pins so the camera connects to SPI or I2C with ID=0 (see: Pico / Pico W pinout), you must change the IDs in the camera initialization line.

## Usage - Software

Just upload the files into your microcontroller via Thonny and you're good to go.

## Credits

The original driver source from Arducam was instrumental in the creation of this pure
MicroPython version.

The overall project was inspired by
[esparducam](https://johan.kanflo.com/building-the-esparducam/), but
getting this to work doesn't require any SMD soldering. :)

