# an arrangement of pieces 
# and methods to access or change that arrangement 
# backend is a list

import math, copy, piece, engine

class Board:
	def __init__(self):
		self.render = None
		self.turn = "w"
		self.pcsList = [];

	def nextTurn(self):
		if self.turn == 'w':
			self.turn = 'b'
		else:
			self.turn = 'w'

	def getPiece(self, sqr):
		# iterate through the current list of pieces and check their sqr attribute
		# O(n) time where n is current number of Pieces in play
		if sqr[0] >= 0 and sqr[0] <=7:
			if sqr[1] >= 0 and sqr[1] <=7:
				for x in range(len(self.pcsList)):
					if self.pcsList[x].sqr == sqr:
						return self.pcsList[x]
				#print("Piece DNE")
				return None;
		else:
			#print("Not a square")
			return None

	def getPieceByKind(self, kind, color):
		for x in range(len(self.pcsList)):
			p = self.pcsList[x] 
			if p.color == color and p.kind == kind:
				return p
		return None

	def getPieces(self, color):
		# return the pieces of given color
		# if color == None, return all pieces
		# O(n) time where n is current number of Pieces in play
		# O(1) if color == None
		if color == None:
			return self.pcsList
		else:
			l = []
			for x in range(len(self.pcsList)):
				if self.pcsList[x].color == color:
					l.append(self.pcsList[x])
			return l

	def isEmptySquare(self, sqr):
		p = self.getPiece(sqr)
		if p == None:
			return True
		else:
			return False
	
	def movePiece(self, engine, startSqr, endSqr):
		p = self.getPiece(startSqr)
		#print("moving " + p.__str__() + " to " + str(endSqr))
		q = self.getPiece(endSqr)

		if engine.isLegalMove(self, startSqr, endSqr):
			if engine.isCapture(p, q):
				self.removePiece(q);
			self.setPiece(endSqr, p)
			return True
		else:
			return False

	def setPiece(self, sqr, p):
		print("Setting piece " + str(sqr))
		p.sqr = sqr;
		return p
	
	def removePiece(self, p):
		#print("Capturing " + p.__str__())
		self.pcsList.remove(p)

	def setupDefault(self):
		#setup the black army
		self.pcsList.append(self.setPiece([0,0], piece.Rook("b")))	
		self.pcsList.append(self.setPiece([1,0], piece.Knight("b")))
		self.pcsList.append(self.setPiece([2,0], piece.Bishop("b")))
		self.pcsList.append(self.setPiece([3,0], piece.Queen("b")))
		self.pcsList.append(self.setPiece([4,0], piece.King("b")))
		self.pcsList.append(self.setPiece([5,0], piece.Bishop("b")))
		self.pcsList.append(self.setPiece([6,0], piece.Knight("b")))
		self.pcsList.append(self.setPiece([7,0], piece.Rook("b")))
		self.pcsList.append(self.setPiece([0,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([1,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([2,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([3,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([4,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([5,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([6,1], piece.Pawn("b")))
		self.pcsList.append(self.setPiece([7,1], piece.Pawn("b")))
		
		#setup the white army
		self.pcsList.append(self.setPiece([0,7], piece.Rook("w")))	
		self.pcsList.append(self.setPiece([1,7], piece.Knight("w")))
		self.pcsList.append(self.setPiece([2,7], piece.Bishop("w")))
		self.pcsList.append(self.setPiece([3,7], piece.Queen("w")))
		self.pcsList.append(self.setPiece([4,7], piece.King("w")))
		self.pcsList.append(self.setPiece([5,7], piece.Bishop("w")))
		self.pcsList.append(self.setPiece([6,7], piece.Knight("w")))
		self.pcsList.append(self.setPiece([7,7], piece.Rook("w")))
		self.pcsList.append(self.setPiece([0,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([1,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([2,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([3,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([4,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([5,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([6,6], piece.Pawn("w")))
		self.pcsList.append(self.setPiece([7,6], piece.Pawn("w")))

	def setupCheckmate(self):
		#setup the black army
		self.pcsList.append(self.setPiece([0,0], piece.Rook("b")))	
		self.pcsList.append(self.setPiece([4,0], piece.King("b")))
		self.pcsList.append(self.setPiece([1,0], piece.Rook("b")))
		
		#setup the white army
		self.pcsList.append(self.setPiece([7,7], piece.King("w")))


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
				boardStr = boardStr + self.getPiece([y,x]).__str__() + ' '
			if x != 7:
				boardStr = boardStr + '\n'
		return boardStr

	def getMaterialSums(self):
		bMat = 0
		wMat = 0
		for p in self.pcsList:
			if p.color == "w":
				wMat+=p.value
			else:
				bMat+=p.value
		return [bMat, wMat]