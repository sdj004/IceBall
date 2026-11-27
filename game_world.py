from pico2d import draw_rectangle
import game_world
BACKGROUND = 0
OBJECT = 1
UI = 2
LAYER_COUNT = 3

world = [[] for _ in range(LAYER_COUNT)]
collision_pairs = {}
check_collision_box = False


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
            if game_world.check_collision_box and hasattr(obj, 'get_bb'):
                draw_rectangle(*obj.get_bb())


def clear():
    for layer in world:
        layer.clear()
    collision_pairs.clear()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        collision_pairs[group] = [[], []] # a와 b를 저장할 빈 리스트 생성
    if a : 
        if a not in collision_pairs[group][0]:
            collision_pairs[group][0].append(a)
    if b : 
        if b not in collision_pairs[group][1]:
            collision_pairs[group][1].append(b)


def remove_collision_pair(obj):
    for group, pairs in list(collision_pairs.items()):
        pairs[0][:] = [candidate for candidate in pairs[0] if candidate is not obj]
        pairs[1][:] = [candidate for candidate in pairs[1] if candidate is not obj]
        if not pairs[0] or not pairs[1]:
            del collision_pairs[group]


def _remove_inactive_collision_pairs():
    for pairs in list(collision_pairs.values()):
        for obj in pairs[0][:] + pairs[1][:]:
            if getattr(obj, "exist", True) is False:
                remove_collision_pair(obj)


def handle_collisions():
    _remove_inactive_collision_pairs()
    for group, pairs in list(collision_pairs.items()):
        for a in pairs[0][:]:
            for b in pairs[1][:]:
                if getattr(a, "exist", True) is False:
                    continue
                if getattr(b, "exist", True) is False:
                    continue
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
    _remove_inactive_collision_pairs()

