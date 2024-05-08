import network
import webrepl
import time
import machine

pin = machine.Pin(2, machine.Pin.OUT)
pin.off()
ap_if = network.WLAN(network.AP_IF); ap_if.active(False)
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_ssid = 'DysonSphere'
sta_pass = 'Esp8266Fun'
sta_if.connect(sta_ssid, sta_pass)
while not sta_if.isconnected():
    time.sleep(0.02)
pin.on()
webrepl.start()