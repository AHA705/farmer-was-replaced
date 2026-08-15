def is_even(n):
	return n % 2 == 0

def farm():
	if can_harvest():
		harvest()
	if is_even(get_pos_x() + get_pos_y()):
		plant(Entities.Tree)
		#use_item(Items.Fertilizer)
		#use_item(Items.Weird_Substance)
	else:
		plant(Entities.Grass)