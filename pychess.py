import os, pygame
from pygame.locals import *


#Game Parameters
boardImage = 'img/chessboard.jpg'     #image of chessboard used for background
whiteKingImage = 'img/whiteKing.png'
whiteQueenImage = 'img/whiteQueen.png'
whiteRookImage = 'img/whiteRook.png'
whiteBishopImage = 'img/whiteBishop.png'
whiteKnightImage = 'img/whiteKnight.png'
whitePawnImage = 'img/whitePawn.png'
blackKingImage = 'img/blackking.png'
blackQueenImage = 'img/blackQueen.png'
blackRookImage = 'img/blackRook.png'
blackBishopImage = 'img/blackBishop.png' 
blackKnightImage = 'img/blackKnight.png'
blackPawnImage = 'img/blackPawn.png'

class Board:
    def __init__(self, gSize):
        self.render = pygame.image.load(boardImage).convert()
        self.render = pygame.transform.scale(self.render, (gSize, gSize))

        self.gameSize = gSize

        

        # self.squares = [[square(none) for y in range(8)] for x in range(8)]
        
        # a1 = square('a1', blackKnight1)
        # a2 = square('a2', none)

        # board.getSquare(x,y)

    # def getSquare(x, y):

    #     return square

    # class Square:
    #     __init__(self, name, piece):
    #         self.piece = piece
    #         self.name = name

    #     def isEmpty():
    #         if self.piece = none:
    #             return true

    #     def getPiece():
    #         if isEmpty() == false:
    #             return self.piece
        
    # def getSquare(x,y):
    #     return square

    class Pawn:
        def __init__(self, color, gSize, x, y):
            if color == 'black':
                self.render = pygame.image.load(blackPawnImage).convert_alpha() #load correct pic from file
            else:
                self.render = pygame.image.load(whitePawnImage).convert_alpha()
            
            self.render = pygame.transform.scale(self.render, (gSize/16, 2*gSize/16)) #scales dimensions of peice
            
            self.x = x  #set location on board
            self.y = y

    class Rook:
        def __init__(self, color, gSize, x, y):
            if color == 'black':
                self.render = pygame.image.load(blackRookImage).convert_alpha() #load correct pic from file
            else:
                self.render = pygame.image.load(whiteRookImage).convert_alpha()
            
            self.render = pygame.transform.scale(self.render, (gSize/16, 2*gSize/16)) #scales dimensions of peice
            
            self.x = x  #set location on board
            self.y = y

    class Knight:
        def __init__(self, color, gSize, x, y):
            if color == 'black':
                self.render = pygame.image.load(blackKnightImage).convert_alpha() #load correct pic from file
            else:
                self.render = pygame.image.load(whiteKnightImage).convert_alpha()
            
            self.render = pygame.transform.scale(self.render, (gSize/16, 2*gSize/16)) #scales dimensions of peice
            
            self.x = x  #set location on board
            self.y = y

    class Bishop:
        def __init__(self, color, gSize, x, y):
            if color == 'black':
                self.render = pygame.image.load(blackBishopImage).convert_alpha() #load correct pic from file
            else:
                self.render = pygame.image.load(whiteBishopImage).convert_alpha()
            
            self.render = pygame.transform.scale(self.render, (gSize/16, 2*gSize/16)) #scales dimensions of peice
            
            self.x = x  #set location on board
            self.y = y

    class King:
        def __init__(self, color, gSize, x, y):
            if color == 'black':
                self.render = pygame.image.load(blackKingImage).convert_alpha() #load correct pic from file
            else:
                self.render = pygame.image.load(whiteKingImage).convert_alpha()
            
            self.render = pygame.transform.scale(self.render, (gSize/16, 2*gSize/16)) #scales dimensions of peice
            
            self.x = x  #set location on board
            self.y = y

    class Queen:
        def __init__(self, color, gSize, x, y):
            if color == 'black':
                self.render = pygame.image.load(blackQueenImage).convert_alpha() #load correct pic from file
            else:
                self.render = pygame.image.load(whiteQueenImage).convert_alpha()
            
            self.render = pygame.transform.scale(self.render, (gSize/16, 2*gSize/16)) #scales dimensions of peice
            
            self.x = x  #set location on board
            self.y = y
