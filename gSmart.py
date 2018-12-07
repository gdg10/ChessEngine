""" 
TODO

Chess A.I.


	def getMove(self, board):
		
		pList = board.getPieces(board.turn)
		
		for p in pList:
			self.getAllMoves(p, board)
		
	#get a list of all possible moves a piece can make
	def getAllMoves(self, p, board):
		mList = []
		for x in range(8):
			for y in range(8):
				capture = getPiece([x,y])
				endSqr = [x,y]
				p.isLegalMove(p.sqr, endSqr, )

class move:
	def __init__(piece, startSqr, endSqr, weight):
		self.piece = piece
		self.endSqr = endSqr
		self.weight = weight;

	def compare(move):
		if self.weight > move.weight:
			return self
		else:
			return move

"""