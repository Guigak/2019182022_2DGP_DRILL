from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

dir = 0
x = 0
y = 0

ox = 400
oy = 300
rad = 0

while 1:
    clear_canvas_now()
    grass.draw_now(400, 30)
    
    if dir == 0:
        if x < 699:
            character.draw_now(x + 50 , y + 90)
            x = x + 2
        else:
            character.draw_now(x + 50, y + 90)
            y = y + 2
            dir = 1
    elif dir == 1:
        if y < 459:
            character.draw_now(x + 50, y + 90)
            y = y + 2
        else:
            character.draw_now(x + 50, y + 90)
            x = x - 2
            dir = 2
    elif dir == 2:
        if x > 1:
            character.draw_now(x + 50, y + 90)
            x = x - 2
        else:
            character.draw_now(x + 50, y + 90)
            y = y - 2
            dir = 3
    else:
        if y > 1:
            character.draw_now(x + 50, y + 90)
            y = y - 2
        else:
            character.draw_now(x + 50, y + 90)
            x = x + 2
            dir = 0

    
    character.draw_now(ox + 200 * math.cos(rad / 360 * 2 * math.pi), oy + 200 * math.sin(rad / 360 * 2 * math.pi))

    if rad != 358:
        rad = rad + 2
    else:
        rad = 0
        
    
    delay(0.01)

close_canvas()
