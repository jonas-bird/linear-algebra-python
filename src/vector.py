class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def __add__(self, other-matrix):
        """
        define addition for Vector class
        """
        # This should provide duck-typing for adding vectors and vector like
        # matrices
        new-coordinates = []
        try:
            if self.dimension != other-matrix.dimension:
                raise ValueError('The order of the matrices must be equal')
        except TypeError('Both operands must have degree')

       return tuple(map(lambda i, j: i + j, self.coordinates, other-matrix.coordinates))
