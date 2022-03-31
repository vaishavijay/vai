def make_candy(x, y, goal):
    if goal >= 5 * y :
        z = goal - 5 * y
    else :
        z = goal % 5

        if z <= x :
            return z