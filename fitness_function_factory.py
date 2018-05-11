class FitnessFunctionFactory():

	def __init__(self):
		pass

	def get_fitness_function(self, name):
		if (name == 'hardmaze'):
			return self.get_hardmaze_fitness_function()

	def get_hardmaze_fitness_function(self):
		def hardmaze_fitness_function(x):
			return x + 2
		return hardmaze_fitness_function