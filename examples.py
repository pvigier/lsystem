from grammar import *
from tortoise2d import *

def algae():
	system = LSystem('A', {'A': 'AB', 'B': 'A'})
	for _ in range(8):
		print(system.state)
		system.step()

def koch():
	system = LSystem('F', {'F': 'F+F-F-F+F'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 90)

def tree():
	system = LSystem('B', {'B': 'F/[+B]-B*'})
	for _ in range(7):
		system.step()
	plot2d(system.state, 20, 2, 90, 'g')

def plant():
	system = LSystem('X', {'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 25, 1, 50, 'g')

def liana():
	system = LSystem('F', {'F': 'F[+F]F[-F]F'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 25, 1, 90, 'g')

if __name__ == '__main__':
	tree()