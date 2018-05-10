import bs4
import goal
import point_of_interest
import robot
import wall

class Environment():

    def __init__(self, xml_file):
        soup = self.file_to_soup(xml_file)
        self.populate_walls(soup)
        self.populate_pois(soup)
        self.init_robot(soup)
        self.init_goal(soup)
        self.group_orientation = soup.find('group_orientation')
        self.robot_spacing = soup.find('robot_spacing')
        self.heading = soup.find('robot_heading')
        self.seed = soup.find('seed')

    def init_robot(self, soup):
        start = soup.find('start_point')
        start_x = float(start.x.get_text())
        start_y = float(start.y.get_text())
        self.robot = robot.Robot((start_x, start_y))

    def init_goal(self, soup):
        goal_point = soup.find('goal_point')
        goal_x = float(goal_point.x.get_text())
        goal_y = float(goal_point.y.get_text())
        self.goal = goal.Goal(goal_x, goal_y)       

    def populate_walls(self, soup):
        self.walls = []

        for cur_wall in soup.find_all('Wall'):
            line = cur_wall.line
            ax = float(line.p1.x.get_text())
            ay = float(line.p1.y.get_text())
            bx = float(line.p2.x.get_text())
            by = float(line.p2.y.get_text())
            new_wall = wall.Wall(ax,ay,bx,by)
            self.walls.append(new_wall)

    def populate_pois(self, soup):
        self.pois = []

        for point in soup.find_all('Point'):
            x = float(point.X.get_text())
            y = float(point.Y.get_text())
            new_poi = point_of_interest.PointOfInterest(x, y)
            self.pois.append(new_poi)

    def file_to_soup(self, xml_file):
        """
        Return a Beautiful Soup object created
        from xml filename.
        """
        file = open(xml_file,'r')
        xml = file.read()
        return bs4.BeautifulSoup(xml, 'xml')

    def reset(self):
        self.robot = robot.Robot((400, 700))

