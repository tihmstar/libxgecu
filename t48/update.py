#!/usr/bin/env python3

from xgecu import t48
import time
import usb1

def replay(t):
    dev = t.dev
    validate_read = t48.validate_read
    
    def bulkRead(endpoint, length, timeout=None):
        return dev.bulkRead(endpoint, length, timeout=(1000 if timeout is None else timeout))

    def bulkWrite(endpoint, data, timeout=None):
        dev.bulkWrite(endpoint, data, timeout=(1000 if timeout is None else timeout))
    
    def controlRead(bRequestType, bRequest, wValue, wIndex, wLength,
                    timeout=None):
        return dev.controlRead(bRequestType, bRequest, wValue, wIndex, wLength,
                    timeout=(1000 if timeout is None else timeout))

    def controlWrite(bRequestType, bRequest, wValue, wIndex, data,
                     timeout=None):
        dev.controlWrite(bRequestType, bRequest, wValue, wIndex, data,
                     timeout=(1000 if timeout is None else timeout))

    def interruptRead(endpoint, size, timeout=None):
        return dev.interruptRead(endpoint, size,
                    timeout=(1000 if timeout is None else timeout))

    def interruptWrite(endpoint, data, timeout=None):
        dev.interruptWrite(endpoint, data, timeout=(1000 if timeout is None else timeout))

    # Generated by usbrply
    # Source: Linux pcap (usbmon)
    # cmd: /usr/local/bin/usbrply --wrapper --device 56 2022-12-21_01_init_reflash.pcapng

    """
    # Generated from packet 89/90
    buff = controlRead(0xC0, 0xEE, 0x0000, 0x0004, 16)
    validate_read(b"\x28\x00\x00\x00\x00\x01\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00", buff, "packet 89/90")
    """
    t.winusb_16()

    """
    # Generated from packet 91/92
    buff = controlRead(0xC0, 0xEE, 0x0000, 0x0004, 40)
    validate_read(b"\x28\x00\x00\x00\x00\x01\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x01\x57\x49\x4E\x55\x53\x42\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00", buff, "packet 91/92")
    """
    t.winusb_40()


    """
    # Generated from packet 107/108
    bulkWrite(0x01, b"\x00\x00\x00\x00\x00\x00\x00\x00")
    # Generated from packet 109/110
    buff = bulkRead(0x81, 0x0200)
    validate_read(b"\x00\x01\x30\x00\x00\x01\x07\x00\x32\x30\x32\x32\x2D\x30\x39\x2D"
            b"\x32\x31\x30\x39\x3A\x32\x37\x00\x32\x39\x41\x30\x33\x36\x33\x32"
            b"\x57\x44\x4E\x35\x59\x46\x4F\x4D\x4B\x32\x52\x52\x56\x4A\x30\x41"
            b"\x32\x46\x39\x53\x39\x36\x31\x33\x1E\x06\x00\x00\x01\x00\x00", buff, "packet 109/110")
    """
    t.version_raw()

    """
    so starting from
    bulkWrite(0x01, b"\x3C\x00\x00\x00\x00\x00\x00\x00\x23\x01\x67\x45\xAB\x89\xEF\xCD")
    this is the bulk-write setup command (aka command 0x3c). It sets up the firmware for receiving a large blob from the host.
    the last 8 bytes are a magic value, and must be exactly those
    you then have a series of bulk-write commands which are used to send over the new firmware blob.

    0x3c is the 'enter programming mode' command
    0x3b is "transfer over control interface"
    """

    """
    maybe this is a flash erase
    """
    print("Sending update command...")
    # not the same as the pre-reset command (3D)
    # Generated from packet 111/112
    bulkWrite(0x01, b"\x3C\x00\x00\x00\x00\x00\x00\x00\x23\x01\x67\x45\xAB\x89\xEF\xCD")
    # Generated from packet 113/114
    # XXX: this needs a longer timeout. How long?
    buff = bulkRead(0x81, 0x0200, timeout=3000)
    validate_read(b"\x3C\x00\x30\x00\x00\x01\x07\x00", buff, "packet 113/114")

    print("Sending firmware...")
    # Generated from packet 115/116
    bulkWrite(0x01, b"\x3B\x01\x00\x00\x00\x00\x00\x00\x23\x01\x67\x45\xAB\x89\xEF\xCD")
    

    FIXME: insert firmware here
    


    # Generated from packet 3887/3888
    buff = bulkRead(0x81, 0x0200)
    validate_read(b"\x3B\x00\x30\x00\x00\x01\x07\x00", buff, "packet 3887/3888")
    # Generated from packet 3889/3890
    bulkWrite(0x01, b"\x3B\x02\x00\x01\x00\xFF\x03\x08\x23\x01\x67\x45\xAB\x89\xEF\xCD")

    """
    # Generated from packet 3891/3892
    bulkWrite(0x01, b"\x3F\x02\x00\x01\x00\xFF\x03\x08")
    
    note previous reset
    self.bulkWrite(0x01, b"\x3F\x00\x00\x00\x00\x00\x00\x00")
    """
    t.reset(mode=2)


