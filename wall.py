import distance

class Wall():
	def __init__(self, ax, ay, bx, by, color=(0,0,0)):
		self.ax = ax
		self.ay = ay
		self.bx = bx
		self.by = by
		self.color = color

	def length_sq(self):
		d = distance.distance(self.ax, self.ay, self.bx, self.by)
		return d ** 2