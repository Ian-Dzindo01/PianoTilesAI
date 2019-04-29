import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import click, queryMousePosition
import time
import matplotlib.pyplot as plt

# link of the game to be used with: https://www.yiv.com/Piano-Tiles-2-Online

for i in list(range(3))[::-1]:
    print(i + 1)
    time.sleep(1)

score = 0
previousLane = -1
gameCoords = [710, 250, 1185, 790]                              # 250 to evade clicking the watermark ad


def begin(screen):
    global gameCoords, score, previousLane

    for y_ in range(5, len(screen) - 5, 5):                     # YOU WILL HAVE TO GO THROUGH THIS FUNCTION! len(screen) = 600. We are iterating each 5 pixels vertically.
        for i in range(4):
            if previousLane == i:                               # this makes sure that the clicked lane isnt checked again
                continue

            w = gameCoords[2] - gameCoords[0]
            x = int(i * w / 4 + w / 8)                               # get the coords of the pixels to look at
            y = int(len(screen) - y_)                                # y is going to keep decreasing as we go further down the loop

            if screen[y][x] < 70:
                actualX = x + gameCoords[0]                          # stores the positions to click at
                actualY = y + gameCoords[1]
                score += 1
                if score > 1000:                                     # taking care of the mouse lag when the speeds increase a lot.
                    actualY += 10
                if score > 1250:
                    actualY += 10
                if score > 1450:
                    actualY += 10
                if score > 1600:
                    actualY += 20
                if score > 1750:
                    actualY += 20
                if score > 1900:
                    actualY += 30
                if score > 2100:
                    actualY += 30                                   # the score could be improved by further calibrating the mouse speed at high scores

                click(actualX, actualY)
                previousLane = i
                return


click(1000, 710)                                 # clicks the start buttons, wherever they are, initalizing the game
click(1130, 710)
click(860, 710)
click(760, 710)

while True:
    mousePos = queryMousePosition()

    if gameCoords[2] > mousePos.x > gameCoords[0]:                            # make sure that the mouse is in the right position
        startTime = time.time()
        screen = np.array(ImageGrab.grab(bbox=gameCoords))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        begin(screen)
        print("Frame took {} seconds.".format((time.time() - startTime)))

        # plt.imshow(screen)
        # plt.show()

        # cv2.imshow('window', screen)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
    else:                                                    # the program is paused if the mouse is moved to the right of the captured screen area.
        if mousePos.x < 0:
            score = 0
            while True:
                mousePos = queryMousePosition()
                if gameCoords[2] < mousePos.x:                # if 1150 < mousePos.x, then break, because the mouse is not in the right position
                    break
