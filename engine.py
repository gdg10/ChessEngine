import chess, copy
class engine:
	def getMove(self, board):
		pieces = self.getPieces(board.turn, board)	#return a list of pieces that can be moved
		for piece in pieces:
			self.calcBestMove(piece)
		return move
			
	def getPieces(self, color, board):
		pieces = []
		for x in range(8):
			for y in range(8):
				p = board.getPiece(x,y)
				if p != None:
					if p.color == color
						pieces.append([copy.deepCopy(p),[x,y]])
		return pieces

	def calcBestMove(piece):

class move:
	def __init__(piece, startSqr, endSqr, weight):
		self.piece = piece
		self.startSqr = startSqr
		self.endSqr = endSqr
		self.weight = weight;

	def compare(move):
		if self.weight > move.weight:
			return self
		else:
			return move