import network
import webrepl
import time

ap_if = network.WLAN(network.AP_IF); ap_if.active(False)
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_ssid = 'DysonSphere'
sta_pass = 'Esp8266Fun'
sta_if.connect(sta_ssid, sta_pass)
time.sleep(10)

webrepl.start()

# BACK UP: CHIP WIFI
# ap_if = network.WLAN(network.AP_IF); ap_if.active(True)
# ap_ssid = 'Team 1 wifi'
# ap_pass = '!hpassword'
# ap_if.config(essid=ap_ssid, password=ap_pass)
# time.sleep(2)
# if ap_if.active():
#     print(f'Board network active')