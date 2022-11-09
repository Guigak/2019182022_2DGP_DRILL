from pico2d import *
import game_world
import game_framework

import random

#
PIXEL_PER_METER = 10.0 / 0.3    # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # km / hour - 마라토너의 평균 속도
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

#
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
            
        self.x = random.randint(50, 500)
        self.y = random.randint(100, 549)

        self.frame_x = random.randint(0, 4)
        self.frame_y = random.randint(0, 1)

        self.direct = 1

    def draw(self):
        if self.direct == 1 :
            self.image.clip_composite_draw(int(self.frame_x) * 918 // 5, (2 - int(self.frame_y)) * 506 // 3, 918 // 5, 506 // 3, 0, '', self.x, self.y, 100, 100)
        else :
            self.image.clip_composite_draw(int(self.frame_x) * 918 // 5, (2 - int(self.frame_y)) * 506 // 3, 918 // 5, 506 // 3, 0, 'h', self.x, self.y, 100, 100)

    def update(self):
        if self.direct == 1 :
            if self.x >= 1600 - 1 - 50:
                self.direct = -1
        else :
            if self.x <= 50 :
                self.direct = 1

        self.x += self.direct * RUN_SPEED_PPS * game_framework.frame_time            

        #
        if self.frame_y == 2 :
            if self.frame_x >= 3 :
                self.frame_x += 1
                self.frame_y = 0

            self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        else :
            if self.frame_x >= 4 :
                self.frame_y += 1

            self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5


        # if self.x < 25 or self.x > 1600 - 25:
        #     game_world.remove_object(self)
