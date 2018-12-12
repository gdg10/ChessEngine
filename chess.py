# main.py

import os, pygame, board, math, engine, sys, gSmart, gui
from pygame.locals import *


def main():
	c = chess()
	
class chess:

	def __init__(self):
		
		self.b = board.Board()
		self.e = engine.engine()
		self.g = gSmart.gSmart()
		self.gui = gui.gui()
		self.gameMode = 3
	
		self.b.setupDefault()
		#self.b.setupCheckmate()	
		self.gui.push(self.b)
		
		self.main()
		
	def main(self):
		
		print("main")
		if self.gameMode == 1:
			self.humanVhuman()
		elif self.gameMode == 2:
			self.humanVgSmart()
		elif self.gameMode == 3:
			self.gSmartVgSmart()
		#else:
		#	return

	def humanVhuman(self):
		startSqr = [0,0]
		endSqr = [0,0]
		win = False
			
		while win == False:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				if event.type == MOUSEBUTTONDOWN:
					startSqr = self.gui.coorToSquare(event.pos)
				elif event.type == MOUSEBUTTONUP:
					endSqr = self.gui.coorToSquare(event.pos)
					success = self.makeHumanMove([startSqr, endSqr])
					if success:
						win = self.checkForWin()
						self.b.nextTurn()
						print("nextTurn")

	def humanVgSmart(self):
		startSqr = [0,0]
		endSqr = [0,0]
		win = False
			
		while win == False:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				if event.type == MOUSEBUTTONDOWN:
					startSqr = self.gui.coorToSquare(event.pos)
				elif event.type == MOUSEBUTTONUP:
					endSqr = self.gui.coorToSquare(event.pos)
					success = self.makeHumanMove([startSqr, endSqr])
					if success:
						win = self.checkForWin()
						self.b.nextTurn()
						print("nextTurn")
						self.makeComputerMove();
						self.b.nextTurn()
						print("nextTurn")
	
	def gSmartVgSmart(self):
		win = False
			
		while win == False:
			self.makeComputerMove();
			win = self.checkForWin()
			self.b.nextTurn()
			print("nextTurn")
			
	def updateGUI(self):
		self.gui.push(self.b)
		
	def makeHumanMove(self, move):
		success = self.b.movePiece(self.e, move[0], move[1])
		if success:
			self.updateGUI()
		return success
	
	def makeComputerMove(self):
		move = self.g.getNextMove(self.b)
		print(move)
		success = self.b.movePiece(self.e, move[0], move[1])
		if success:
			print("-----------------------------------")
			self.g.evaluatePosition(self.b)
			self.updateGUI()
			
	def checkForWin(self):
		color = self.e.getOppositeColor(self.b.turn)
		k = self.b.getPieceByKind("K", color)
		if self.e.isCheckmate(self.b, k):
			print(self.b.turn + " wins")
			return True
		else:
			return False
			
if __name__ == '__main__': main()