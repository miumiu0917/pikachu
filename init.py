from mcpi import minecraft
import csv
from time import sleep

mc = None

def main():
    global mc
    mc = minecraft.Minecraft.create()
    mc.player.setTilePos(0, 0, 0)
    for i in range(-128, 0):
        for j in range(-128, 0):
            for k in range(-128, 30):
                mc.setBlock(i, j, k, 1)
                print(i, j, k)


if __name__ == '__main__':
    main()