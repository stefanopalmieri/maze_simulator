import math
import random
import utils
from radar import Radar
from rangefinder import RangeFinder

class Robot():
    def __init__(self, location):
        self.name = "MazeRobotPieSlice"
        self.default_speed = 25.0
        self.default_turn_speed = 9.0
        self.actualRange = 40.0
        self.default_robot_size = 10.5 # radius of robot
        self.default_sensor_density = 5
        self.velocity = 0.0
        self.heading = math.pi/2
        self.location = location
        self.old_location = location
        self.time_step = 0.1
        self.heading_noise = 0.0
        self.rangefinders = []
        self.radars = []
        for i in range(0,5):
            between_angle = math.pi/4.0
            final_angle = math.pi/2-(between_angle*i)
            self.rangefinders.append(RangeFinder(final_angle, self.actualRange))
        for i in range(0,4):
            between_angle = math.pi/2.0
            start_angle = math.pi/4-(between_angle*i)
            self.radars.append(Radar(start_angle, start_angle + between_angle))

    def rand_bool(self):
        return bool(random.getrandbits(1))

    def undo(self):
        self.location = self.old_location

    # Also find out what value headingNoise shoud be, 200 is incorrect
    def noisy_heading(self):
        handedness = 1 if self.rand_bool() else -1
        noisy = self.heading + 0.1 * handedness * random.randint(0, self.heading_noise) / 100.0
        return noisy

    def decide_action(self, outputs, time_step):
        """
        Step the robot in time where "outputs" is the action vector.
        """
        speed = 20.0
        turnSpeed = 4.28

        self.velocity = speed * outputs[1]
        self.heading += (outputs[0] - outputs[2]) * turnSpeed * time_step

    def update_position(self):
        self.old_location = self.location

        # update current coordinates (may be revoked if new position forces collision)
        temp_heading = self.noisy_heading()
        self.heading = temp_heading;
        dx = math.cos(temp_heading) * self.velocity * self.time_step
        dy = math.sin(temp_heading) * self.velocity * self.time_step
        x = self.location[0] + dx
        y = self.location[1] - dy
        self.location = (x, y)

    def update_rangefinders(self, walls):
        for finder in self.rangefinders:
            length = self.default_robot_size
            angle = self.heading + finder.angle
            a1x = self.location[0]
            a1y = self.location[1]
            #a2x = self.location[0] + (length) * math.cos(angle)
            #a2y = self.location[1] - (length) * math.sin(angle)
            #finder.distance = utils.raycast(walls, finder, a2x, a2y, self.heading)
            finder.distance = utils.raycast(walls, finder, a1x, a1y, self.heading, self.default_robot_size)