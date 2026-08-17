import utils
def farm():
	if get_entity_type() != None:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				harvest()
	def pumpkins_ready():
#	ready_state = True
#		n = measure()
		for i in range(get_world_size()):
			# Dont need to measure with fert
			#if measure() != None and measure() == measure(South):
			#	entire_farmland.move_to_start()
			#	break
			for j in range(get_world_size()):
				# quick_print(get_entity_type())
				while get_entity_type() != Entities.Pumpkin:
					if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
						use_item(Items.Fertilizer)
					elif get_entity_type() != Entities.Pumpkin:
						harvest()
				move(North)
			move(East)
		return measure() == measure(South)
	while True:
		state = pumpkins_ready()
		if state == True:
			# quick_print("Measurement:", measure())
			harvest()
			break