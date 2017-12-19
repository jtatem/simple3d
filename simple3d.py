import math
import pygame
import random
import sys


class Point(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return 'Point({0}, {1}, {2})'.format(self.x, self.y, self.z)

    def project_2d(self, fov, viewer_distance):
        win_width = screen.get_width()
        win_height = screen.get_height()
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = self.y * factor + win_height / 2
        return x, y

    def drawPoint(self):
        x, y = self.project_2d(90, 4)
        screen.fill((abs(x % 255), 255, 255), (x, y, 1, 1))
        print('Point ({0}, {1}, {2}) drawn'.format(self.x, self.y, self.z))

    def addVectorToPoint(self, vector):
        new_vector = add_vectors(self, vector)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def subtractVectorFromPoint(self, vector):
        new_vector = subtract_vectors(self, vector)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def subtractPointFromPoint(self, point):
        new_vector = subtract_vectors(self, point)
        return new_vector

    def setPointToPoint(self, point):
        self.x, self.y, self.z = point.x, point.y, point.z
        return None


class Vector(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return 'Vector({0}, {1}, {2})'.format(self.x, self.y, self.z)

    def addVectorToVector(self, vector):
        new_vector = add_vectors(self, vector)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def subtractVectorFromVector(self, vector):
        new_vector = subtract_vectors(self, vector)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def rotate_xy(self, degrees):
        theta = math.radians(degrees)
        matrix = list()
        matrix.append([math.cos(theta), -1 * math.sin(theta), 0])
        matrix.append([math.sin(theta), math.cos(theta), 0])
        matrix.append([0, 0, 1])
        new_vector = linear_transform(self, matrix)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def rotate_xz(self, degrees):
        theta = math.radians(degrees)
        matrix = list()
        matrix.append([math.cos(theta), 0, math.sin(theta)])
        matrix.append([0, 1, 0])
        matrix.append([-1 * math.sin(theta), 0, math.cos(theta)])
        new_vector = linear_transform(self, matrix)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def rotate_yz(self, degrees):
        theta = math.radians(degrees)
        matrix = list()
        matrix.append([1, 0, 0])
        matrix.append([0, math.cos(theta), -1 * math.sin(theta)])
        matrix.append([0, math.sin(theta), math.cos(theta)])
        new_vector = linear_transform(self, matrix)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self

    def scale(self, scale_x, scale_y, scale_z):
        matrix = list()
        matrix.append([scale_x, 0, 0])
        matrix.append([0, scale_y, 0])
        matrix.append([0, 0, scale_z[2]])
        new_vector = linear_transform(self, matrix)
        self.x, self.y, self.z = new_vector.x, new_vector.y, new_vector.z
        return self


def add_vectors(vector1, vector2):
    return Vector(*(vector1.x + vector2.x,
                    vector1.y + vector2.y,
                    vector1.z + vector2.z))


def subtract_vectors(vector1, vector2):
    return Vector(*(vector1.x - vector2.x,
                    vector1.y - vector2.y,
                    vector1.z - vector2.z))


def linear_transform(vector, transform_matrix):
    x = transform_matrix[0][0] * vector.x + transform_matrix[0][1] * vector.y + transform_matrix[0][2] * vector.z
    y = transform_matrix[1][0] * vector.x + transform_matrix[1][1] * vector.y + transform_matrix[1][2] * vector.z
    z = transform_matrix[2][0] * vector.x + transform_matrix[2][1] * vector.y + transform_matrix[2][2] * vector.z
    return Vector(x, y, z)


def draw_loop():
    clock = pygame.time.Clock()
    points = [Point(1, 0, 0),
              Point(-1, 0, 0),
              Point(1, 1, 0),
              Point(-1, 1, 0)
              ]
    while True:
        #return None
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


