from pico2d import *
open_canvas()
hide_lattice()

# function

def anime_func():
    for c in range(0, count):
        frame = 0
        
        for n in range(0, effects[c]['num']):
                clear_canvas()
                grass.draw(400, 30)
                
                if c == 15:
                    effect.clip_draw(280 + n * effects[c]['wide'], height_efct - effects[c]['y'] - effects[c]['height'], effects[c]['wide'], effects[c]['height'], 400, 300)
                else:
                    effect.clip_draw(n * effects[c]['wide'], height_efct - effects[c]['y'] - effects[c]['height'], effects[c]['wide'], effects[c]['height'], 400, 300)

                update_canvas()
                delay(0.2)
                get_events()

# data    

grass = load_image('grass.png')
effect = load_image('effect.png')

height_efct = effect.h

effects = {'y' : 0, 'height' : 60, 'wide' : 60, 'num' : 16},\
          {'y' : 140, 'height' : 60, 'wide' : 60, 'num' : 5},\
          {'y' : 220, 'height' : 110, 'wide' : 130, 'num' : 7},\
          {'y' : 330, 'height' : 110, 'wide' : 130, 'num' : 7},\
          {'y' : 470, 'height' : 70, 'wide' : 130, 'num' : 4},\
          {'y' : 540, 'height' : 100, 'wide' : 90, 'num' : 11},\
          {'y' : 640, 'height' : 100, 'wide' : 90, 'num' : 4},\
          {'y' : 740, 'height' : 130, 'wide' : 155, 'num' : 6},\
          {'y' : 870, 'height' : 130, 'wide' : 155, 'num' : 1},\
          {'y' : 1000, 'height' : 140, 'wide' : 130, 'num' : 5},\
          {'y' : 1140, 'height' : 50, 'wide' : 70, 'num' : 8},\
          {'y' : 1190, 'height' : 50, 'wide' : 100, 'num' : 6},\
          {'y' : 1240, 'height' : 40, 'wide' : 100, 'num' : 6},\
          {'y' : 1280, 'height' : 80, 'wide' : 125, 'num' : 4},\
          {'y' : 1370, 'height' : 30, 'wide' : 25, 'num' : 6},\
          {'y' : 1360, 'height' : 70, 'wide' : 50, 'num' : 4},\
          {'y' : 1430, 'height' : 50, 'wide' : 75, 'num' : 13},\
          {'y' : 1480, 'height' : 50, 'wide' : 75, 'num' : 3}

count = len(effects)

# main

while 1:
    anime_func()

close_canvas()

