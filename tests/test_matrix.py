import io

import pytest

from module import (
    matrix_sum,
    matrix_read_from,
    matrix_write_to,
    Matrix,
    MatrixType,
    Diagonal,
    TwoDimArray,
    Triangle
)


def test_read_from():
    input = io.StringIO('2\n5\n1\n1 2 3 4 5\n')
    line = input.readline()
    matrix = matrix_read_from(input, line)
    input.seek(2)

    assert matrix.size == int(input.read(1))


def test_write_to():
    output = io.StringIO()
    matrix = Matrix()
    matrix.size = 5
    matrix.out_type = 1
    matrix.key = MatrixType.diagonal
    matrix.obj = Diagonal()
    matrix.obj.data = [1, 2, 3, 4, 5]
    matrix_write_to(matrix, output)

    output.seek(0)

    test_str = '''\tThis is diagonal matrix
		1 0 0 0 0 
		0 2 0 0 0 
		0 0 3 0 0 
		0 0 0 4 0 
		0 0 0 0 5 
		Sum: 15
		Size: 5
		Output type: 1\n'''

    assert output.read() == test_str


@pytest.mark.parametrize('input, s', [
    (io.StringIO('1\n2\n1\n1 2\n3 4\n'), 10),
    (io.StringIO('2\n5\n1\n1 2 3 4 5\n'), 15),
    (io.StringIO('3\n3\n1\n1 2 3 4 5 6\n'), 21),
])
def test_sum(input, s):
    line = input.readline()
    matrix = matrix_read_from(input, line)
    assert matrix_sum(matrix.obj) == s
