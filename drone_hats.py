# Simple file to iterate over unlocked hates (Excluding Special-effect hats)
def unlocked_hats():
	hats_set = []
	for hat in Hats:
		if hat == Hats.Dinosaur_Hat:
			continue
		if num_unlocked(hat):
			hats_set.append(hat)
	return hats_set

def wear_random_hat(hats_set):
	picked_hat = hats_set[random() * len(hats_set) // 1]
	print("Wearing: ", picked_hat)
	change_hat(picked_hat)
	do_a_flip()

if __name__ == "__main__":
	wear_random_hat(unlocked_hats())
