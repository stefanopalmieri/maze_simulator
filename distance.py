import math

def distance(x1, y1, x2, y2):
	return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def robot_distance_from_poi(env, i):
	"""
	Return the distance between the robot and 
	the ith point of interest.
	"""
	robot_x = env.robot.location[0]
	robot_y = env.robot.location[1]
	poi_x = env.pois[i].x
	poi_y = env.pois[i].y
	return distance(robot_x, robot_y, poi_x, poi_y)

def robot_distance_from_goal(env):
	"""
	Return the distance between the robot and 
	the ith point of interest.
	"""
	robot_x = env.robot.location[0]
	robot_y = env.robot.location[1]
	goal_x = env.goal.x
	goal_y = env.goal.y
	return distance(robot_x, robot_y, goal_x, goal_y)