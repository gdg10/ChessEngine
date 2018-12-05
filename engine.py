import chess, copy
class engine:
	def getMove(self, board):
		pieces = getPieces(board.turn, board)	#return a list of pieces that can be moved
		for piece in pieces:
			
	
	def getPieces(self, color, board):
		pieces = []
		for x in range(8):
			for y in range(8):
				p = board.getPiece(x,y)
				if p != None:
					if p.color == color
						pieces.append(copy.deepCopy(p))
		return pieces