def main():
    import argparse 

    parser = argparse.ArgumentParser(description="Reset programmer")
    args = parser.parse_args()

    t = t48.get()



    """
    ***********************************************************
    55-init
    ***********************************************************
    """
    print("55-init")
    """
    # Generated from packet 33/34
    buff = controlRead(0xC0, 0xEE, 0x0000, 0x0004, 16)
    validate_read(b"\x28\x00\x00\x00\x00\x01\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00", buff, "packet 33/34")
    """
    t.winusb_16()
    """
    # Generated from packet 35/36
    buff = controlRead(0xC0, 0xEE, 0x0000, 0x0004, 40)
    validate_read(b"\x28\x00\x00\x00\x00\x01\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x01\x57\x49\x4E\x55\x53\x42\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00", buff, "packet 35/36")
    """
    t.winusb_40()

    """
    # Generated from packet 51/52
    t.bulkWrite(0x01, b"\x00\x00\x00\x00\x00\x00\x00\x00")
    # Generated from packet 53/54
    buff = t.bulkRead(0x81, 0x0200)
    t48.validate_read(b"\x00\x01\x30\x00\x00\x01\x07\x00\x32\x30\x32\x32\x2D\x30\x39\x2D"
            b"\x32\x31\x30\x39\x3A\x32\x37\x00\x32\x39\x41\x30\x33\x36\x33\x32"
            b"\x57\x44\x4E\x35\x59\x46\x4F\x4D\x4B\x32\x52\x52\x56\x4A\x30\x41"
            b"\x32\x46\x39\x53\x39\x36\x31\x33\x1F\x06\x00\x00\x01\x00\x00", buff, "packet 53/54")
    """
    t.version_raw()


    # Generated from packet 55/56
    t.bulkWrite(0x01, b"\x3D\x00\x00\x00\x00\x00\x00\x00\x23\x01\x67\x45\xAB\x89\xEF\xCD")
    # Generated from packet 57/58
    buff = t.bulkRead(0x81, 0x0200)
    t48.validate_read(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", buff, "packet 57/58")

    """
    # Generated from packet 59/60
    t.bulkWrite(0x01, b"\x3F\x00\x00\x00\x00\x00\x00\x00")
    """
    print("Resetting...")
    t.reset(mode=0)

    print("Back...")



    """
    ***********************************************************
    56-update
    ***********************************************************
    """
    print("56-update")
    replay(t)


    """
    ***********************************************************
    57-reboot
    ***********************************************************
    """
    print("57-reboot")

    # Generated by usbrply
    # Source: Linux pcap (usbmon)
    # cmd: /usr/local/bin/usbrply --wrapper --device 57 2022-12-21_01_init_reflash.pcapng

    """
    # Generated from packet 3921/3922
    buff = controlRead(0xC0, 0xEE, 0x0000, 0x0004, 16)
    validate_read(b"\x28\x00\x00\x00\x00\x01\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00", buff, "packet 3921/3922")
    """
    t.winusb_16()

    """
    # Generated from packet 3923/3924
    buff = controlRead(0xC0, 0xEE, 0x0000, 0x0004, 40)
    validate_read(b"\x28\x00\x00\x00\x00\x01\x04\x00\x01\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x01\x57\x49\x4E\x55\x53\x42\x00\x00\x00\x00\x00\x00\x00\x00"
            b"\x00\x00\x00\x00\x00\x00\x00\x00", buff, "packet 3923/3924")
    """
    t.winusb_40()

    """
    # Generated from packet 3939/3940
    t.bulkWrite(0x01, b"\x00\x00\x30\x00\x00\x01\x07\x00")
    # Generated from packet 3941/3942
    buff = t.bulkRead(0x81, 0x0200)
    t48.validate_read(b"\x00\x01\x30\x00\x07\x01\x07\x00\x32\x30\x32\x32\x2D\x30\x39\x2D"
            b"\x32\x31\x30\x39\x3A\x32\x37\x00\x32\x39\x41\x30\x33\x36\x33\x32"
            b"\x57\x44\x4E\x35\x59\x46\x4F\x4D\x4B\x32\x52\x52\x56\x4A\x30\x41"
            b"\x32\x46\x39\x53\x39\x36\x31\x33\x1E\x06\x00\x00\x01\x00\x00", buff, "packet 3941/3942")
    """
    t.version_raw()
    
    print("update ok!")

if __name__ == "__main__":
    main()
