from grammar import *
from plot import *

# Grammar

def algae():
	system = LSystem('A', {'A': 'AB', 'B': 'A'})
	for _ in range(8):
		print(system.state)
		system.step()

# 2D plots

def koch():
	system = LSystem('F', {'F': 'F+F-F-F+F'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 90)

def tree():
	system = LSystem('B', {'B': 'F/[+B]-B*'})
	for _ in range(7):
		system.step()
	plot2d(system.state, 20, 2, np.array([0, 1.]), 'g')

def plant():
	system = LSystem('X', {'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 25, 1, rotate(np.array([1., 0]), 50), 'g')

def liana():
	system = LSystem('F', {'F': 'F[+F]F[-F]F'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 25, 1, np.array([0, 1.]), 'g')

# 3D plots

def tree3d():
	system = LSystem('B', {'B': 'F/[+B][-B][&B]^B*'})
	for _ in range(6):
		system.step()
	plot3d(system.state, 20, 1.2, np.array([0, 0, 1.]), 'g')

def pine3d():
	system = LSystem('B', {'B': 'F/[+++B][---B][&&&B][^^^B]*F/[++B][--B][&&B][^^B]*F/B*'})
	for _ in range(4):
		system.step()
	plot3d(system.state, 20, 2, np.array([0, 0, 1.]), 'g')

if __name__ == '__main__':
	pine3d()