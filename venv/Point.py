class Point:

    xpos, ypos = 0, 0

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def distanceTo(self, other_point):
        dx = other_point.x - self.xpos
        dy = other_point.y - self.ypos
