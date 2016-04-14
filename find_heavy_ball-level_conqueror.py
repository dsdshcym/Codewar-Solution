def find_ball(scales):
    def find_ball_helper(balls):
        n = len(balls)
        if n == 1:
            return balls[0]
        left_pan = balls[:n / 2]
        right_pan = balls[n / 2:]
        w = scales.get_weight(left_pan, right_pan)

        if w < 0:
            return find_ball_helper(left_pan)

        if w > 0:
            return find_ball_helper(right_pan)
    return find_ball_helper(range(8))
