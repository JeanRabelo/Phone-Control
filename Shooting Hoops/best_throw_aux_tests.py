import cv2
import numpy as np
from PIL import Image
import mss
from pprint import pprint

from ppadb.client import Client
# image = device.screencap()

# with open('screen2.png', 'wb') as f:
#     f.write(image)

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices)==0:
    print('no device attached')
    quit()

device = devices[0]

sct = mss.mss()
# color_purple_ball = [216, 176, 177]

lower = np.array([214, 173, 178, 255], dtype='uint8')
upper = np.array([214, 173, 178, 255], dtype='uint8')
scr = sct.grab({'left': 3115, 'top': 32, 'width': 490, 'height': 1008})
img = np.array(scr)
pprint(img)

while True:
    scr = sct.grab({'left': 3115, 'top': 32, 'width': 490, 'height': 1008})
    # scr = sct.grab({'left': 3343, 'top': 799, 'width': 15, 'height': 15})

    img = np.array(scr)
    # print('-----img-----')
    # print(img)
    # print('-----lower-----')
    # print(lower)
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow('output', img)
    cv2.imshow('output', np.hstack([img, output]))
    # cv2.imshow('output', mask)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break

# color_tank = {'r':209, 'g':220, 'b':89}
# color_purple_ball = {'r':177, 'g':176, 'b':216}
