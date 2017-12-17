class Point(object):
    def __init__(self, x, y, z):
        self.value = (x, y, z)

    def __repr__(self):
        return '{0}'.format(self.value)

    def drawPoint(self):
        print('{0}'.format(self.value))

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


class Vector(object):
    def __init__(self, x, y, z):
        self.value = (x, y, z)

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


if __name__ == '__main__':
    p1 = Point(1, 2, 1)
    p2 = Point(0, 4, 4)
    v1 = Vector(2, 0, 0)

    p1.drawPoint()
    p2.drawPoint()

    v2 = p1.subtractPointFromPoint(p2)

    v1 = v1.addVectorToVector(v2)

    p1.addVectorToPoint(v1)
    p1.drawPoint()

    p2.subtractVectorFromPoint(v2)
    p2.drawPoint()
