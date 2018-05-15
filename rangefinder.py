class RangeFinder():

    def __init__(self, angle, max_range):
        self.angle = angle
        self.max_range = max_range
        self.distance = -1

    def get_value(self):
        return self.distance / self.max_range;

    def get_value_raw(self):
        return self.distance

