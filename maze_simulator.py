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
        factory = FitnessFunctionFactory()
        fitness_function = factory.get_hardmaze_fitness_function()
        print(fitness_function(5))

    def reset(self):
        self.env.reset()

    def step_robot(self, outputs, time_step):
        """
        Step the robot in time where "outputs" is the action vector.
        """
        self.env.robot.decide_action(outputs, time_step)
        self.env.robot.update_position()

    def step(self, action, time_delta):
        observation = 0
        reward = 0
        done = 0
        info = 0

        self.step_robot(action, time_delta)

        return observation, reward, done, info

    def render(self):
        self.renderer.render(self.env)

    def quit(self):
        pygame.quit()