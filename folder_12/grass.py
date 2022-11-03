from pico2d import *

class Grass:
    def __init__(self, y):
        self.y = y
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, self.y)

    def update(self) :
        pass

