This was our Project-Repository
rom mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getPos():
	pos = mc.player.getPos()
	x = pos.x
	y = pos.y
	z = pos.z
	return x, y, z

def getTilePos():
	pos = mc.player.getTilePos()
	x = pos.x
	y = pos.y
	z = pos.z
	return x, y, z

def getBlock(x, y, z):
	block = mc.player.getBlock(x, y, z)
	return block

def getHeight(x, z):
	height = mc.player.getHeight(x, y)
	return height

def postToChat(message):
	mc.player.postToChat(str(message))

def setBlock(x, y, z, blocktype):
	mc.setBlock(x, y, z, blocktype)

def setBlocks(x_start, y_start, z_start, x_end, y_end, z_end, blocktype):
	mc.setBlock(x_start, y_start, z_start, x_end, y_end, z_end, blocktype)

def setPos(x, y, z):
	mc.player.setPos(x, y, z)

def setTilePos(x, y, z):
	mc.player.setPos(int(x), int(y), int(z)) 
Das war Finn
