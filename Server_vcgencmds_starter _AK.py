#ANKITKUMAR CHAUDHARY
#100887553
#TPRG 2
#THIS THE SERVER FILE WHERE I ADD 4 NEW ARGUMENT WHICH SHOW VOLTAGE, FREQUENCY, RAM VOLTAGE AND CONFIGRATION OF PI
#This server runs on Pi, sends Pi's your 4 arguments from the vcgencmds, sent as Json object.

# details of the Pi's vcgencmds - https://www.tomshardware.com/how-to/raspberry-pi-benchmark-vcgencmd
# more vcgens on Pi 4, https://forums.raspberrypi.com/viewtopic.php?t=245733
# more of these at https://www.nicm.dev/vcgencmd/

import socket
import os, time
import json

s = socket.socket()
host = '192.168.2.107' # I USED MY SYSTEM AT HOME SO THAT REASON MY HOST ID IS STARTED AR 192
port = 5000
s.bind((host, port))
s.listen(5)


#gets the Core Temperature from Pi, ref https://github.com/nicmcd/vcgencmd/blob/master/README.md
def temperature():  # FOR MEASURE  TEMPERATURE OF SYSTEM
    t = os.popen('vcgencmd measure_temp').readline() #gets from the os, using vcgencmd - the core-temperature
    return t.strip()
def voltage():  #FOR MEASURE CORE VOLTAGE
    v = os.popen('vcgencmd measure_volts core').readline()
    return v.strip() #USEING STRIP COMMAND FOR SIMPLIFY CODE AND ITS HELPS TO AVOID UNNESSECCARY CODING
def configuration(): #FOR SYSTEM CONFIGRATION
    confi = os.popen('vcgencmd get_config int').readline()
    return confi.strip()
def frequency():  #FOR MEASURE CLOCK FREQUENCY
    f = os.popen('vcgencmd measure_clock core').readline()
    return f.strip()
def voltage_sdram_p():  #FOR MEASURE GPU SPEED
    vsdram = os.popen('vcgencmd measure_volts sdram_p').readline()
    return vsdram.strip()


while True:
    try:
        c, addr = s.accept()
        print ('Got connection from',addr)
        t = temperature()
        v = voltage()
        confi = configuration()
        f = frequency()
        vsdram = voltage_sdram_p()
        data = {
            "temperature": t,
            "voltage": v,
            "configuration": confi,
            "frequency": f,
            "voltage_sdram_p": vsdram
        }
  
        res = json.dumps(data) #USING THIS FROM WEEK 10 
                          # needs to be a byte
        c.send(res.encode('utf-8')) # sends data as a byte type
        c.close()
    except KeyboardInterrupt:
        print("error")
  

