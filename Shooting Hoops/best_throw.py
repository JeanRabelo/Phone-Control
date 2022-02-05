from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices)==0:
    print('no device attached')
    quit()

device = devices[0]
# device.shell('input touchscreen swipe 540 1600 540 2000 1')
device.shell('input tap 540 1108')
