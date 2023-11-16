import time
import random
import sys
import os
from math import sin, cos, pi
from psychopy import visual, core, event
from movingcircles import *

win = visual.Window([600,600], color = 'black', units = 'pix', allowGUI = True)
my_mouse = event.Mouse(win=win)
num_circles = 4

circles = [MovingCircle(win) for _ in range(num_circles)]
while True:
    for cur_circle in circles:
        cur_circle.target.draw()
        if my_mouse.isPressedIn(cur_circle.target):
            print('clicked on a circle!')
            cur_circle.change_speed(.8)
            cur_circle.make_dimmer(.9)
        cur_circle.move_it()
    
    core.wait(.05)
    win.flip()

    if event.getKeys(['space']):
        sys.exit()