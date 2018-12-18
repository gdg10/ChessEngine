# the graphic user interface
# displays board
# provides the user access to some board methods
# also contains game loop

#import everything
import os, pygame, board, math, engine, sys, gSmart, piece
from pygame.locals import *
import time

class gui:

	def __init__(self):
		
		self.gameSize = 500						#dictates size of window
		self.boardPath = 'img/chessboard.jpg' 	#path to image of chessboard used for background
		self.splashPath = 'img/splashScreen.png'
		self.splashRender = None
		self.boardRender = None
		self.screen = None
		kys = ["wK","wQ","wR","wB","wN","wP","bK","bQ","bR","bB","bN","bP" ]
		
		self.pathDict = {						#paths to images of peices
		"wK" : 'img/whiteKing.png',	
		"wQ" : 'img/whiteQueen.png',
		"wR" : 'img/whiteRook.png',
		"wB" : 'img/whiteBishop.png',
		"wN" : 'img/whiteKnight.png',
		"wP" : 'img/whitePawn.png',
		"bK" : 'img/blackking.png',
		"bQ" : 'img/blackQueen.png',
		"bR" : 'img/blackRook.png',
		"bB" : 'img/blackBishop.png',
		"bN" : 'img/blackKnight.png',
		"bP" : 'img/blackPawn.png'}
		
		self.renderDict = {						#paths to Renders of peices
		"wK" : None,					
		"wQ" : None,
		"wR" : None,
		"wB" : None,
		"wN" : None,
		"wP" : None,
		"bK" : None,
		"bQ" : None,
		"bR" : None,
		"bB" : None,
		"bN" : None,
		"bP" : None }
		

		pygame.init()
		#self.screen = pygame.display.set_mode((self.gameSize, self.gameSize), RESIZABLE)
		self.screen = pygame.display.set_mode((self.gameSize, self.gameSize))
		pygame.display.set_caption("gSmart Chess")
		
		
		r = pygame.image.load(self.splashPath).convert()
		self.splashRender = pygame.transform.scale(r, (self.gameSize, self.gameSize))
		self.screen.blit(self.splashRender, (0, 0))
		
		
		pygame.display.update()
		#pygame.time.wait(2000)
		
		#fill in the render dictionaries
		self.createBoardRender()
		for k in kys:
			self.renderDict[k] = self.createPieceRender(self.pathDict[k])
		
		
	def push(self, board):
		# push the staged render to screen 
		self.renderBoard(board)
		self.renderPieces(board)
		pygame.display.update()
	
	def renderBoard(self, board):
		#renders the board on to the screen
		self.screen.blit(self.boardRender, (0, 0))

	def renderPieces(self, board):
		pl = board.getPieces(None);
		for p in pl:
			render = self.getRender(p) #render an image of that piece
			self.screen.blit(render, self.squareToCoor(p.sqr)) #stage

	def getRender(self, piece):
		k = piece.getKey();
		return self.renderDict[k]
			
	def createPieceRender(self, path):
		r = pygame.image.load(path).convert_alpha() #render
		r = pygame.transform.scale(r, (int(.92*self.gameSize/16), int(2*self.gameSize/16))) #scale
		return r
	
	def createBoardRender(self):
		r = pygame.image.load(self.boardPath).convert()
		self.boardRender = pygame.transform.scale(r, (self.gameSize, self.gameSize))
		
	def coorToSquare(self, coor):
		# helper method - translates a users "click" coordinates into a chess square index 
		sqr = [0,0]
		sqr[0] = int(math.floor(coor[0]/(self.gameSize/8)))
		sqr[1] = int(math.floor(coor[1]/(self.gameSize/8)))
		return sqr

	def squareToCoor(self, sqr):
		# helper method - translates a chess square index into coordinates
		coor = [0,0]
		coor[0] = int(math.floor(sqr[0]*((self.gameSize)/8))+(self.gameSize/32))
		coor[1] = int(math.floor(sqr[1]*((self.gameSize)/8)))
		return coor