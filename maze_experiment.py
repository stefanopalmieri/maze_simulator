import time
from maze_simulator import MazeSimulator

def main():
	sim = MazeSimulator(render=True, xml_file='hardmaze_env.xml')

	for t in range(1000):
		time.sleep(0.01)
		sim.render()
		print(sim.evaluate_fitness())
		observation, done, info = sim.step([0.01, 1.0, 0], 0.2)
		if done:
			print("Episode finished after {} timesteps".format(t+1))
			print(sim.evaluate_fitness())
			break

if __name__ == "__main__":
    main()