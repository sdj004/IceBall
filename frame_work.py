import time


FRAME_DELAY = 0.01
running = False
stack = []


def change_mode(mode):
    if stack:
        stack.pop().finish()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    if not stack:
        quit()
        return

    stack.pop().finish()
    if stack:
        stack[-1].resume()
    else:
        quit()


def quit():
    global running
    running = False

frame_time = 0.0

def run(start_mode):
    global running

    if running:
        raise RuntimeError("The game loop is already running")

    stack[:] = [start_mode]
    running = True
    try:
        start_mode.init()

        global frame_time
        frame_time = 0.0
        current_time = time.time()
        while running and stack:
            mode = stack[-1]
            mode.handle_events()
            if not running:
                break
            if not stack or stack[-1] is not mode:
                continue

            mode.update()
            if not running:
                break
            if not stack or stack[-1] is not mode:
                continue

            mode.render()
            frame_time = time.time() - current_time
            frame_rate = 1.0 / frame_time
            current_time += frame_time
            #print(f'Frame Time: {frame_time}, Frame Rate: {frame_rate}')
            time.sleep(FRAME_DELAY)
    finally:
        try:
            while stack:
                stack.pop().finish()
        finally:
            running = False
