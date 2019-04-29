import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time
import matplotlib.pyplot as plt

for i in list(range(3))[::-1]:
    print(i + 1)
    time.sleep(1)

score = 0
previousLane = -1
gameCoords = [710, 250, 1185, 790]


def begin(screen):
    global gameCoords, score, previousLane

    for y_ in range(5, len(screen) - 5, 5):                     # YOU WILL HAVE TO GO THROUGH THIS FUNCTION! len(screen) = 600. We are iterating each 5 pixels vertically.
        for i in range(4):
            if previousLane == i:
                continue

            w = gameCoords[2] - gameCoords[0]
            x = int(i * w / 4 + w / 8)                               # get the coords of the pixels to look at
            y = int(len(screen) - y_)                                # y is going to keep decreasing as we go further down the loop

            if screen[y][x] < 40:
                actualX = x + gameCoords[0]                          # maybe stores the positions to click at
                actualY = y + gameCoords[1]
                score += 1
                if score > 1000:                                     # this is probably taking care of the mouse lag when the speeds increase a lot.
                    actualY += 10
                if score > 1250:
                    actualY += 10
                if score > 1450:
                    actualY += 10
                if score > 1600:
                    actualY += 20

                for k in range(1700, 2500):                         # also taking care of the mouse lag
                    if score > k:
                        actualY += 10
                    else:
                        break

                click(actualX, actualY)
                previousLane = i
                return


while True:
    mousePos = queryMousePosition()

    if gameCoords[2] > mousePos.x > gameCoords[0]:
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=[710, 250, 1185, 790]))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # begin(screen)
        print("Frame took {} seconds.".format((time.time() - startTime)))

        plt.imshow(screen)
        plt.show()

        # cv2.imshow('window', screen)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
    else:
        if mousePos.x < 0:
            score = 0
            while True:
                mousePos = queryMousePosition()
                if gameCoords[2] < mousePos.x:                # if 1150 < mousePos.x.
                    break


# game1Coords = [750, 260, 1150, 860]
# game2Coords = [710, 185, 1185, 790]


# TASKS:
    # 1. Figure out whether the proper places on the board are being checked.
    # 2. Figure out whether the speeds are adjusted correctly.
