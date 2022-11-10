from psychopy import visual, core, event
import random
import time
from math import sin, cos, pi

class MovingCircle():
    def __init__(self,win):
        self.min_angle = -30
        self.max_angle = 30
        self.prev_angle_to_deviate = 0
        self.angle_moving_degrees = 0.0
        self.inter_step_interval = 2.0
        self.target = visual.Circle(win, size = 20, lineColor = 'black', fillColor = [1,1,1])

    def change_speed(self,delta_speed):
        self.inter_step_interval *= delta_speed

    def make_dimmer(self,percent):
        self.target.opacity *= percent

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
        if (abs(self.target.pos[0]) > 300 or abs(self.target.pos[1]) > 300):
            hit_boundary = True
            new_x_pos = self.inter_step_interval * cos(cur_angle - pi)
            new_y_pos = self.inter_step_interval * sin(cur_angle - pi)

        self.prev_angle_to_deviate = cur_angle_to_deviate
        if hit_boundary:
            self.prev_angle_to_deviate -= 180
            self.prev_angle_to_deviate %= 360
