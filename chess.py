#should represent a chess board. 
#be able to read in a position and write it out to a file. 
#be able to print to the console
#eventaul link to GUI

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

import math
import copy 

class Board:
	def __init__(self):
		self.render = None
		w, h = 8, 8;
		self.squares = [[None for x in range(w)] for y in range(h)] #creates 2d array and initializes with None

	def getMoveVector(self, startSqr, endSqr):
		return [endSqr[0]-startSqr[0],endSqr[1]-startSqr[1]]
		
	def getDistance(self, mV):
		d = math.sqrt(mV[0]*mV[0] + mV[1]*mV[1])
		print(d)
		return d
		
	def isClearPath(self, startSqr, endSqr): #BUG!
		p = self.getPiece(startSqr)
		if p.kind == "K" or p.kind == "N":
			return True
		else:
			path = self.getPath(startSqr, endSqr)
			print(path)
			for x in range(len(path)):
				if self.isEmptySquare(path[x]) == False:
					return False
			return True

	def getPath(self, startSqr, endSqr):
		moveVector = self.getMoveVector(startSqr, endSqr)
		if moveVector[0] != 0:
			xInc = int(moveVector[0]/abs(moveVector[0]))
		else:
			xInc = 0
		if moveVector[1] != 0:
			yInc = int(moveVector[1]/abs(moveVector[1]))
		else:
			yInc = 0
			
		path = []
		newSqr = startSqr
		while 1:
			newSqr[0] = newSqr[0] + xInc
			newSqr[1] = newSqr[1] + yInc
			print(newSqr)
			if newSqr == endSqr:
				break
			else:
				temp = [0,0]
				temp[0] = newSqr[0]
				temp[1] = newSqr[1]
				path.append(temp)
		return path
	
	def getPiece(self, sqr):
		if sqr[0] >= 0 and sqr[0] <=7:
			if sqr[1] >= 0 and sqr[1] <=7:
				return self.squares[sqr[1]][sqr[0]] #note that this is reversed
		else:
			print("Not a square")
			return None
	
	def isEmptySquare(self, sqr):
		p = self.getPiece(sqr)
		if p == None:
			return True
		else:
			return False
			
	def setPiece(self, sqr, p):
		print("Setting piece " + str(sqr))
		self.squares[sqr[1]][sqr[0]] = p;

	def movePiece(self, startSqr, endSqr):
	
		p = self.getPiece(startSqr)
		q = self.getPiece(endSqr)
		s = copy.deepcopy(startSqr);
		e = copy.deepcopy(endSqr);
		if p != None:
			if p.isLegalMove(startSqr, endSqr) == True:
				if self.isClearPath(startSqr,endSqr) == True:
					if q == None or q.color != p.color:
						print(endSqr)
						print(startSqr)
						print(e)
						print(s)
						self.setPiece(e, p)
						self.setPiece(s, None) # bug here. s to end square
						print("valid move")
					else:
						print("invalid capture or move")
				else:
					print("Invalid move - Cannot jump over pieces")	
			else:
				print("invalid move: peice cannot move to that square")
		else:
			print("invalid move - no piece selected")
			

	def setupDefault(self):
		self.squares[0][0] = Rook("b")	#setup the black army
		self.squares[0][1] = Knight("b")
		self.squares[0][2] = Bishop("b")
		self.squares[0][3] = Queen("b")
		self.squares[0][4] = King("b")
		self.squares[0][5] = Bishop("b")
		self.squares[0][6] = Knight("b")
		self.squares[0][7] = Rook("b")
		self.squares[1][0] = Pawn("b")
		self.squares[1][1] = Pawn("b")
		self.squares[1][2] = Pawn("b")
		self.squares[1][3] = Pawn("b")
		self.squares[1][4] = Pawn("b")
		self.squares[1][5] = Pawn("b")
		self.squares[1][6] = Pawn("b")
		self.squares[1][7] = Pawn("b")

		self.squares[7][0] = Rook("w")	#setup the white army
		self.squares[7][1] = Knight("w")
		self.squares[7][2] = Bishop("w")
		self.squares[7][3] = Queen("w")
		self.squares[7][4] = King("w")
		self.squares[7][5] = Bishop("w")
		self.squares[7][6] = Knight("w")
		self.squares[7][7] = Rook("w")
		self.squares[6][0] = Pawn("w")
		self.squares[6][1] = Pawn("w")
		self.squares[6][2] = Pawn("w")
		self.squares[6][3] = Pawn("w")
		self.squares[6][4] = Pawn("w")
		self.squares[6][5] = Pawn("w")
		self.squares[6][6] = Pawn("w")
		self.squares[6][7] = Pawn("w")

	def writeToFile(self, fName):
		fo = open(fName, "wb+")
		fo.write(self.__str__())
		fo.close()

	def readFromFile(self,fName):
		fo = open(fName, "Wb+")
		buf = fo.read(500)
		#finish todo

	def __str__(self):
		boardStr = ''
		for x in range(8):
			for y in range(8):
				boardStr = boardStr + self.squares[x][y].__str__() + ' '
			if x != 7:
				boardStr = boardStr + '\n'
		return boardStr

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

	def isLegalMove(self, startSqr, endSqr):
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

	def isLegalMove(self, startSqr,endSqr):
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
	
	def isLegalMove(self, startSqr, endSqr):
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


class Rook(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'R'
		self.value = 5
		self.whiteImg = whiteRookImage
		self.blackImg = blackRookImage

	def isLegalMove(self, startSqr, endSqr):
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
		
	def isLegalMove(self, startSqr,endSqr):
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

	def isLegalMove(self, startSqr, endSqr):
		moveVector = self.getMoveVector(startSqr, endSqr)
		if(abs(moveVector[0]) == abs(moveVector[1]) and moveVector != [0,0]): 
			return True
		else:
			return False