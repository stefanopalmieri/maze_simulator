class Radar():

    def __init__(self, start_angle, end_angle):
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.max_range = 100.0
        self.detecting = 0

    def get_value(self):
        return self.detecting

