import pygame
import time
from maze_simulator import MazeSimulator

def main():
	sim = MazeSimulator(render=True, xml_file='hardmaze_env.xml')

	for t in range(30000):
		time.sleep(.01)
		sim.render()
		events = pygame.event.get()
		action = [0, 0.2, 0]
		for event in events:
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_LEFT:
		            action = [0.453, 0, 0]
		        if event.key == pygame.K_RIGHT:
		            action = [0, 0, 0.453]
		observation, done, info = sim.step(action, 0.2)
		if done:
			print("Episode finished after {} timesteps".format(t+1))
			print(sim.evaluate_fitness())
			break

if __name__ == "__main__":
    main()