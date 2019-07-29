class Point:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def distanceTo(self, otherPoint):
        dx = otherPoint.x - self.xpos
        dy = otherPoint.y - self.ypos
