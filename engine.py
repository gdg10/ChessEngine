""" 
Inforcer of the rules:
	-Determines if a move is legal
	-Determines check, and checkmate
"""

import board, piece, copy

class engine:

	def isCheckmate(self, board):
		
		# determine which army may be in check or checkmate
		checkColor = self.getOppositeColor(board.turn)	

		# if the king is not in check, its not in checkmate
		k = board.getPieceByKind("K", checkColor)
		if self.isCheck(board, k) == False:
			print("no checkmate")
			return False		
		else:
			# if the king is in check, determine if it can get out of it
			pcs = board.getPieces(checkColor)
			for p in pcs:
				print("checking if " + p.__str__() + " can move to prevent checkmate")
				for x in range(8):							
					for y in range(8):						# for each peice in your army
						sqr = [x, y]
						print("considering a move to: " + str(sqr))
						b = copy.deepcopy(board)					# copy the board
						b.nextTurn()
						success = b.movePiece(self, p.sqr, sqr)		# attempt move
						k = b.getPieceByKind("K", checkColor)
						if success:
							print("legal move...")
							if self.isCheck(b, k) == False:
								print("moving " + p.__str__() + " to " + str(sqr) + " can prevent checkmate")
								return False
							else:
								print("moving " + p.__str__() + "to " + str(sqr) + " cannot prevent checkmate")
						else:
							print("illegal move")
			print("King is in checkmate")
			return True

	#def getPosTree(n): 
		#n is number of levels

	#def getBoard ()
		# 

	def isCheck(self, board, p):
		# you're in check if your king is threatened
		print("Checking if " + p.__str__() + " is in check")
		check = self.isThreatened(board, p)
		
		if check == False:
			print(p.__str__() + " is not in check")	
		else:
			print(p.__str__() + " is in check")	
		return check

	def getOppositeColor(self, color):
		if color == 'w':
			c = 'b'
		else:
			c = 'w'
		return c

	def isThreatened(self, board, p):
		# a piece is threatened if any peice from the opposing army can legal move to its square
		print("Checking if " + p.__str__() + " is threatened")
		pcs = board.getPieces(self.getOppositeColor(p.color))
		for q in pcs:
			if self.isThreatening(board, q, p) == True:
				print(q.__str__() + " is threatening " + p.__str__())
				return True
		return False

	def isThreatening(self, board, p, q):
		print("checking if " + p.__str__() + " is threatening " + q.__str__())
		legal = p.isLegalMove(p.sqr, q.sqr, self.isCapture(p, q))
		clear = False
		if legal:
			clear = self.isClearPath(board, p, p.sqr, q.sqr)
		
		threatening = (legal and clear)
		if threatening == True:
			print(p.__str__() + " is threatening " + q.__str__())
		else:
			print(p.__str__() + " is not threatening " + q.__str__())
		return threatening

	def isCapture(self, p, q):
		return (q != None and q.color != p.color)

	def isLegalMove(self, board, startSqr, endSqr):
		p = board.getPiece(startSqr)	#piece being moved
		
		pieceClicked = (p != None)
		if pieceClicked == False:
			print("invalid move - no piece selected")
			return False
		
		isTurn = (p.color == board.turn)
		if isTurn == False:
			print("invalid move - not your turn")
			return False

		q = board.getPiece(endSqr)		#piece on destination sqr if one
		capture = self.isCapture(p, q);
		if p.isLegalMove(startSqr, endSqr, capture):
			if self.isClearPath(board, p, startSqr, endSqr):
				
				print("Checking that move doesnt put King in check...")
				b = copy.deepcopy(board)
				k = b.getPieceByKind("K", b.turn)
				kq = b.getPiece(endSqr)
				if capture:
					b.removePiece(kq);
				b.setPiece(endSqr, k)
				print(k.__str__())
				check = self.isCheck(b, k)

				if check == False:
					if q == None:
						print("valid move")
						return True;
					elif capture:
						print("valid capture")
						return True;
					else:
						print("invalid move or captures")
						return False
				else:
					print("invalid move - would result in check")
			else:
				print("invalid move - Cannot jump over pieces")	
				return False
		else:
			print("invalid move - peice cannot move to that square")
			return False
			
	
	def getMoveVector(self, startSqr, endSqr):
		return [endSqr[0]-startSqr[0],endSqr[1]-startSqr[1]]
		
	def getDistance(self, mV):
		d = math.sqrt(mV[0]*mV[0] + mV[1]*mV[1])
		return d
		
	def getPath(self, startSqr, endSqr):

		s = copy.deepcopy(startSqr);
		e = copy.deepcopy(endSqr);
		print("getting path between " + str(startSqr) +" and " + str(endSqr))

		moveVector = self.getMoveVector(s, e)
		if moveVector[0] != 0:
			xInc = int(moveVector[0]/abs(moveVector[0]))
		else:
			xInc = 0
		if moveVector[1] != 0:
			yInc = int(moveVector[1]/abs(moveVector[1]))
		else:
			yInc = 0
			
		path = []
		newSqr = s
		while 1:
			newSqr[0] = newSqr[0] + xInc
			newSqr[1] = newSqr[1] + yInc
			if newSqr == endSqr:
				break
			else:
				temp = [0,0]
				temp[0] = newSqr[0]
				temp[1] = newSqr[1]
				path.append(temp)
		print(path)
		return path

	def isClearPath(self, board, p, startSqr, endSqr):
		print("checking if " + p.__str__() + " has a clear path to " + str(endSqr))
		s = copy.deepcopy(startSqr);
		e = copy.deepcopy(endSqr);
		if p.kind == "K" or p.kind == "N":
			return True
		else:
			path = self.getPath(s, e)
			for x in range(len(path)):
				if board.isEmptySquare(path[x]) == False:
					print(p.__str__() + " does not have a clear path to " + str(endSqr) + ". Conflict at " + str(path[x]))
					return False
			print(p.__str__() + " has a clear path to " + str(endSqr))
			return True