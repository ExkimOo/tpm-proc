import sys

from module import (
    container_read_from,
    container_write_to,
    container_clear,
    container_sort,
    Container
)


def main():
    if len(sys.argv) != 3:
        print("Incorrect command line!\n"
              "Waited: command in_file out_file")
        sys.exit(1)

    input_file = open(sys.argv[1], "r")

    print('Start')

    container = Container(5)
    container_read_from(container, input_file)

    print('Filled container')

    container_sort(container)
    output_file = open(sys.argv[2], "w")
    container_write_to(container, output_file)

    container_clear(container)

    print('Empty container')
    container_write_to(container, output_file)

    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
