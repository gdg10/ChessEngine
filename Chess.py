#import everything
import os, pygame, pychess
from pygame.locals import *

def main():
	
	gameSize = 700

	pygame.init()
  	screen = pygame.display.set_mode((gameSize, gameSize))	#create the screen
	
	background = pychess.Board(gameSize)
  	screen.blit(background.render, (0, 0))

  	blackRook1 = pychess.Board.Rook('black', gameSize, 1*gameSize/32, 0*gameSize/32)
  	screen.blit(blackRook1.render,(blackRook1.x, blackRook1.y))

  	blackKnight1 = pychess.Board.Knight('black', gameSize, 5*gameSize/32, 0*gameSize/32)
  	screen.blit(blackKnight1.render,(blackKnight1.x, blackKnight1.y))

  	blackBishop1 = pychess.Board.Bishop('black', gameSize, 9*gameSize/32, 0*gameSize/32)
  	screen.blit(blackBishop1.render,(blackBishop1.x, blackBishop1.y))

  	blackQueen = pychess.Board.Queen('black', gameSize, 13*gameSize/32, 0*gameSize/32)
  	screen.blit(blackQueen.render,(blackQueen.x, blackQueen.y))

  	blackKing = pychess.Board.King('black', gameSize, 17*gameSize/32, 0*gameSize/32)
  	screen.blit(blackKing.render,(blackKing.x, blackKing.y))

  	blackBishop2 = pychess.Board.Bishop('black', gameSize, 21*gameSize/32, 0*gameSize/32)
  	screen.blit(blackBishop2.render,(blackBishop2.x, blackBishop2.y))

  	blackKnight2 = pychess.Board.Knight('black', gameSize, 25*gameSize/32, 0*gameSize/32)
  	screen.blit(blackKnight2.render,(blackKnight2.x, blackKnight2.y))

  	blackRook2 = pychess.Board.Rook('black', gameSize, 29*gameSize/32, 0*gameSize/32)
  	screen.blit(blackRook2.render,(blackRook2.x, blackRook2.y))

  	blackPawn1 = pychess.Board.Pawn('black', gameSize, 1*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn1.render,(blackPawn1.x, blackPawn1.y))

  	blackPawn2 = pychess.Board.Pawn('black', gameSize, 5*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn2.render,(blackPawn2.x, blackPawn2.y))

  	blackPawn3 = pychess.Board.Pawn('black', gameSize, 9*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn3.render,(blackPawn3.x, blackPawn3.y))

  	blackPawn4 = pychess.Board.Pawn('black', gameSize, 13*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn4.render,(blackPawn4.x, blackPawn4.y))

  	blackPawn5 = pychess.Board.Pawn('black', gameSize, 17*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn5.render,(blackPawn5.x, blackPawn5.y))

  	blackPawn6 = pychess.Board.Pawn('black', gameSize, 21*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn6.render,(blackPawn6.x, blackPawn6.y))

  	blackPawn7 = pychess.Board.Pawn('black', gameSize, 25*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn7.render,(blackPawn7.x, blackPawn7.y))

   	blackPawn8 = pychess.Board.Pawn('black', gameSize, 29*gameSize/32, 4*gameSize/32)
  	screen.blit(blackPawn8.render,(blackPawn8.x, blackPawn8.y))

  	whiteRook1 = pychess.Board.Rook('white', gameSize, 1*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteRook1.render,(whiteRook1.x, whiteRook1.y))

  	whiteKnight1 = pychess.Board.Knight('white', gameSize, 5*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteKnight1.render,(whiteKnight1.x, whiteKnight1.y))

  	whiteBishop1 = pychess.Board.Bishop('white', gameSize, 9*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteBishop1.render,(whiteBishop1.x, whiteBishop1.y))

  	whiteQueen = pychess.Board.Queen('white', gameSize, 13*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteQueen.render,(whiteQueen.x, whiteQueen.y))

  	whiteKing = pychess.Board.King('white', gameSize, 17*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteKing.render,(whiteKing.x, whiteKing.y))

  	whiteBishop2 = pychess.Board.Bishop('white', gameSize, 21*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteBishop2.render,(whiteBishop2.x, whiteBishop2.y))

  	whiteKnight2 = pychess.Board.Knight('white', gameSize, 25*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteKnight2.render,(whiteKnight2.x, whiteKnight2.y))

  	whiteRook2 = pychess.Board.Rook('white', gameSize, 29*gameSize/32, 28*gameSize/32)
  	screen.blit(whiteRook2.render,(whiteRook2.x, whiteRook2.y))

  	whitePawn1 = pychess.Board.Pawn('white', gameSize, 1*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn1.render,(whitePawn1.x, whitePawn1.y))

  	whitePawn2 = pychess.Board.Pawn('white', gameSize, 5*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn2.render,(whitePawn2.x, whitePawn2.y))

  	whitePawn3 = pychess.Board.Pawn('white', gameSize, 9*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn3.render,(whitePawn3.x, whitePawn3.y))

  	whitePawn4 = pychess.Board.Pawn('white', gameSize, 13*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn4.render,(whitePawn4.x, whitePawn4.y))

  	whitePawn5 = pychess.Board.Pawn('white', gameSize, 17*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn5.render,(whitePawn5.x, whitePawn5.y))

  	whitePawn6 = pychess.Board.Pawn('white', gameSize, 21*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn6.render,(whitePawn6.x, whitePawn6.y))

  	whitePawn7 = pychess.Board.Pawn('white', gameSize, 25*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn7.render,(whitePawn7.x, whitePawn7.y))

   	whitePawn8 = pychess.Board.Pawn('white', gameSize, 29*gameSize/32, 24*gameSize/32)
  	screen.blit(whitePawn8.render,(whitePawn8.x, whitePawn8.y))

  	while 1:
  		for event in pygame.event.get():
  			if event.type in (QUIT, KEYDOWN):
  				return
  			elif event.type == MOUSEBUTTONUP:
  				print(event.pos)

		pygame.display.update()

if __name__ == '__main__': main()