# Maze solution. Goes through the maze and "follows" the wall until it finds the treasure
import drone_hats

axis = [North, East, South, West]


def setup_maze():
    plant(Entities.Bush)
    substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


# Task for each drone
def task(i, hat):
    quick_print(i, "Drone reporting in, wearing:", hat)
    change_hat(hat)
    find_treasure(i)


def find_treasure(i):
    # Using i so that every drone goes into a different direction at start
    i = i % 4
    while True:
        if get_entity_type() == Entities.Treasure:
            harvest()
            setup_maze()
        if can_move(axis[i]):
            move(axis[i])
            # Turn left
            i = (i - 1) % 4
        else:
            # Turn Right
            i = (i + 1) % 4


def main():
    clear()
    setup_maze()
    u_hats: list = drone_hats.unlocked_hats()
    max_d = max_drones() - 1
    for i in range(max_d):
        hat = u_hats[i % len(u_hats)]
        spawn_drone(task, i, hat) # pyright: ignore[reportArgumentType]
    task(max_d, u_hats.pop())


if __name__ == "__main__":
    main()
