from pico2d import close_canvas, open_canvas

import frame_work
from Logo_mode import LogoMode


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


def main():
    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    try:
        frame_work.run(LogoMode())
    finally:
        close_canvas()


if __name__ == "__main__":
    main()
