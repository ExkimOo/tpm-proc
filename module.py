import sys
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
    container.data = []


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


def container_write_two_dimensional_array_to(container, stream):
    stream.write('Only two dimensional arrays\n')

    for item in container.data:
        if item.key == MatrixType.two_dimensional_array:
            matrix_write_to(item, stream)


def container_check_matrices(container):
    matrices_1 = [item for item in container.data]
    matrices_2 = matrices_1.copy()

    for matrix_1 in matrices_1:
        for matrix_2 in matrices_2:
            check_matrices(matrix_1, matrix_2)


def check_matrices(matrix_1, matrix_2):
    match matrix_1.obj, matrix_2.obj:
        case TwoDimArray(), TwoDimArray():
            print("Matrices are the same type: TwoDimArray and TwoDimArray")

        case TwoDimArray(), Diagonal():
            print("Matrices are different type: TwoDimArray and Diagonal")

        case TwoDimArray(), Triangle():
            print("Matrices are different type: TwoDimArray and Triangle")

        case Diagonal(), TwoDimArray():
            print("Matrices are different type: Diagonal and TwoDimArray")

        case Diagonal(), Diagonal():
            print("Matrices are the same type: Diagonal and Diagonal")

        case Diagonal(), Triangle():
            print("Matrices are different type: Diagonal and Triangle")

        case Triangle(), TwoDimArray():
            print("Matrices are different type: Triangle and TwoDimArray")

        case Triangle(), Diagonal():
            print("Matrices are different type: Triangle and Diagonal")

        case Triangle(), Triangle():
            print("Matrices are the same type: Triangle and TwoDimArray")

        case _:
            print('Unknown type')
            return

    print(f"First: {matrix_1}, second: {matrix_2}")
    print()


def two_dimensional_array_read_from(matrix, stream, size):
    try:
        for i in range(size):
            line = stream.readline().rstrip('\n')
            matrix.data.append(list(map(lambda x: int(x), line.split())))
    except:
        print('Reading two-dimensional array from file error')
        stream.close()
        sys.exit(1)


def two_dimensional_array_write_to(matrix, stream, size, out_type):
    try:
        if out_type == 1:
            stream.write('\t\t')
            for i in range(size):
                for j in range(size):
                    stream.write(f'{matrix.data[i][j]} ')
                stream.write('\n\t\t')

        elif out_type == 2:
            for i in range(size):
                for j in range(size):
                    stream.write(f'{matrix.data[j][i]} ')
                stream.write('\n\t\t')

        elif out_type == 3:
            for i in range(size):
                for j in range(size):
                    stream.write(f'{matrix.data[i][j]} ')
            stream.write('\n\t\t')
        else:
            stream.write('\tError matrix output type\n')
    except:
        print('Writing two-dimensional array to file error')
        stream.close()
        sys.exit(1)


def diagonal_read_from(matrix, stream):
    try:
        matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))
    except:
        print('Reading diagonal matrix from file error')
        stream.close()
        sys.exit(1)


def diagonal_write_to(matrix, stream, size, out_type):
    try:
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
        else:
            stream.write('\tError matrix output type\n')
    except:
        print('Writing diagonal matrix to file error')
        stream.close()
        sys.exit(1)


def triangle_read_from(matrix, stream):
    try:
        matrix.data = list(map(lambda x: int(x), stream.readline().rstrip('\n').split()))
    except:
        print('Reading triangle matrix from file error')
        stream.close()
        sys.exit(1)


def triangle_write_to(matrix, stream, size, out_type):
    try:
        if out_type == 1 or out_type == 2:
            stream.write('\t\t')
            index = 0
            for i in range(size):
                for j in range(size):
                    if j >= i:
                        stream.write(str(matrix.data[index]) + ' ')
                        index += 1
                    else:
                        stream.write('0 ')
                stream.write('\n\t\t')

        elif out_type == 3:
            stream.write('\t\t')
            for i in range(size):
                for j in range(size):
                    stream.write('{} '.format(matrix.data[i] if i == j else 0))
        else:
            stream.write('\tError matrix output type\n')
    except:
        print('Writing triangle matrix to file error')
        stream.close()
        sys.exit(1)


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
    try:
        k = int(line)
    except Exception:
        print('Reading type of matrix error')
        stream.close()
        sys.exit(1)

    matrix = Matrix()
    try:
        matrix.size = int(stream.readline().rstrip('\n'))
    except Exception:
        print('Reading size error')
        stream.close()
        sys.exit(1)
    try:
        matrix.out_type = int(stream.readline().rstrip('\n'))
    except Exception:
        print('Reading out type error')
        stream.close()
        sys.exit(1)

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
    try:
        if matrix.key == MatrixType.two_dimensional_array:
            stream.write(f'\tThis is two-dimensional array\n')
            two_dimensional_array_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
        elif matrix.key == MatrixType.diagonal:
            stream.write(f'\tThis is diagonal matrix\n')
            diagonal_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
        elif matrix.key == MatrixType.triangle:
            stream.write('\tThis is triangle matrix\n')
            triangle_write_to(matrix.obj, stream, matrix.size, matrix.out_type)
        else:
            stream.write('Error type\n')
            sys.exit(1)
    except Exception:
        print('Writing matrix type to file error')
        stream.close()
        sys.exit(1)

    try:
        stream.write(f'Sum: {matrix_sum(matrix.obj)}\n')
        stream.write(f'\t\tSize: {matrix.size}\n')
        stream.write(f'\t\tOutput type: {matrix.out_type}\n')
    except Exception:
        print('Writing matrix properties to file error')
        stream.close()
        sys.exit(1)


def matrix_sum(matrix):
    try:
        s = 0
        for item in matrix.data:
            if isinstance(item, int):
                s += item
            else:
                s += sum(item)
        return s
    except Exception:
        print('Sum calculation error')


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
