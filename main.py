import ov2640
import gc
import time
import sys

Npics = 3

def main():
    try:
        print("initializing camera")
        ### FULL INITIALIZATON LINE FOR CUSTOM PIN AND BAUD RATE SETTINGS ###
        #cam = ov2640.ov2640(sclpin=15, sdapin=14, cspin=13, mosipin=11, misopin=12, idSPI=1, idI2C=1,
        #                    spiBaudRate=8000000, i2cBaudRate=100000, resolution=OV2640_320x240_JPEG)
        
        ### USING DEFAULTS, APART FROM RESOLUTION ###
        #cam = ov2640.ov2640(resolution=ov2640.OV2640_320x240_JPEG)
        cam = ov2640.ov2640(resolution=ov2640.OV2640_640x480_JPEG)
        #cam = ov2640.ov2640(resolution=ov2640.OV2640_1024x768_JPEG)
        print(gc.mem_free())
        for i in range(Npics):
            FNAME = 'image%02d.jpg' % i
            clen = cam.capture_to_file(FNAME, True) #the /True/ here is file overwrite boolean
            print("captured image is %d bytes" % clen)
            print("image is saved to %s" % FNAME)
            time.sleep(1)
        sys.exit(0)
    
    except KeyboardInterrupt:
        print("exiting...")
        sys.exit(0)


if __name__ == '__main__':
    main()
