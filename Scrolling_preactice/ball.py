import random
from pico2d import *
import game_world

import server

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(10, server.background.w - 1 - 10)
        self.y = random.randint(10, server.background.h - 1 - 10)

    def draw(self):
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        self.image.draw(sx, sy)

    def update(self):
        pass

    def get_bb(self) :
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group) :
        if group == 'boy:ball' :
            game_world.remove_object(self)