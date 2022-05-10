import io

from module import (
    diagonal_read_from,
    diagonal_write_to,
    Diagonal,
    Matrix, MatrixType
)


def test_read_from():
    input = io.StringIO('5\n1\n1 2 3 4 5\n')
    matrix = Matrix()
    matrix.size = int(input.readline().rstrip('\n'))
    matrix.out_type = int(input.readline().rstrip('\n'))
    matrix.key = MatrixType.two_dimensional_array
    matrix.obj = Diagonal()
    diagonal_read_from(matrix.obj, input)
    input.seek(0)

    assert matrix.size == 5
    assert matrix.out_type == 1
    assert matrix.obj.data == [1, 2, 3, 4, 5]


def test_write_to():
    test_input = io.StringIO('\t\t1 0 0 0 0 \n'
                             '\t\t0 2 0 0 0 \n'
                             '\t\t0 0 3 0 0 \n'
                             '\t\t0 0 0 4 0 \n'
                             '\t\t0 0 0 0 5 \n'
                             '\t\t')

    input = io.StringIO()

    matrix = Matrix()
    matrix.size = 5
    matrix.out_type = 1
    matrix.key = MatrixType.two_dimensional_array
    matrix.obj = Diagonal()
    matrix.obj.data = [1, 2, 3, 4, 5]
    diagonal_write_to(matrix.obj, input, matrix.size, matrix.out_type)

    input.seek(0)

    assert input.read() == test_input.read()
