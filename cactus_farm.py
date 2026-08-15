# Assumes start from (0,0)
# Assumes Tilled Ground

# Slow but works
# It will finish just takes a minute or two

import utils

utils.move_to_start()

directions = [North, East]
edge = get_world_size() - 1


def can_swap_in_pos(axis):
    # Check if it's on map edge and if it can swap cacti
    if axis == East:
        return get_pos_x() != edge
    else:
        return get_pos_y() != edge


def swaparoni():
    done_all = True
    while True:
        done = True
        for axis in directions:
            c = measure()
            n = measure(axis)
            if n != None and c > n and can_swap_in_pos(axis):
                swap(axis)
                done = False
                done_all = False
        if done == True:
            break
    return done_all


def order_cacti():
    done_all = False

    while done_all == False:
        done_all = True
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if swaparoni() == False:
                    done_all = False
                move(North)
            move(East)
        quick_print(done_all)
