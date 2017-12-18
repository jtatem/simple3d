import math
import pygame
import random
import sys


class Point(object):
    def __init__(self, x, y, z):
        self.value = (float(x), float(y), float(z))

    def __repr__(self):
        return '{0}'.format(self.value)

    def project_2d(self, fov, viewer_distance):
        win_width = screen.get_width()
        win_height = screen.get_height()
        factor = fov / (viewer_distance + self.value[2])
        x = self.value[0] * factor + win_width / 2
        y = self.value[1] * factor + win_height / 2
        return x, y

    def drawPoint(self):
        x, y = self.project_2d(90, 4)
        screen.fill((abs(x % 255), 0, 0), (x, y, 1, 1))
        print('Point {0} drawn'.format(self.value))

    def addVectorToPoint(self, vector):
        new_vector = add_vectors(self, vector)
        self.value = new_vector.value
        return self

    def subtractVectorFromPoint(self, vector):
        new_vector = subtract_vectors(self, vector)
        self.value = new_vector.value
        return self

    def subtractPointFromPoint(self, point):
        new_vector = subtract_vectors(self, point)
        return new_vector

    def setPointToPoint(self, point):
        self.value = point.value
        return None


class Vector(object):
    def __init__(self, x, y, z):
        self.value = (float(x), float(y), float(z))

    def __repr__(self):
        return '{0}'.format(self.value)

    def addVectorToVector(self, vector):
        new_vector = add_vectors(self, vector)
        self.value = new_vector.value
        return self

    def subtractVectorFromVector(self, vector):
        new_vector = subtract_vectors(self, vector)
        self.value = new_vector.value
        return self

    def rotate_xy(self, degrees):
        theta = math.radians(degrees)
        matrix = list()
        matrix.append([math.cos(theta), -1 * math.sin(theta), 0])
        matrix.append([math.sin(theta), math.cos(theta), 0])
        matrix.append([0, 0, 1])
        new_vector = linear_transform(self, matrix)
        self.value = new_vector.value
        return self

    def rotate_xz(self, degrees):
        theta = math.radians(degrees)
        matrix = list()
        matrix.append([math.cos(theta), 0, math.sin(theta)])
        matrix.append([0, 1, 0])
        matrix.append([-1 * math.sin(theta), 0, math.cos(theta)])
        new_vector = linear_transform(self, matrix)
        self.value = new_vector.value
        return self

    def rotate_yz(self, degrees):
        theta = math.radians(degrees)
        matrix = list()
        matrix.append([1, 0, 0])
        matrix.append([0, math.cos(theta), -1 * math.sin(theta)])
        matrix.append([0, math.sin(theta), math.cos(theta)])
        new_vector = linear_transform(self, matrix)
        self.value = new_vector.value
        return self

    def scale(self, scaling_tuple):
        matrix = list()
        matrix.append([scaling_tuple[0], 0, 0])
        matrix.append([0, scaling_tuple[1], 0])
        matrix.append([0, 0, scaling_tuple[2]])
        new_vector = linear_transform(self, matrix)
        self.value = new_vector.value
        return self


def add_vectors(vector1, vector2):
    result = []
    for i in range(0, 3):
        result.append(vector1.value[i] + vector2.value[i])
    return Vector(*result)


def subtract_vectors(vector1, vector2):
    result = []
    for i in range(0, 3):
        result.append(vector1.value[i] - vector2.value[i])
    return Vector(*result)


def linear_transform(vector, transform_matrix):
    x = transform_matrix[0][0] * vector.value[0] + transform_matrix[0][1] * vector.value[1] + transform_matrix[0][2] * vector.value[2]
    y = transform_matrix[1][0] * vector.value[0] + transform_matrix[1][1] * vector.value[1] + transform_matrix[1][2] * vector.value[2]
    z = transform_matrix[2][0] * vector.value[0] + transform_matrix[2][1] * vector.value[1] + transform_matrix[2][2] * vector.value[2]
    return Vector(x, y, z)


def draw_loop():
    clock = pygame.time.Clock()
    points = [Point(1, 0, 0),
              Point(-1, 0, 0),
              Point(1, 1, 0),
              Point(-1, 1, 0)
              ]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(50)
        screen.fill((0, 0, 0))

        for p in points:
            p.drawPoint()
            p.addVectorToPoint(Vector(0, 0, -0.01))

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('simple3d')

    draw_loop()


