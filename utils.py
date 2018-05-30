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

def collide(wall, robot):
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
        if (distance(bx, by, px, py) ** 2 < rad_sq):
            return True
        else:
            return False

    d1 = distance(bx, by, a1x, a1y) ** 2
    d2 = distance(bx, by, a2x, a2y) ** 2
    if (d1 < rad_sq or d2 < rad_sq):
        return True
    else:
        return False

# calculate the point of intersection between two line segments
def intersection(A, B, C, D):
    
    rTop = (A[1]-C[1])*(D[0]-C[0])-(A[0]-C[0])*(D[1]-C[1]);
    rBot = (B[0]-A[0])*(D[1]-C[1])-(B[1]-A[1])*(D[0]-C[0]);
    
    sTop = (A[1]-C[1])*(B[0]-A[0])-(A[0]-C[0])*(B[1]-A[1]);
    sBot = (B[0]-A[0])*(D[1]-C[1])-(B[1]-A[1])*(D[0]-C[0]);
    
    if (rBot == 0 or sBot == 0):
        return None

    r = rTop/rBot
    s = sTop/sBot

    if( (r>0) and (r<1) and (s>0) and (s<1)):
        ptx = A[0] + r * (B[0]-A[0])
        pty = A[1] + r * (B[1] - A[1])

        return (ptx, pty)
    else:
        return None

def raycast(walls, finder, a1x, a1y, heading, radius):

    shortest_distance = finder.max_range
    length = radius + finder.max_range
    angle = heading + finder.angle
    a2x = a1x + (length) * math.cos(angle)
    a2y = a1y - (length) * math.sin(angle)

    for wall in walls:
        p1 = (a1x, a1y)
        p2 = (a2x, a2y)
        p3 = (wall.ax, wall.ay)
        p4 = (wall.bx, wall.by)
        point = intersection(p1, p2, p3, p4)

        if point is not None:
            curr_distance = distance(a1x, a1y, point[0], point[1])
            if curr_distance < shortest_distance:
                shortest_distance = curr_distance

    return shortest_distance

# Keep angle between -pi and pi
def normalize(angle):
    width = 2 * math.pi
    offset = angle
    return offset - ( math.floor(offset / width) * width )

def radar_detect(goal, x, y, start_angle, end_angle, r_range):

    start_angle = normalize(start_angle)
    end_angle = normalize(end_angle)

    if (distance(x, y, goal.x, goal.y) > r_range):
        return 0.0
    else:
        angle = normalize(math.atan2(-(goal.y-y),(goal.x-x)))
        if start_angle <= angle and angle < end_angle:
            return 1.0
    return 0