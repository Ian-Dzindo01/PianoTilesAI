import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click
import time
import matplotlib.pyplot as plt

for i in list(range(4))[::-1]:
    print(i + 1)
    time.sleep(1)

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=[750, 260, 1150, 860]))
    print('Frame took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # for y in range(len(screen)):
    #     for x in range(len(screen[y])):
    #         if screen[y][x] < 10:
    #             click(x, y)
    plt.imshow(screen)
    plt.show()
    # cv2.imshow('window', screen)
    # print('Frame took {} seconds. Up to frame no {}'.format((time.time() - startTime), i))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
