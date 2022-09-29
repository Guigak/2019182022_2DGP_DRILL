from asyncio import get_event_loop
from sre_parse import HEXDIGITS
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    # fill here

    global running
    global frame_x
    global frame_y
    global character_dir
    global character_running_x
    global character_running_y
    global dir_x
    global dir_y

    events = get_events()
    for event in events :
        if event.type == SDL_QUIT :
            running = False
        elif event.type == SDL_KEYDOWN :
            frame_x = 0

            if event.key == SDLK_RIGHT :
                character_running_x = True

                frame_y = 1
                character_dir = True
                dir_x += 1
            elif event.key == SDLK_LEFT :
                character_running_x = True

                frame_y = 0
                character_dir = False
                dir_x -= 1
            elif event.key == SDLK_UP :
                character_running_y = True

                if character_dir :
                    frame_y = 1
                else :
                    frame_y = 0

                dir_y += 1
            elif event.key == SDLK_DOWN :
                character_running_y = True

                if character_dir :
                    frame_y = 1
                else :
                    frame_y = 0

                dir_y -= 1
            elif event.key == SDLK_ESCAPE :
                running = False
        elif event.type == SDL_KEYUP :
            frame_x = 0

            if event.key == SDLK_RIGHT :
                character_running_x = False
                dir_x -= 1
            elif event.key == SDLK_LEFT :
                character_running_x = False
                dir_x += 1
            elif event.key == SDLK_UP :
                character_running_y = False
                dir_y -= 1
            elif event.key == SDLK_DOWN :
                character_running_y = False
                dir_y += 1                

            if character_running_x == False and character_running_y == False :
                if character_dir :
                    frame_y = 3
                else :
                    frame_y = 2

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame_x, frame_y = 0, 3
character_dir = True
character_running_x, character_running_y = False, False
dir_x, dir_y = 0, 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8

    if x + dir_x < 25 :
        x = 25
    elif x + dir_x > TUK_WIDTH - 25 :
        x = TUK_WIDTH - 25
    else :
        x += dir_x * 5

    if y + dir_y < 50 :
        y = 50
    elif y + dir_y > TUK_HEIGHT - 50 :
        y = TUK_HEIGHT - 50
    else :
        y += dir_y * 5

    delay(0.01)

close_canvas()

