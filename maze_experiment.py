import time
from maze_simulator import MazeSimulator

def main():
	sim = MazeSimulator(render=True, xml_file='hardmaze_env.xml')

	for t in range(1000):
		time.sleep(0.01)
		sim.render()
		observation, reward, done, info = sim.step([0.01, 1.0, 0], 0.2)
		if done:
			print("Episode finished after {} timesteps".format(t+1))
			break

if __name__ == "__main__":
    main()