# Common functions


def move_n_dir(n, dir):
    for i in range(n):
        move(dir)


def move_to_start():
    move_n_dir(get_pos_x(), West)
    move_n_dir(get_pos_y(), South)


# For all drones, do f with Args
def for_all_args(f, args):
    def row():
        for _ in range(get_world_size() - 1):
            f(args)
            move(East)
        f(args)

    for _ in range(get_world_size()):
        if not spawn_drone(row):
            row()
        move(North)


# For all drones, do f
def for_all(f):
    def row():
        for _ in range(get_world_size() - 1):
            f()
            move(East)
        f()

    for _ in range(get_world_size()):
        if not spawn_drone(row):
            row()
        move(North)


# Water tile while < 0.5 if water is below 0.25
def water_tile():
    # Prevent running if current is over 0.25
    if get_water() > 0.25:
        return
    while get_water() < 0.5 and num_items(Items.Water) != 0:
        use_item(Items.Water)


# Water farm
def water():
    if get_water() > 0.25:
        return
    for_all(water_tile)


def till_for(g: Ground):
    if get_ground_type() != g:
        till()
