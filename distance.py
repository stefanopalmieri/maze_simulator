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