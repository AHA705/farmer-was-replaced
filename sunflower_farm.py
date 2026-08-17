import utils

locations:list = []
for _ in range(9):
	locations.append([])

def harvest_loc(
	x:int,
	x_dir:Direction,
	y:int,
	y_dir:Direction
):
	for _ in range(x):
		move(x_dir)
	for _ in range(y):
		move(y_dir)

	if get_entity_type() == None:
		quick_print("Error: Empty Tile found: (", get_pos_x(),get_pos_y(), ")")
		return

	while can_harvest() == False:
		pass
	# quick_print(get_pos_x(),get_pos_y())
	# quick_print(measure())
	harvest()

def harvest_sunflowers(locations:list):
	drone_i = None
	drone_i_l = []
	for loc in locations:
		for d in drone_i_l:
			wait_for(d)
		drone_i_l = []
		for l in loc:
			x,y = l
			x, y -= get_pos_x(), get_pos_y()
	
			x_dir, y_dir = West, South	
			if x >= 0:
				x_dir = East
			if y >= 0:
				y_dir = North
			x, y = abs(x), abs(y)

			drone_i = spawn_drone(harvest_loc, x,x_dir,y,y_dir) # type: ignore
			if drone_i:
				drone_i_l.append(drone_i)
				continue
			harvest_loc(x,x_dir,y,y_dir)

def measure_sunflowers():
	loc:list = locations
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			loc[15-measure()].append((get_pos_x(), get_pos_y()))
			move(North)
		move(East)
	return loc

def plant_sunflowers():
	loc:list = locations
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			spawn_drone(plant_measure)
			move(North)
		move(East)
	return loc

if __name__ == "__main__":
	#clear()
	# utils.for_all(till)
	utils.move_to_start()
	utils.water()
	utils.for_all_args(plant, Entities.Sunflower)
	utils.move_to_start()
	loc = measure_sunflowers()
	harvest_sunflowers(loc)