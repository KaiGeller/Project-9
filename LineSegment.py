#Kai Geller
#GitHub Username: KaiGeller
#05/25/2033
#The point if this code is to find the distance between points, find the length of a line, and find if the line is parallel to another line

class Point:
    """This class classifies the point"""
    _x_coord = 0
    _y_coord = 0

    def __init__(self,x_coordinate,y_coordinate):
        """This function initializes point with x and y coordinate"""
        self._x_coord = x_coordinate
        self._y_coord = y_coordinate

    def get_x_coord(self):
        """This function gets the x coordinate"""
        return self._x_coord

    def get_y_coord(self):
        """This function gets the y coordinate"""
        return self._y_coord

    def distance_to(self,point):
        """This function finds the distance in between the points"""
        distance = (self._x_coord - point._x_coord)**2 + (self._y_coord - point._y_coord)**2
        return distance**.5

class LineSegment:
    """This class classifies the line segment"""
    _endpoint_1 = (0,0)
    _endpoint_2 = (0,0)

    def __init__(self,point1,point2):
        """This function sets the endpoints equal to the inputted points"""
        self._endpoint_1 = point1
        self._endpoint_2 = point2

    def get_endpoint_1(self):
        """This function gets the first endpoint"""
        return self._endpoint_1

    def get_endpoint_2(self):
        """This function gets the second endpoint"""
        return self._endpoint_2

    def length(self):
        """This function finds the lenght of the line"""
        return self._endpoint_1.distanceTo(self._endpoint_2)

    def slope(self):
        """This function finds the slope of the line"""
        dx = self._endpoint_1.get_x_coord()-self._endpoint_2.get_x_coord()
        dy = self._endpoint_1.get_y_coord()-self._endpoint_2.get_y_coord()
        return dy/dx

    def is_parallel_to(self,line_2):
        """This function tests if the two lines are parallel"""
        if abs(self.slope() - line_2.slope()) < 0.000001:
            return True
        return False

