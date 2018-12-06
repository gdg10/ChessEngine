#should represent a chess board. 
#be able to read in a position and write it out to a file. 
#be able to print to the console
#eventaul link to GUI
import math, copy, piece

class Board:
	def __init__(self):
		self.render = None
		w, h = 8, 8;
		self.squares = [[None for x in range(w)] for y in range(h)] #creates 2d array and initializes with None
		self.turn = "w"
		
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
	
	def nextTurn(self):
		if self.turn == 'w':
			self.turn = 'b'
		else:
			self.turn = 'w'

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
		s = copy.deepcopy(startSqr);	#deep copy needed to avoid pointer errors in helper methods
		e = copy.deepcopy(endSqr);		#deep copy needed to avoid pointer errors in helper methods
		
		pieceClicked = (p != None)
		capture = (q != None and q.color != p.color)
		
		#validity check regular moves
		if pieceClicked:
			isTurn = (p.color == self.turn)
			if isTurn:
				if p.isLegalMove(startSqr, endSqr, capture):
					if self.isClearPath(startSqr,endSqr):
						if q == None or capture:
							self.setPiece(e, p)
							self.setPiece(s, None) 
							self.nextTurn()
							print("valid move")
						else:
							print("invalid capture or move")
					else:
						print("Invalid move - Cannot jump over pieces")	
				else:
					print("invalid move: peice cannot move to that square")
			else:
				print("invalid move - not your turn")
		else:
			print("invalid move - no piece selected")
			
	def setupDefault(self):

		self.squares[0][0] = piece.Rook("b")	#setup the black army
		self.squares[0][1] = piece.Knight("b")
		self.squares[0][2] = piece.Bishop("b")
		self.squares[0][3] = piece.Queen("b")
		self.squares[0][4] = piece.King("b")
		self.squares[0][5] = piece.Bishop("b")
		self.squares[0][6] = piece.Knight("b")
		self.squares[0][7] = piece.Rook("b")
		self.squares[1][0] = piece.Pawn("b")
		self.squares[1][1] = piece.Pawn("b")
		self.squares[1][2] = piece.Pawn("b")
		self.squares[1][3] = piece.Pawn("b")
		self.squares[1][4] = piece.Pawn("b")
		self.squares[1][5] = piece.Pawn("b")
		self.squares[1][6] = piece.Pawn("b")
		self.squares[1][7] = piece.Pawn("b")

		self.squares[7][0] = piece.Rook("w")	#setup the white army
		self.squares[7][1] = piece.Knight("w")
		self.squares[7][2] = piece.Bishop("w")
		self.squares[7][3] = piece.Queen("w")
		self.squares[7][4] = piece.King("w")
		self.squares[7][5] = piece.Bishop("w")
		self.squares[7][6] = piece.Knight("w")
		self.squares[7][7] = piece.Rook("w")
		self.squares[6][0] = piece.Pawn("w")
		self.squares[6][1] = piece.Pawn("w")
		self.squares[6][2] = piece.Pawn("w")
		self.squares[6][3] = piece.Pawn("w")
		self.squares[6][4] = piece.Pawn("w")
		self.squares[6][5] = piece.Pawn("w")
		self.squares[6][6] = piece.Pawn("w")
		self.squares[6][7] = piece.Pawn("w")

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
