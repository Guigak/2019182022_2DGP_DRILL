import pico2d
import play_state
import logo_state
state = logo_state # 모듈 이름을 변수로 취급

pico2d.open_canvas()

states = [logo_state, play_state]

for state in states :
    state.enter()

    # game main loop code
    while state.running:
        state.handle_events()

        # 게임 월드 객체를 업데이트 - 게임 로직
        state.update()

        # 게임 월드 렌더링
        state.draw()

        pico2d.delay(0.05)
    
    state.exit()

pico2d.close_canvas()
    