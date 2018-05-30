import pygame
import time
from maze_simulator import MazeSimulator

def main():
    sim = MazeSimulator(render=True, xml_file='ENV_dual_task.xml')

    for t in range(30000):
        time.sleep(0.005)
        sim.render()
        keys = pygame.key.get_pressed()
        action = [0, 0.4, 0]
        if keys[pygame.K_LEFT]:
            action = [0.05, 0, 0]
        if keys[pygame.K_RIGHT]:
            action = [0, 0, 0.05]

        finder_obs, radar_obs, done = sim.step(action, 0.2)

        pygame.event.pump()
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            print(sim.evaluate_fitness())
            break

if __name__ == "__main__":
    main()