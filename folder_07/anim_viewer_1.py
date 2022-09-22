from pico2d import *
open_canvas()

grass = load_image('grass.png')
ice = load_image('icepillar.png')

frame = 0

wide = 206
height = 384

while 1:
    for h in range(0, 5):
        if h != 4:
            for w in range(0, 6):
                clear_canvas()
                grass.draw(400, 30)
                ice.clip_draw(w * wide, (4 - h) * height, wide, height, 400, 225)
                update_canvas()
                delay(0.1)
                get_events()
        else:
            for w in range(0, 5):
                clear_canvas()
                grass.draw(400, 30)
                ice.clip_draw(w * wide, (4 - h) * height, wide, height, 400, 225)
                update_canvas()
                delay(0.1)
                get_events()

close_canvas()

