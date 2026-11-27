BACKGROUND = 0
OBJECT = 1
UI = 2
LAYER_COUNT = 3

world = [[] for _ in range(LAYER_COUNT)]


def add_object(obj, depth=OBJECT):
    if (
        not isinstance(depth, int)
        or isinstance(depth, bool)
        or not 0 <= depth < LAYER_COUNT
    ):
        raise ValueError(f"depth must be an integer from 0 to {LAYER_COUNT - 1}")

    world[depth].append(obj)


def remove_object(obj):
    for layer in world:
        if obj in layer:
            layer.remove(obj)
            return


def update():
    for layer in world:
        for obj in layer[:]:
            obj.update()


def render():
    for layer in world:
        for obj in layer[:]:
            obj.draw()


def clear():
    for layer in world:
        layer.clear()
