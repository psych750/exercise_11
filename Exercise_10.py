import time
import random
import sys
import os
from math import sin, cos, pi
from psychopy import visual, core, event

win = visual.Window([300,300], color = 'black', units = 'pix', allowGUI = True)
my_mouse = event.Mouse(win=win)
num_circles = 4

class MovingCircle():
    def __init__(self,win):
        self.min_angle = -30
        self.max_angle = 30
        self.prev_angle_to_deviate = 0
        self.angle_moving_degrees = 0.0
        self.inter_step_interval = 2.0
        self.target = visual.Circle(win, size = 20, lineColor = 'black', fillColor = [1,1,1])

    def get_pos(self):
        return self.target.pos
    
    def target(self):
        return self.target

    def move_it(self):
        "gets new position and set target to that position"
        cur_angle_to_deviate = self.prev_angle_to_deviate + random.randint(self.min_angle,self.max_angle) # calcualte new angle
        cur_angle = cur_angle_to_deviate * pi / 180.0 # covnert to radians

        new_x_pos = self.inter_step_interval * cos(cur_angle)
        new_y_pos = self.inter_step_interval * sin(cur_angle)

        self.target.setPos((new_x_pos,new_y_pos),'+')
        hit_boundary = False
        if (abs(self.target.pos[0]) > 150 or abs(self.target.pos[1]) > 150):
            hit_boundary = True
            new_x_pos = self.inter_step_interval * cos(cur_angle - pi)
            new_y_pos = self.inter_step_interval * sin(cur_angle - pi)

        self.prev_angle_to_deviate = cur_angle_to_deviate
        if hit_boundary:
            self.prev_angle_to_deviate -= 180
            self.prev_angle_to_deviate %= 360

    def turn_it_red():
        "turns the circle red when you click on it without any pauses"

circles = [MovingCircle(win) for _ in range(num_circles)]
while True:
    for cur_circle in circles:
        cur_circle.target.draw()
        cur_circle.move_it()
    
    core.wait(.05)
    win.flip()

    if event.getKeys(['space']):
        sys.exit()