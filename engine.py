# inforcer of the rules of chess
# is it a legal move? ask the engine

import board, copy
class engine:

	def isLegalMove(self, board, startSqr, endSqr):
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
						if q == None:
							self.setPiece(e, p)
							self.nextTurn()
							print("valid move")
						elif capture:
							self.pcsList.remove(q)
							self.setPiece(e, p)
							self.nextTurn()
							print("valid capture")
						else:
							print("Invalid move or captures")
					else:
						print("Invalid move - Cannot jump over pieces")	
				else:
					print("invalid move: peice cannot move to that square")
			else:
				print("invalid move - not your turn")
		else:
			print("invalid move - no piece selected")
	
	def getMoveVector(self, startSqr, endSqr):
		return [endSqr[0]-startSqr[0],endSqr[1]-startSqr[1]]
		
	def getDistance(self, mV):
		d = math.sqrt(mV[0]*mV[0] + mV[1]*mV[1])
		return d
		
	def isClearPath(self, board, startSqr, endSqr):
		p = board.getPiece(startSqr)
		if p.kind == "K" or p.kind == "N":
			return True
		else:
			path = self.getPath(startSqr, endSqr)
			for x in range(len(path)):
				if board.isEmptySquare(path[x]) == False:
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
			if newSqr == endSqr:
				break
			else:
				temp = [0,0]
				temp[0] = newSqr[0]
				temp[1] = newSqr[1]
				path.append(temp)
		return path
