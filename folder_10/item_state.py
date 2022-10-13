from pico2d import *
import game_framework
import play_state
import title_state

image = None
running = True
logo_time = 0.0

# fill here

def enter():
    # fill here
    global image, logo_time

    image = load_image('add_delete_boy.png')

def exit():
    # fill here
    global image

    del image
    pass

def update():
    pass

def draw():
    # fill here
    #global image

    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN :
            match event.key :
                case pico2d.SDLK_ESCAPE :
                    game_framework.pop_state()
                case pico2d.SDLK_1 :
                    for boy in play_state.boys :
                        boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2 :
                    for boy in play_state.boys :
                        boy.item = 'BigBall'
                    game_framework.pop_state()
                

def test_self() :
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas

if __name__ == '__main__' :
    test_self()