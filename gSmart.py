""" 
TODO

Chess A.I.

"""
import os, pygame, board, math, engine, sys, gSmart
from pygame.locals import *

import engine, board, piece, copy

class gSmart:

	def __init__(self):
		self.e = engine.engine()
		self.mtrlW = .75
		self.dvlpW = 2
		self.aggnW = 2
		self.defnW = .5
		self.thrndW = 2
		self.epW = 10
		self.chkW = 50
		self.chkmtW = 1000

	def getNextMove(self, b):
		pcs = b.getPieces(b.turn)
		bestMove = []
		bestPosition = -200;
		moves = self.getAllNextMoves(b)
		for m in moves:
			pos = self.evaluatePosition(m[0])
			if b.turn == 'b':
				ps = pos[0]
			else:
				ps = pos[1]
			if ps > bestPosition:
				bestPosition = ps
				bestMove = m
		print("The best move is: " + str(bestMove))
		return bestMove[1]

	def getAllNextMoves(self, b):
		pcs = b.getPieces(b.turn)
		nextMoves = []
		for p in pcs:
			for x in range(8):
				for y in range(8):
					futureB = copy.deepcopy(b)
					success = futureB.movePiece(self.e, p.sqr, [x,y])
					if success == True:
						m = [p.sqr, [x,y]]
						nextMoves.append([futureB, m])
		# print(nextMoves)
		return nextMoves

	def evaluatePosition(self, b):

		mtrl = b.getMaterialSums()
		dvlp = self.e.getDevelopment(b)
		agg = self.e.getAggression(b)
		defn = self.e.getDefense(b)
		thrnd = self.e.getThreatened(b)
		ep = self.e.getEnPrise(b)
		chk = self.e.getCheck(b)
		chkmt = self.e.getCheckmate(b)
		
		#print("Unweighted")
		#print("Material: \t" + str(mtrl))
		#print("Development: \t" + str(dvlp))
		#print("Aggression: \t" + str(agg))
		#print("Defense: \t" + str(defn))
		#print("Threatened:\t" + str(thrnd))
		#print("En Prise: \t" + str(ep))
		#print("Check:    \t" + str(chk))
		#print("Checkmate: \t" + str(chkmt))
		#print("")

		metrics = [mtrl, dvlp, agg, defn, thrnd, ep, chk, chkmt]
		weights = [self.mtrlW, self.dvlpW, self.aggnW, self.defnW, self.thrndW, self.epW, self.chkW, self.chkmtW]
		
		position = [0,0]
		for x in range(len(metrics)):
			for y in range(2):
				position[y]+=metrics[x][y]
		# print("Position: " + str(position))

		weightedMetrics = [ [weights[x]*metrics[x][0], weights[x]*metrics[x][1]] for x in range(len(weights))]
		
		#print("Unweighted")
		#print("Material: \t" + str(weightedMetrics[0]))
		#print("Development: \t" + str(weightedMetrics[1]))
		#print("Aggression: \t" + str(weightedMetrics[2]))
		#print("Defense: \t" + str(weightedMetrics[3]))
		#print("Threatened:\t" + str(weightedMetrics[4]))
		#print("En Prise: \t" + str(weightedMetrics[5]))
		#print("Check:     \t" + str(weightedMetrics[6]))
		#print("Checkmate: \t" + str(weightedMetrics[7]))
		#print("")
		
		weightedPosition = [0,0]
		for x in range(len(metrics)):
			for y in range(2):
				weightedPosition[y]+=weightedMetrics[x][y]
		# print("Weighted Position: " + str(weightedPosition))

		#print("Weighted Posistion: " + str(weightedPosition))
		return weightedPosition
