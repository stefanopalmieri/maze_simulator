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

    def step(self, action, time_delta):
        observation = 0
        done = 0
        info = 0

        self.step_robot(action, time_delta)
        self.update_pois()

        return observation, done, info

    def update_pois(self):
        """
        Update the reached pois and if the robot has reached the goal.
        """
        if distance.robot_distance_from_goal(self.env) < 35.0:
            self.reached_goal = True
        else:
            for i in range(0, len(self.env.pois)):
                if distance.robot_distance_from_poi(self.env, i) < 20.0:
                    self.pois_reached[i] = True
                    print("reached a new poi")

    def render(self):
        self.renderer.render(self.env)

    def evaluate_fitness(self):
        factory = FitnessFunctionFactory()
        fitness_function = factory.get_fitness_function('hardmaze')
        return fitness_function(self.pois_reached, self.env, self.reached_goal)

    def quit(self):
        pygame.quit()