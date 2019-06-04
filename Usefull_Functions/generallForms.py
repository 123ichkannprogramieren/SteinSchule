from mcpi.minecraft import Minecraft
from funtionShortForms import setBlocks, setBlock, getPos

def emptyRoom(x_start, y_start, z_start, x_end, y_end, z_end, blocktype):
    setBlocks(x_start, y_start, z_start, x_end, y_end, z_end, blocktype)
    setBlocks(x_start + 1, y_start + 1, z_start + 1, x_end - 1, y_end - 1, z_end - 1, 0)

def emptyRoomNextToPlayer(x_end, y_end, z_end, blocktype):
    x_start, y_start, z_start = getPos()
    setBlocks(x_start, y_start, z_start, x_end, y_end, z_end, blocktype)
    setBlocks(x_start + 1, y_start + 1, z_start + 1, x_end - 1, y_end - 1, z_end - 1, 0)

def getHeightForRooftop(length, width):
    if length < width:
        return int(length / 2)
    else:
        return int(width / 2)

def setRooftop(x, y, z, length, width):
    height = getHeightForRooftop(length, width)
    for i in range(height):
        setBlocks(x, y + i, z, x + length, y + i, z + width)

def getNumberForWindows(sizeWall):
    if sizeWall % 2 != 0:
        return int(sizeWall / 2) + 1
    else:
        return sizeWall / 2

def setWindowsInXAxis(x, y, z, length, height, width):
    numberOfWindows = getNumberForWindows(length)
    for i in range(numberOfWindows):
        setBlock(x + 1 + (i * 2), y + height, z, 20)
        setBlock(x + 1 + (i * 2), y + height, z + height, 20)

def setWindowsInZAxis(x, y, z, length, height, width):
    numberOfWindows = getNumberForWindows(length)
    for i in range(numberOfWindows):
        setBlock(x, y + height, z + 1 + (i * 2), 20)
        setBlock(x, y + height, z + 1 + (i * 2) + height, 20)