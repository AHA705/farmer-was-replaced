import pumpkins_farm
import cactus_farm
import sunflower_farm
import trees_farm
import utils

def farm(crop):
	if crop == Entities.Grass:
		farm_hay()
	elif crop == Entities.Tree:
		farm_wood()
	elif crop == Entities.Carrot:
		farm_carrots()
	elif crop == Entities.Pumpkin:
		pumpkins_farm.farm()
	elif crop == Entities.Sunflower:
		utils.for_all_args(plant, Entities.Sunflower)
		utils.move_to_start()
		loc = sunflower_farm.measure_sunflowers()
		sunflower_farm.harvest_sunflowers(loc)
	elif crop == Entities.Cactus:
		farm_cactus()
	else:
		print("ERROR HELP ME MASTER")
		quick_print(crop)
		while True:
			do_a_flip()
	
def farm_generic(plant_type:Entity):
	utils.for_all_args(plant, plant_type)
	utils.for_all(farm_harvest)

def farm_harvest():
	while True:
		if can_harvest() or get_entity_type() == None:
			harvest()
			break

def farm_hay():
	farm_generic(Entities.Grass)

def farm_carrots():
	farm_generic(Entities.Carrot)

def farm_wood():
	utils.for_all(trees_farm.farm)

def farm_cactus():
	utils.for_all_args(plant, Entities.Cactus)
	cactus_farm.order_cacti()
	utils.for_all(farm_harvest)