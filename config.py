import math

DEFAULT_XP = 200


# Level with corresponding xp
def get_level(xp):
    return (math.sqrt(625 + 100 * xp) - 25) / 50
