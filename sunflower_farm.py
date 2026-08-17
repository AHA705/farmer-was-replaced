# Farms sunflowers for power

import utils

def sunflower_task():
	utils.till_for(Grounds.Soil)
	utils.water_tile()
	plant(Entities.Sunflower)
	# use_item(Items.Fertilizer)
	return (measure(), (get_pos_x(), get_pos_y()))


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
	drone_i_l = []
	# Loc is a list of lists sorted by measurement.
	# Each nested list is a tuple (x,y).
	for loc in locations:
		# Need to wait for each measurement to be fully harvested.
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

# For all drones, do f
def for_all(f):
	drones_l = []
	measurements = []
	def row():
		a = []
		for _ in range(get_world_size() - 1):
			a.append(f())
			move(East)
		a.append(f())
		return a

	for _ in range(get_world_size()):
		d = spawn_drone(row)
		if not d:
			measurements += row()
		else:
			drones_l.append(d)
		move(North)

	for d in drones_l:
		measurements += wait_for(d) # type: ignore
	return measurements

def sort_harvest(m: list[tuple[int,int,int]]):

	s_loc:list = []
	for _ in range(9):
		s_loc.append([])

	for i in m:
		s_loc[15-i[0]].append(i[1])
	return s_loc

if __name__ == "__main__":
	# clear()
	# utils.for_all(till)
	utils.move_to_start()
	measurements = for_all(sunflower_task)
	sorted_locs = sort_harvest(measurements)
	harvest_sunflowers(sorted_locs)