import pygame

Master_Rect = pygame.Rect((0,0), (50, 50))

class Coordinates(object):
	pass
	#def __init__(self, x, y, ):
		

class Object_Base(object):
	pass
	#def __init__(self, ):



class Square(object):
	square_rect = pygame.Rect((0, 0), (50, 50))
	current_id = 0
	def __init__(self, SquareId=None):
		self.square_id = self.current_id
		self.incrementId()
	@classmethod
	def changeSize (sizetuple):
		Square.square_rect = pygame.Rect((0,0), sizetuple)

	def incrementId(self):
		Square.current_id += 1

Master_Square = Square()


class SquareFactory(object):
	array_of_squares = []
	def __init__(self, Template=Master_Square, ChangedSquareSize=None, ):
		SquareFactory.array_of_squares.append(pygame.Surface( (Template.square_rect.x, Template.square_rect.y)))

	def addASquare(self, Size):
		SquareFactory.array_of_squares.append(pygame.Surface((Square.square_rect.x, Square.square_rect.y)))




	def printCurrentLocations():
		pass

	

class CircleFactory(object):
	pass


class ShapeFactory(object):
	def __init__(self, ):
		pass
