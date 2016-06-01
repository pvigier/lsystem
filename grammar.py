class LSystem:
	def __init__(self, axiom, rules):
		#self.alphabet
		self.axiom = axiom
		self.rules = rules
		self.state = self.axiom

	def reset(self):
		self.state = self.axiom

	def step(self):
		self.state = ''.join(self.rules.get(x, x) for x in self.state)