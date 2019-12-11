from mcpi import minecraft
import csv
from time import sleep

mc = None

def main():
    global mc
    mc = minecraft.Minecraft.create()
    with open('data/0001.csv') as f:
        reader = csv.reader(f)
        one = [list(map(to_block_id, map(int, row))) for row in reader]
    with open('data/0002.csv') as f:
        reader = csv.reader(f)
        two = [list(map(to_block_id, map(int, row))) for row in reader]

    put_block(one, -128, -103)
    
    put_block(two, -128, 0)
    
    while True:    
        sleep(2)
        mc.player.setTilePos(-108, 20, 10)
        sleep(2)
        mc.player.setTilePos(-108, 20, -93)


def put_block(table, x, y):
    for i, row in enumerate(reversed(table)):
        for j, cell in enumerate(reversed(row)):
            mc.setBlock(x, i, y+j, cell)


def delete_block(table):
    for i, row in enumerate(reversed(table)):
        for j, cell in enumerate(row):
            mc.setBlock(10, i, j+10, 0)


def to_block_id(i):
    if i == 1:
        return 49
    elif i == 2:
        return 41
    else:
        return i



if __name__ == '__main__':
    main()