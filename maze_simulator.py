import distance
import environment as env
import renderer
import robot
import wall

from fitness_function_factory import FitnessFunctionFactory

class MazeSimulator():

    def __init__(self, render, xml_file):

        if render:
            self.renderer = renderer.Renderer(600, 500, 'Maze Simulator')

        self.env = env.Environment(xml_file)
        self.pois_reached = [False] * len(self.env.pois)
        self.reached_goal = False

    def reset(self):
        self.env.reset()
        self.pois_reached = [False] * len(self.env.pois)
        self.reached_goal = False

    def step_robot(self, outputs, time_step):
        """
        Step the robot in time where "outputs" is the action vector.
        """
        self.env.robot.decide_action(outputs, time_step)
        self.env.robot.update_position()
        # Check for collision
        did_collide = self.check_collisions()
        if did_collide:
            print(did_collide)
            self.env.robot.undo()

    def step(self, action, time_delta):
        observation = 0
        done = 0
        info = 0

        self.step_robot(action, time_delta)
        done = self.update_pois()

        return observation, done, info

    def collide(self, wall, robot):
        a1x = wall.ax
        a1y = wall.ay
        a2x = wall.bx
        a2y = wall.by
        bx = robot.location[0]
        by = robot.location[1]

        rad = robot.default_robot_size
        r = ((bx - a1x) * (a2x - a1x) + (by - a1y) * (a2y - a1y)) / wall.length_sq();
        px = a1x + r * (a2x - a1x);
        py = a1y + r * (a2y - a1y);
        np = (px, py);
        rad_sq = rad * rad;

        if (r >= 0.0 and r <= 1.0):
            if (distance.distance(bx, by, px, py) ** 2 < rad_sq):
                return True
            else:
                return False

        d1 = distance.distance(bx, by, a1x, a1y) ** 2
        d2 = distance.distance(bx, by, a2x, a2y) ** 2
        if (d1 < rad_sq or d2 < rad_sq):
            return True
        else:
            return False

    def check_collisions(self):
        for wall in self.env.walls:
            if self.collide(wall, self.env.robot):
                return True
        
    def update_pois(self):
        """
        Update the reached pois and if the robot has reached the goal.
        Return whether or not the robot has reached the goal.
        """
        if distance.robot_distance_from_goal(self.env) < 35.0:
            self.reached_goal = True
            return True
        else:
            for i in range(0, len(self.env.pois)):
                if distance.robot_distance_from_poi(self.env, i) < 20.0:
                    self.pois_reached[i] = True
            return False

    def render(self):
        self.renderer.render(self.env)

    def evaluate_fitness(self):
        factory = FitnessFunctionFactory()
        fitness_function = factory.get_fitness_function('hardmaze')
        return fitness_function(self.pois_reached, self.env, self.reached_goal)

    def quit(self):
        pygame.quit()