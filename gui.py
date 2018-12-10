# the graphic user interface
# displays board
# provides the user access to some board methods
# also contains game loop

#import everything
import os, pygame, board, math, engine, sys, gSmart
from pygame.locals import *

boardImage = 'img/chessboard.jpg'     #image of chessboard used for background
gameSize = 600
gameMode = 2
#gameMode = 1 --> human white v human black
#gameMode = 2 --> human white v computer black 
#gameMode = 3 --> computer white v computer black

def coorToSquare(coor):
	#for a set of coor, returns the sqr indices
	sqr = [0,0]
	sqr[0] = int(math.floor(coor[0]/(gameSize/8)))
	sqr[1] = int(math.floor(coor[1]/(gameSize/8)))
	return sqr

def squareToCoor(sqr):
	#for a given square, returns its top left coordinates
	coor = [0,0]
	coor[0] = int(math.floor(sqr[0]*((gameSize)/8))+(gameSize/32))
	coor[1] = int(math.floor(sqr[1]*((gameSize)/8)))
	return coor

def renderBoard(board, screen):
	#renders the board on to the screen
	if board.render == None: #only render once then store
		board.render = pygame.image.load(boardImage).convert()
		board.render = pygame.transform.scale(board.render, (gameSize, gameSize))
	screen.blit(board.render, (0, 0))
	return screen

def renderPieces(board, screen):
	pl = board.getPieces(None);
	print(pl)
	for x in range(len(pl)):
		p = pl[x]
		render = getRender(p) #render an image of that piece
		screen.blit(render, squareToCoor(p.sqr)) #stage
	return screen

def getRender(piece):
	if piece.render == None: #only render once then store
		image = piece.getImage()
		piece.render = pygame.image.load(image).convert_alpha()
		piece.render = pygame.transform.scale(piece.render, (int(gameSize/16), int(2*gameSize/16)))
	return piece.render

def main():
	pygame.init()
	screen = pygame.display.set_mode((gameSize, gameSize))

	b = board.Board()
	#b.setupDefault()
	b.setupCheckmate()

	screen = renderBoard(b, screen)
	screen = renderPieces(b, screen)
	pygame.display.update()

	startSqr = [0,0]
	endSqr = [0,0]

	e = engine.engine()
	g = gSmart.gSmart()

	size = sys.getsizeof(board)
	print(size)
	print(size/16)
	checkmate = False
	while checkmate == False:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if gameMode == 1 or gameMode ==2:
				if event.type == MOUSEBUTTONDOWN:
					startSqr = coorToSquare(event.pos)
				elif event.type == MOUSEBUTTONUP:
					endSqr = coorToSquare(event.pos)
					success = b.movePiece(e, startSqr, endSqr)
					if success:
						screen = renderBoard(b, screen)
						screen = renderPieces(b, screen)
						pygame.display.update()

						print("Checking if " + e.getOppositeColor(b.turn) + " is checkmated")
						if e.isCheckmate(b):
							print(b.turn + " wins")
							checkmate = True
						else:
							g.evaluatePosition(b)
							b.nextTurn()
							if gameMode ==2:
								move = g.getNextMove(b)
								print("m: " + str(move))
								b.movePiece(e, move[1][0], move[1][1])
								screen = renderBoard(b, screen)
								screen = renderPieces(b, screen)
								pygame.display.update()
								print("Checking if " + e.getOppositeColor(b.turn) + " is checkmated")
								if e.isCheckmate(b):
									print(b.turn + " wins")
									checkmate = True
								else:
									g.evaluatePosition(b)
									b.nextTurn()

if __name__ == '__main__': main()