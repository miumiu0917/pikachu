import csv
from time import sleep


class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    LIGHT_BROWN = '\033[38;5;136m'
    BROWN = '\033[38;5;96m'
    END = '\033[0m'


def main():
    with open('data/0001.csv') as f:
        reader = csv.reader(f)
        one = '\n'.join([''.join(map(number2color, row)) for row in reader])
    with open('data/0002.csv') as f:
        reader = csv.reader(f)
        two = '\n'.join([''.join(map(number2color, row)) for row in reader])
    while True:
        print(one)
        sleep(0.5)
        print(two)
        sleep(0.5)


def number2color(s):
    color = Color.WHITE
    if s == '0':
        color = Color.WHITE
    elif s == '1':
        color = Color.BLACK
    elif s == '2':
        color = Color.YELLOW
    elif s == '3':
        color = Color.RED
    elif s == '4':
        color = Color.LIGHT_BROWN
    elif s == '5':
        color = Color.BROWN
    return color + '■■' + Color.END


if __name__ == '__main__':
    main()
