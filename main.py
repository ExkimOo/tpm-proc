import sys

from module import (
    container_read_from,
    container_write_to,
    container_clear,
    container_sort,
    container_write_two_dimensional_array_to,
    container_check_matrices,
    Container
)


def main():
    if len(sys.argv) != 3:
        print("Incorrect command line!\n"
              "Waited: command in_file out_file")
        sys.exit(1)

    try:
        input_file = open(sys.argv[1], "r")
    except OSError:
        print('Opening file error')
        sys.exit(1)

    print('Start')

    container = Container(5)
    container_read_from(container, input_file)

    print('Filled container')

    # container_sort(container)
    try:
        output_file = open(sys.argv[2], "w")
    except OSError:
        print('Opening file error')
        sys.exit(1)
    finally:
        input_file.close()

    container_write_to(container, output_file)
    # container_write_two_dimensional_array_to(container, output_file)
    container_check_matrices(container)

    container_clear(container)

    print('Empty container')
    container_write_to(container, output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
