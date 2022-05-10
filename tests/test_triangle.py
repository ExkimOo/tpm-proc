import io

from module import (
    Triangle,
    triangle_read_from,
    triangle_write_to,
    Matrix,
    MatrixType
)


def test_read_from():
    input = io.StringIO('3\n1\n1 2 3 4 5 6\n')
    matrix = Matrix()
    matrix.size = int(input.readline().rstrip('\n'))
    matrix.out_type = int(input.readline().rstrip('\n'))
    matrix.key = MatrixType.two_dimensional_array
    matrix.obj = Triangle()
    triangle_read_from(matrix.obj, input)
    input.seek(0)

    assert matrix.size == 3
    assert matrix.out_type == 1
    assert matrix.obj.data == [1, 2, 3, 4, 5, 6]


def test_write_to():
    test_input = io.StringIO('\t\t1 2 3 \n\t\t0 4 5 \n\t\t0 0 6 \n\t\t')

    input = io.StringIO()

    matrix = Matrix()
    matrix.size = 3
    matrix.out_type = 1
    matrix.key = MatrixType.two_dimensional_array
    matrix.obj = Triangle()
    matrix.obj.data = [1, 2, 3, 4, 5, 6]
    triangle_write_to(matrix.obj, input, matrix.size, matrix.out_type)

    input.seek(0)
    # print()
    # print(input)

    assert input.read() == test_input.read()
