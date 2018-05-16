import environment as env
import math
import pygame

WHITE = (255,255,255)
GREEN = (0, 255, 0)
# Width of line
LINE_WIDTH = 3
POINT_RAD = 5

class Renderer():
    def __init__(self, width, height, title):
        pygame.init()
        self.disp_width = width
        self.disp_height = height

        self.screen = pygame.display.set_mode((self.disp_width, self.disp_height))
        self.screen.fill(WHITE)
        pygame.display.set_caption('Maze Simulator')

    def render_walls(self, walls):
        for wall in walls:
            color = wall.color
            ax = wall.ax
            ay = wall.ay
            bx = wall.bx
            by = wall.by
            pygame.draw.line(self.screen, color, [ax, ay], [bx,by], LINE_WIDTH)

    def render_rangefinder(self, x, y, radius, heading, finder):
        length = finder.distance
        angle = heading + finder.angle
        bx = x + (length) * math.cos(angle)
        by = y - (length) * math.sin(angle)
        pygame.draw.line(self.screen, GREEN, [x, y], [bx,by], LINE_WIDTH)

    def render_radar(self, x, y, radius, heading, radar):

        length = radar.max_range
        start_angle = heading + radar.start_angle
        end_angle = heading + radar.end_angle
        while start_angle < end_angle:
            bx = x + (length) * math.cos(start_angle)
            by = y - (length) * math.sin(start_angle)
            start_angle += 0.01
            if (radar.detecting > 0):
                pygame.draw.line(self.screen, (200,50,0), [x, y], [bx,by], LINE_WIDTH)
            else:
                pygame.draw.line(self.screen, (200,200,200), [x, y], [bx,by], LINE_WIDTH)

    def render_robot(self, robot):
        x = int(robot.location[0])
        y = int(robot.location[1])
        radius = robot.default_robot_size
        for radar in robot.radars:
            self.render_radar(x, y, radius, robot.heading, radar)
        for finder in robot.rangefinders:
            self.render_rangefinder(x, y, radius, robot.heading, finder)
        pygame.draw.circle(self.screen, WHITE, [x, y], int(radius))
        pygame.draw.circle(self.screen, (0,0,0), [x, y], int(radius), LINE_WIDTH)

    def render_goal(self, goal):
        x = int(goal.x)
        y = int(goal.y)
        pygame.draw.circle(self.screen, (0,100,0), [x, y], POINT_RAD, LINE_WIDTH)

    def render_pois(self, pois):
        for poi in pois:
            x = int(poi.x)
            y = int(poi.y)
            pygame.draw.circle(self.screen, (0,0,100), [x, y], POINT_RAD, LINE_WIDTH)

    def render_aoi(self):
        x = 160
        y = 114
        pygame.draw.rect(self.screen, (255,0,0), [x, y, 263, 299], LINE_WIDTH)

    def render(self, env):
        self.screen.fill(WHITE)
        self.render_robot(env.robot)
        self.render_walls(env.walls)
        self.render_pois(env.pois)
        self.render_goal(env.goal)
        #self.render_aoi()
        pygame.display.update() 