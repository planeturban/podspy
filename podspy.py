__author__ = 'ube'



from serial import Serial
from time import sleep


podSerial = Serial(port="/dev/tty.usbserial", baudrate=19200, timeout=.5)
dockSerial = Serial(port="/dev/tty.SLAB_USBtoUART", baudrate=19200, timeout=.5)





while podSerial.isOpen():
    dock = dockSerial.read()
    sleep(.1)
    dock += dockSerial.read(dockSerial.inWaiting())

    if ( len(dock)):
        for s in dock.split("ff55".decode('hex')):
            print "Dock -> Pod: FF55%s" % s.encode('hex')
            print "             %s" % s
        podSerial.write(dock)
        dock = ""

    pod = podSerial.read()
    sleep(.2)
    pod += podSerial.read(podSerial.inWaiting())

    if len(pod):
        for s in pod.split(chr(0xff) + chr(0x55)):
            print "Pod -> Dock: FF55%s" % s.encode('hex')
            print "             %s" % s

        dockSerial.write(pod)
        pod = ""

