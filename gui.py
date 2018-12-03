#import everything
import os, pygame, chess, math
from pygame.locals import *

boardImage = 'img/chessboard.jpg'     #image of chessboard used for background
gameSize = 200

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
  #pushes the pieces from the board object onto the screen
  for x in range(8):
    for y in range(8):
      p = board.getPiece((x,y)) #get peice on square
      if p != None:
        render = getRender(p) #render an image of that piece
        screen.blit(render, squareToCoor((x,y))) #stage
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

  board = chess.Board()
  board.setupDefault()
  print(board)

  screen = renderBoard(board, screen)
  screen = renderPieces(board, screen)

  startSqr = [0,0]
  endSqr = [0,0]
  
  while 1:
      for event in pygame.event.get():
          
          #if event.type in (QUIT, KEYDOWN):
          if event.type == QUIT:
              return
          elif event.type == MOUSEBUTTONDOWN:
              print(event.pos)
              startSqr = coorToSquare(event.pos)
              print(startSqr)
          elif event.type == MOUSEBUTTONUP:
              print(event.pos)
              endSqr = coorToSquare(event.pos)
              print(endSqr)
              board.movePiece(startSqr, endSqr)

              screen = renderBoard(board, screen)
              screen = renderPieces(board, screen)

      pygame.display.update()

if __name__ == '__main__': main()