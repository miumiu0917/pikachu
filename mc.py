import minecraft
import csv
from time import sleep

mc = None

def main():
    global mc
    mc = minecraft.Minecraft.create()
    mc.player.setTilePos(0, 0, 0)
    with open('data/0001.csv') as f:
        reader = csv.reader(f)
        one = [list(map(int, row)) for row in reader]
    with open('data/0002.csv') as f:
        reader = csv.reader(f)
        two = [list(map(int, row)) for row in reader]
    
    while True:
        put_block(one)
        sleep(0.5)
        put_block(two)
        sleep(0.5)


def put_block(table):
    for i, row in enumerate(table):
        for j, cell in enumerate(row):
            mc.setBlock(0, i, j, cell)


if __name__ == '__main__':
    main()