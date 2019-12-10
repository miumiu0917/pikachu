from mcpi import minecraft
import csv
from time import sleep

mc = None

def main():
    global mc
    mc = minecraft.Minecraft.create()
    mc.player.setTilePos(0, 0, 0)
    with open('data/0001.csv') as f:
        reader = csv.reader(f)
        one = [list(map(to_block_id, map(int, row))) for row in reader]
    with open('data/0002.csv') as f:
        reader = csv.reader(f)
        two = [list(map(to_block_id, map(int, row))) for row in reader]
    
    while True:
        put_block(one)
        # sleep(0.5)
        delete_block(one)
        put_block(two)
        # sleep(0.5)
        delete_block(one)


def put_block(table):
    for i, row in enumerate(reversed(table)):
        for j, cell in enumerate(reversed(row)):
            mc.setBlock(10, i, j+10, cell)


def delete_block(table):
    for i, row in enumerate(reversed(table)):
        for j, cell in enumerate(row):
            mc.setBlock(10, i, j+10, 0)


def to_block_id(i):
    if i == 1:
        return 14
    else:
        return i



if __name__ == '__main__':
    main()