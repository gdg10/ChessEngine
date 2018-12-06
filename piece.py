whiteKingImage = 'img/whiteKing.png'
whiteQueenImage = 'img/whiteQueen.png'
whiteRookImage = 'img/whiteRook.png'
whiteBishopImage = 'img/whiteBishop.png'
whiteKnightImage = 'img/whiteKnight.png'
whitePawnImage = 'img/whitePawn.png'
blackKingImage = 'img/blackking.png'
blackQueenImage = 'img/blackQueen.png'
blackRookImage = 'img/blackRook.png'
blackBishopImage = 'img/blackBishop.png' 
blackKnightImage = 'img/blackKnight.png'
blackPawnImage = 'img/blackPawn.png'

import math, copy, chess

class Piece:
	def __init__(self, color):
		self.render = None
		self.color = color

	def __str__(self):
		return self.color + self.kind + "  "

	def getImage(self):
		if self.color == 'w':
			return self.whiteImg
		else:
			return self.blackImg

	def isLegalMove(self, startSqr, endSqr, capture):
		return True
	
	def getMoveVector(self, startSqr, endSqr):
		return [endSqr[0]-startSqr[0],endSqr[1]-startSqr[1]]
	
	def getDistance(self, mV):
		d = math.sqrt(mV[0]*mV[0] + mV[1]*mV[1])
		print(d)
		return d

class King(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'K'
		self.value = 20
		self.whiteImg = whiteKingImage
		self.blackImg = blackKingImage

	def isLegalMove(self, startSqr,endSqr, capture):
		moveVector = self.getMoveVector(startSqr, endSqr)
		distance = self.getDistance(moveVector)
		if(distance == 1 or distance == math.sqrt(2)):
			return True
		else:
			return False
		
class Queen(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'Q'
		self.value = 8
		self.whiteImg = whiteQueenImage
		self.blackImg = blackQueenImage
	
	def isLegalMove(self, startSqr, endSqr, capture):
		moveVector = self.getMoveVector(startSqr, endSqr)
		if(abs(moveVector[0]) == abs(moveVector[1]) and moveVector != [0,0]): 
			return True
		elif(moveVector[0] != 0 and moveVector[1] == 0): 
			return True
		elif(moveVector[1] != 0 and moveVector[0] == 0):
			return True
		else:
			return False

class Pawn(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = ' '
		self.value = 1
		self.whiteImg = whitePawnImage
		self.blackImg = blackPawnImage
		self.neverMoved = True
	
	def correctDirection(self, mV):
		if self.color == 'b' and mV[1] > 0:
			return True
		elif self.color == 'w' and mV[1] < 0:
			return True
		else:
			return False
			
	def isLegalMove(self, startSqr, endSqr, capture):
		mV = self.getMoveVector(startSqr, endSqr)
		d = self.getDistance(mV)
		if(d == 1 and self.correctDirection(mV) == True):	#Pawn may move 1 square "forward"
			return True
		elif(d == 2 and self.correctDirection(mV) == True and self.neverMoved == True): #Pawn may move 2 squares "forward" if first turn
			self.neverMoved = False
			return True
		elif(d == math.sqrt(2) and self.correctDirection(mV) and capture):
			return True
		else:
			return False

class Rook(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'R'
		self.value = 5
		self.whiteImg = whiteRookImage
		self.blackImg = blackRookImage

	def isLegalMove(self, startSqr, endSqr, capture):
		moveVector = self.getMoveVector(startSqr, endSqr)
		if(moveVector[0] != 0 and moveVector[1] == 0): 
			return True
		elif(moveVector[1] != 0 and moveVector[0] == 0):
			return True
		else:
			return False

class Knight(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'N'
		self.value = 3
		self.whiteImg = whiteKnightImage
		self.blackImg = blackKnightImage
		
	def isLegalMove(self, startSqr,endSqr, capture):
		moveVector = self.getMoveVector(startSqr, endSqr)
		distance = self.getDistance(moveVector)
		if(distance == math.sqrt(5)):
			return True
		else:
			return False

class Bishop(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'B'
		self.value = 3
		self.whiteImg = whiteBishopImage
		self.blackImg = blackBishopImage

	def isLegalMove(self, startSqr, endSqr, capture):
		moveVector = self.getMoveVector(startSqr, endSqr)
		if(abs(moveVector[0]) == abs(moveVector[1]) and moveVector != [0,0]): 
			return True
		else:
			return False