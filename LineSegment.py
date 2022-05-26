class Point:
    _x_coord = 0
    _y_coord = 0
    def __init__(self,x,y):
        self._x_coord = x
        self._y_coord = y
    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    def distance_to(self,p):
        distance = (self._x_coord - p._x_coord)**2 + (self._y_coord - p._y_coord)**2
        return distance**.5
class LineSegment:
    _endpoint_1 = (0,0)
    _endpoint_2 = (0,0)
    def __init__(self,p1,p2):
        self._endpoint_1 = p1
        self._endpoint_2 = p2
    def get_endpoint_1(self):
        return self._endpoint_2
    def get_endpoint_2(self):
        return self._endpoint_2
    def length(self):
       return self._endpoint_1.distanceTo(self._endpoint_2)
    def slope(self):
        dx = self._endpoint_1.get_x_coord()-self._endpoint_2.get_x_coord()
        dy = self._endpoint_1.get_y_coord()-self._endpoint_2.get_y_coord()
        return dy/dx
    def is_parallel_to(self,line_2):
        if abs(self.slope() - line_2.slope()) < 0.000001:
            return True
        return False

