import io

from module import (
    two_dimensional_array_read_from,
    two_dimensional_array_write_to,
    TwoDimArray,
    Matrix,
    MatrixType
)


def test_read_from():
    input = io.StringIO('1\n1\n5\n')
    matrix = Matrix()
    matrix.size = int(input.readline().rstrip('\n'))
    matrix.out_type = int(input.readline().rstrip('\n'))
    matrix.key = MatrixType.two_dimensional_array
    matrix.obj = TwoDimArray()
    two_dimensional_array_read_from(matrix.obj, input, matrix.size)
    input.seek(0)

    assert matrix.size == 1
    assert matrix.out_type == 1
    assert matrix.obj.data == [[5]]


def test_write_to():
    test_input = io.StringIO('\t\t1 2 \n\t\t3 4 \n\t\t')

    input = io.StringIO()

    matrix = Matrix()
    matrix.size = 2
    matrix.out_type = 1
    matrix.key = MatrixType.two_dimensional_array
    matrix.obj = TwoDimArray()
    matrix.obj.data = [[1, 2], [3, 4]]
    two_dimensional_array_write_to(matrix.obj, input, matrix.size, matrix.out_type)

    input.seek(0)

    assert input.read() == test_input.read()
