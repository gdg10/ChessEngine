"""
gameTree

"""
class gameTree:

	def __init__(b, h):
		#builds a game tree of ply "h" from board "b"
		
		#create a tree
		self.t = tree(b)
		
		
		#build from the root node down
		cur = t.getRoot()
		for i in range(h):
		
			#get moves for board in current node
			moves = cur.board.getMoves()
			
			#make a node for each move
			for move in moves:
				self.t.addNode(cur, node(b))
			
			
			
		
		
	def minimax():

	class tree:
	
		root = None
	
		def __init__()
			root = node()
	
		def addNode(parent, child):
			parent.addChild(child)
	
		def DFS(start, n):
			cur
			for child in n.children:
				DFS(child)
			
	
		class node:
		
			def __init__(c = [], d = None, mm = None):
				self.children = c
				self.data = d
				self.minOrMax = mm
			
			def addChild(newChild):
				self.children.append(newChild)
			
			def getData():
				return self.data
			
		