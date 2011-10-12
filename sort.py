class Node:
	def __init__(self):
		self.children = []
	
	def add_child(self, child):
		self.children.append(child)
	
	def __str__(self):
		ret = ""
		for child in self.children:
			ret += str(child) + " "
		ret += "\n"
		return ret
	
	def __repr__(self):
		return self.__str__()

def create_tree(v):
	global tree 
	tree = [Node() for i in range(len(v))]


def main():
	v = [1, 2, 3, 4]
	create_tree(v)

if __name__ == "__main__":
	main()