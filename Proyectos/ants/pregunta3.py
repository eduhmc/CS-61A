new_place = self.plac
while new_place is not hive:
	if new_place.bees:
	break
	else:
		new_place = new_place.entrance
if new_place is hive:
	return None
return random_or_none(new_place.bees)