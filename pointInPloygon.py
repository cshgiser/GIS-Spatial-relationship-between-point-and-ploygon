import math


def getMBR(ploygon):
    """
    get the Minimum Bounding Rectangle of the given ploygon
    :param ploygon: the given polygon
    :return: the given ploygon's MBR
    """
    left_bottom_x = float('inf')
    left_bottom_y = float('inf')
    right_up_x = float('-inf')
    right_up_y = float('-inf')
    for plg in ploygon:
        for i in range(len(plg)):
            xx = plg[i][0]
            yy = plg[i][0]
            if xx < left_bottom_x:
                left_bottom_x = xx
            if xx > right_up_x:
                right_up_x = xx
            if yy < left_bottom_y:
                left_bottom_y = yy
            if yy > right_up_y:
                right_up_y = yy
    return (left_bottom_x, left_bottom_y), (right_up_x, right_up_y)


def distance(pointA, pointB):
    """
    the distance between point A and B
    :param pointA: point A
    :param pointB: point B
    :return: distance
    """
    return ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** 0.5


def isOnEdge(startPoint, endPoint, point):
    """
    whether the given point is on the line
    :param startPoint: the start point of the line
    :param endPoint: the end point of the line
    :param point: the given point
    :return: if point is on line, return True, else, return False
    """
    if distance(startPoint, point) + distance(endPoint, point) == distance(startPoint, endPoint):
        return True
    else:
        return False


def crossPoint(lineA, lineB):
    """
    the intersection point of two line. Note that if the intersection point is the start of line B,
    then return the start of line B, but if the intersection point is the end of line B, it will be regarded as
    there is no intersection point, avoiding repeated calculation.
    :param lineA: vertical line
    :param lineB: line in ploygon
    :return: intersection point, -1 if no intersection point
    """
    x1, y1, x2, y2 = lineA[0][0], lineA[0][1], lineA[1][0], lineA[1][1]  # here, x1 should be equal to x2
    x3, y3, x4, y4 = lineB[0][0], lineB[0][1], lineB[1][0], lineB[1][1]

    if y1 < min([y3, y4]):  # it means the point is under the whole line. it is no possible for them to intersect.
        return -1

    if x3 == x4:  # line B (from ploygon) is vertical
        if x3 == x1:  # # two lines are overlap
            if y1 > y3:
                return x3, y3
                # if the y coordinate of point is greater than that of the start point of B.
                # the intersection point is definitely the start point of line B.
        else:
            return -1

    # line B: y = kx + b
    k = (y4 - y3) / (x4 - x3)
    b = y3 - k * x3

    # interaction point
    crossP_x = x1
    crossP_y = k * x1 + b

    if min([x3, x4]) < crossP_x < max([x3, x4]) and min([y3, y4]) < crossP_y < max([y3, y4]) and crossP_y < y1:
        return crossP_x, crossP_y
        # in this case, the cross point is on line B but not is the start point of line B

    return -1



def method1(ploygon, point):
    ploygon_MBR = getMBR(ploygon)
    if point[0] < ploygon_MBR[0][0] or point[0] > ploygon_MBR[1][0] or point[1] < ploygon_MBR[0][1]\
            or point[1] > ploygon_MBR[1][1]:
        # not in MBR, let alone in ploygon
        return 'point is not in the ploygon'

    for plg in ploygon:
        for i in range(len(plg) - 1):
            if isOnEdge(plg[i], plg[i + 1], point):
                return 'point is on edge of the ploygon'
    # vertical line
    verticalLine_startP = point
    verticalLine_endP = (point[0], ploygon_MBR[0][1] - 1)

    # the number of the intersection point
    crossPoint_num = 0
    for plg in ploygon:
        for i in range(len(plg) - 1):
            cross_point = crossPoint((verticalLine_startP, verticalLine_endP), (plg[i], plg[i+1]))
            if cross_point != -1:
                crossPoint_num += 1

    if crossPoint_num % 2 == 1:  # if the crossPoint_num is odd
        return 'point is in the ploygon'
    else:  # if the crossPoint_num is even
        return 'point is not in the ploygon'


def vector(startP, endP):
    return endP[0] - startP[0], endP[1] - startP[1]


def distance_vec(vector):
    return (vector[0]**2 + vector[1]**2)**0.5

def vecDot(vecA, vecB):
    """
    the dot product of vecA and vecB
    :param vecA:
    :param vecB:
    :return:
    """
    x1, y1 = vecA[0], vecA[1]
    x2, y2 = vecB[0], vecB[1]
    return x1 * x2 + y1 * y2

def vecX(vecA, vecB):
    """
    the cross product of vecA and vecB
    :param vecA:
    :param vecB:
    :return:
    """
    x1, y1 = vecA[0], vecA[1]
    x2, y2 = vecB[0], vecB[1]
    return x1 * y2 - y1 * x2

def method2(ploygon, point):
    ploygon_MBR = getMBR(ploygon)
    if point[0] < ploygon_MBR[0][0] or point[0] > ploygon_MBR[1][0] or point[1] < ploygon_MBR[0][1] \
            or point[1] > ploygon_MBR[1][1]:
        # not in MBR, let alone in ploygon
        return 'point is not in the ploygon'

    for plg in ploygon:
        for i in range(len(plg) - 1):
            if isOnEdge(plg[i], plg[i + 1], point):
                return 'point is on edge of the ploygon'

    sum_angle = 0
    for plg in ploygon:
        for i in range(len(plg) - 1):
            vec1 = vector(point, plg[i])
            vec2 = vector(point, plg[i+1])
            ang = math.acos(vecDot(vec1, vec2) / (distance_vec(vec1) * distance_vec(vec2)))
            if vecX(vec1, vec2) < 0:
                ang = -ang
            sum_angle += ang

    if int(sum_angle / (2 * math.pi)) % 2 == 1:  # if sum_angle is equal to 2pi, or 3*2pi, or 5*2pi, ....
        return 'point is in the ploygon'
    else:  # if sum_angle is equal to 0, or 2*2pi, or 4*2pi, ....
        return 'point is not in the ploygon'



if __name__=='__main__':
    """"""
    # point = (2, 5)
    # point = (1.5, 9.9)
    point = (2, 3.5)
    ploygonn = [[(1, 1), (2, 3), (2, 4), (1, 6), (3, 10), (11, 8), (11, 3), (7, 0.5), (1, 1)]]
    print(method1(ploygonn, point))
    print(method2(ploygonn, point))

