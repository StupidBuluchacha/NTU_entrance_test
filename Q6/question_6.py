class Point:
    lng = ''
    lat = ''

    def __init__(self, lng, lat):
        self.lng = lng
        self.lat = lat


# Find the polygon
def get_polygon_bounds(points):
    length = len(points)
    top = down = left = right = points[0]
    for i in range(1, length):
        if points[i].lng > top.lng:
            top = points[i]
        elif points[i].lng < down.lng:
            down = points[i]
        else:
            pass
        if points[i].lat > right.lat:
            right = points[i]
        elif points[i].lat < left.lat:
            left = points[i]
        else:
            pass
    top_left = Point(top.lng, left.lat)
    top_right = Point(top.lng, right.lat)
    down_right = Point(down.lng, right.lat)
    down_left = Point(down.lng, left.lat)
    return [top_left, top_right, down_right, down_left]


# determine whether points in polygon
def is_point_in_rect(point, polygon_bounds):
    top_left = polygon_bounds[0]
    top_right = polygon_bounds[1]
    down_right = polygon_bounds[2]
    down_left = polygon_bounds[3]
    return (down_left.lng <= point.lng <= top_right.lng
            and top_left.lat <= point.lat <= down_right.lat)


def is_point_in_polygon(point, points):
    polygon_bounds = get_polygon_bounds(points)
    if not is_point_in_rect(point, polygon_bounds):
        return False
    length = len(points)
    point_start = points[0]
    flag = False
    for i in range(1, length):
        point_end = points[i]
        # point overlap with vertices of polygon
        if (point.lng == point_start.lng and point.lat == point_start.lat) or (
                point.lng == point_end.lng and point.lat == point_end.lat):
            return True
        # check whether vertices of line segment are on the two sides of half-line
        if (point_end.lat < point.lat <= point_start.lat) or (
                point_end.lat >= point.lat > point_start.lat):
            # X coordinate in line segment with same y coordinate of half line
            if point_end.lat == point_start.lat:
                x = (point_start.lng + point_end.lng) / 2
            else:
                x = point_end.lng - (point_end.lat - point.lat) * (
                        point_end.lng - point_start.lng) / (
                            point_end.lat - point_start.lat)
            # point is on the polygon bound
            if x == point.lng:
                return True
            # half-line is through the bound of polygon
            if x > point.lng:
                flag = not flag
            else:
                pass
        else:
            pass

        point_start = point_end
    return flag


if __name__ == '__main__':
    file = open('output question 6.txt', 'w')
    # read the data
    polyline = [Point(float(i.split()[0]), float(i.split()[1])) for i in open('input_question_6_polygon').read().split('\n') if i]
    points = [tuple([int(j) for j in i.split()]) for i in open('input_question_6_points').read().split('\n') if i]
    for point in points:
        res = 'Inside' if is_point_in_polygon(Point(point[0], point[1]), polyline) else 'Outside'
        file.write(' '.join([str(point[0]), str(point[1])]) + ' ' + res + '\n')
    file.close()