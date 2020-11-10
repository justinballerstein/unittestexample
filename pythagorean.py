import math

class Pythagorean:
    def theorem(self, a,b):
        if (a <= 0):
            return None
        if (b <= 0):
            return None
        return math.sqrt((int(a) * int(a)) + (int(b) * int(b)))