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

class Board:
	def __init__(self):
		self.render = None
		w, h = 8, 8;
		self.squares = [[None for x in range(w)] for y in range(h)] #creates 2d array and initializes with None

	def getPiece(self, sqr):
		return self.squares[sqr[0]][sqr[1]]

	def setPiece(self, sqr, p):
		self.squares[sqr[0]][sqr[1]] = p;

	def movePiece(self, startSqr, endSqr):
		p = self.getPiece(startSqr)
		q = self.getPiece(endSqr)
		if p == None:
			print("invalid move - no piece selected")
			return None
		elif p != None and q == None:
			self.setPiece(endSqr, p)
			self.setPiece(startSqr, None)
			print("valid move")
		elif p != None and q != None:
			if q.color == p.color:
				print("invalid capture - you cannont capture your own peice")
			else:
				self.setPiece(endSqr, p)
				self.setPiece(startSqr, None)
				print("valid capture")

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

class King(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'K'
		self.value = 20
		self.whiteImg = whiteKingImage
		self.blackImg = blackKingImage

class Queen(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'Q'
		self.value = 8
		self.whiteImg = whiteQueenImage
		self.blackImg = blackQueenImage

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

class Knight(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'N'
		self.value = 3
		self.whiteImg = whiteKnightImage
		self.blackImg = blackKnightImage

class Bishop(Piece):
	def __init__(self, color):
		Piece.__init__(self, color)
		self.kind = 'B'
		self.value = 3
		self.whiteImg = whiteBishopImage
		self.blackImg = blackBishopImage

# b = Board()
# b.setupDefault()
# print(b)

# b.movePiece([0,0],[3,3])
# print(b)

# b.movePiece([3,3],[1,1])
# print(b)

# b.movePiece([3,3],[7,7])
# print(b)

