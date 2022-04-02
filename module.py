from enum import Enum


class Container:
    def __init__(self, capacity):
        self.size = 0
        self.data = []
        self.capacity = capacity


def container_push_back(container, item):
    if container.size + 1 <= container.capacity:
        container.size += 1
        container.data.append(item)
    else:
        raise OverflowError


def container_clear(container):
    container.size = 0
    container.data = None
    container.capacity = None


def container_read_from(container, stream):
    while line := stream.readline():
        item = matrix_read_from(stream, line)
        container_push_back(container, item)


def container_write_to(container, stream):
    stream.write(f'Container contains {container.size} elements\n')

    if container.data != None:
        for item in container.data:
            matrix_write_to(item, stream)


def container_sort(container):
    for i in range(container.size - 1):
        for j in range(i + 1, container.size):
            if compare(container.data[i].obj, container.data[j].obj):
                container.data[i], container.data[j] = container.data[j], container.data[i]


def two_dimensional_array_read_from(matrix, stream, size):
    for i in range(size):
        line = stream.readline().rstrip('\n')
        matrix.data.append(list(map(lambda x: int(x), line.split())))


def two_dimensional_array_write_to(matrix, stream, size, out_type):
    if out_type == 1:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write(f'{matrix.data[i][j]} ')
            stream.write('\n\t\t')

    elif out_type == 2:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write(f'{matrix.data[j][i]} ')
            stream.write('\n\t\t')

    elif out_type == 3:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write(f'{matrix.data[i][j]} ')
        stream.write('\n\t\t')
    else:
        stream.write('\tError matrix output type\n')


def diagonal_read_from(matrix, stream):
    matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))


def diagonal_write_to(matrix, stream, size, out_type):
    if out_type == 1 or out_type == 2:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write('{} '.format(matrix.data[i] if i == j else 0))
            stream.write('\n\t\t')

    elif out_type == 3:
        stream.write('\t\t')
        for i in range(size):
            for j in range(size):
                stream.write('{} '.format(matrix.data[i] if i == j else 0))
        stream.write('\n\t\t')
    else:
        stream.write('\tError matrix output type\n')


def triangle_read_from(matrix, stream):
    matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))


def triangle_write_to(matrix, stream):
    stream.write(f'\t\t{matrix.data}\n')


class MatrixType(Enum):
    two_dimensional_array = 1
    diagonal = 2
    triangle = 3


class Matrix:
    def __init__(self):
        self.size = 0
        self.out_type = 0

        self.key = None
        self.obj = None


def matrix_read_from(stream, line):
    k = int(line)

    matrix = Matrix()
    matrix.size = int(stream.readline().rstrip('\n'))
    matrix.out_type = int(stream.readline().rstrip('\n'))

    if k == 1:
        matrix.key = MatrixType.two_dimensional_array
        matrix.obj = TwoDimArray()
        two_dimensional_array_read_from(matrix.obj, stream, matrix.size)
    elif k == 2:
        matrix.key = MatrixType.diagonal
        matrix.obj = Diagonal()
        diagonal_read_from(matrix.obj, stream)
    elif k == 3:
        matrix.key = MatrixType.triangle
        matrix.obj = Triangle()
        triangle_read_from(matrix.obj, stream)
    else:
        return 0

    return matrix


def matrix_write_to(matrix, stream):
    if matrix.key == MatrixType.two_dimensional_array:
        stream.write(f'\tThis is two-dimensional array\n')
        two_dimensional_array_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
    elif matrix.key == MatrixType.diagonal:
        stream.write(f'\tThis is diagonal matrix\n')
        diagonal_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
    elif matrix.key == MatrixType.triangle:
        stream.write('\tThis is triangle matrix\n')
        triangle_write_to(matrix.obj, stream)
    else:
        stream.write('Error type\n')

    stream.write(f'\tSum: {matrix_sum(matrix.obj)}\n')
    stream.write(f'\tSize: {matrix.size}\n')
    stream.write(f'\t\tOutput type: {matrix.out_type}\n')


def matrix_sum(matrix):
    s = 0
    for item in matrix.data:
        if isinstance(item, int):
            s += item
        else:
            s += sum(item)
    return s


def compare(first, second):
    return matrix_sum(first) < matrix_sum(second)


class TwoDimArray:
    def __init__(self):
        self.data = []


class Diagonal:
    def __init__(self):
        self.data = None


class Triangle:
    def __init__(self):
        self.data = []
