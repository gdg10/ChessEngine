""" 
TODO

Chess A.I.

"""

import engine, board, piece, numpy, copy

class gSmart:

	def __init__(self):
		self.e = engine.engine()
		self.mtrlW = .75
		self.dvlpW = 1
		self.aggnW = 2
		self.defnW = 2
		self.thrndW = 2
		self.epW = 10

	def getNextMove(self, b):
		pcs = b.getPieces(b.turn)
		bestMove = []
		bestPosition = -200;
		moves = self.getAllNextMoves(b)
		for m in moves:
			pos = self.evaluatePosition(m[0])
			if b.turn == 'b':
				ps = pos[1]
			else:
				ps = pos[0]
			if ps > bestPosition:
				bestPosition = ps
				bestMove = m
		print("The best move is: " + str(bestMove))
		return bestMove

	def getAllNextMoves(self, b):
		pcs = b.getPieces(b.turn)
		nextMoves = []
		for p in pcs:
			for x in range(8):
				for y in range(8):
					futureB = copy.deepcopy(b)
					success = futureB.movePiece(self.e, p.sqr, [x,y])
					if success == True:
						nextMoves.append([futureB, [p.sqr], [x,y]])
		# print(nextMoves)
		return nextMoves

	def evaluatePosition(self, b):

		mtrl = b.getMaterialSums()
		dvlp = self.e.getDevelopment(b)
		agg = self.e.getAggression(b)
		defn = self.e.getDefense(b)
		thrnd = self.e.getThreatened(b)
		ep = self.e.getEnPrise(b)

		# print("Material: \t" + str(mtrl))
		# print("Development: \t" + str(dvlp))
		# print("Aggression: \t" + str(agg))
		# print("Defense: \t" + str(defn))
		# print("Threatened:\t" + str(thrnd))
		# print("En Prise: \t" + str(ep))


		metrics = [mtrl, dvlp, agg, defn, thrnd, ep]
		weights = [self.mtrlW, self.dvlpW, self.aggnW, self.defnW, self.thrndW, self.epW]
		
		position = [0,0]
		for x in range(len(metrics)):
			for y in range(2):
				position[y]+=metrics[x][y]
		# print("Position: " + str(position))

		weightedMetrics = [ [weights[x]*metrics[x][0], weights[x]*metrics[x][1]] for x in range(len(weights))]
		weightedPosition = [0,0]
		for x in range(len(metrics)):
			for y in range(2):
				weightedPosition[y]+=weightedMetrics[x][y]
		# print("Weighted Position: " + str(weightedPosition))

		return weightedPosition
