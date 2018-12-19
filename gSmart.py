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

	def getNextMove(self, b, n):
		gt = gameTree(b, n)		#create a gameTree of n ply
		return gt.miniMax()		#use miniMax algo to return the best move

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
		
		totalWeight = -1*weightedPosition[0] + weightedPosition[1]
		print("total weight: " + totalWeight)
		
		return totalWeight

	class gameTree():

		def __init__(self, b, n):				#builds a game tree of "n" ply from board "b"
			self.t = gSmart.gameTree.tree(b)	#create a tree
			cur = self.t.getRoot()				#grab the root
			self.addPly(cur, b, 3)				#build out "h" ply

		def addPly(self, curNode, b, ply):
			if ply == 0:			#basecase
				return
			else:
				moves = getAllNextMoves(curNode.board)	#get moves for board in current node
				for move in moves:						
					temp = gameTree.tree.node(b,move,mm)		#make a new node for each move
					curNode.addChild(temp)						#add the new node as a child to curNode
					self.addPly(temp, b, ply-1)					#recursively call addPly on the child, with one less ply
		
		def getMinOrMax(self, b):
			if b.getTurn == "w":
				return "max"
			else:
				return "min"
				
		def minimax(self):
			return None

		class tree:
		
			def __init__(self, b = None, m= None):
				self.root = gSmart.gameTree.tree.node(b, m)
		
			def getRoot(self):
				return self.root
				
			def addNode(self, parent, child):
				parent.addChild(child)
		
			def DFS(self, start):
				print(str(start))
				children = start.getChildren()
				if(len(children) == 0):
					return
				else:
					for child in children:
						self.DFS(child)
				
			class node:
			
				def __init__(self, b = None, m = None):
					self.children = []
					self.board = b
					self.move = m
					self.value = None
				
				def addChild(self, newChild):
					self.children.append(newChild)
				
				def getChildren(self):
					return self.children
					
				def getData(self):
					return self.data
					
				def setValue(self, v):
					if v == None:
						self.value = self.getBoardValue()
					else:
						self.value = v
					
				def getValue(self):
						return self.value
						
				def getBoardValue(self):
					return self.gSmart.evaluatePosition()
				
				def isMaxNode(self):
					return self.board.isTurn() == "w"

bd = board.Board()
bd.setupDefault()
gt = gSmart.gameTree(bd, 3)
t.DFS(gt.getRoot())