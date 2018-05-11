import distance

def hardmaze_fitness_function(reached_pois, env, reached_goal):
	fitness = 0.0

	if (reached_goal):
		return 10.0
	for i in range(0, len(reached_pois)):
		# Add 1.0 if the current poi has been reached
		if reached_pois[i]:
			fitness += 1.0
		else:
			discount = distance.robot_distance_from_poi(env, i) / 650.0
			fitness += 1.0 - discount
			break

	return fitness

class FitnessFunctionFactory():

	def __init__(self):
		pass

	def get_fitness_function(self, name):
		if (name == 'hardmaze'):
			return self.get_hardmaze_fitness_function()

	def get_hardmaze_fitness_function(self):
		return hardmaze_fitness_function