#Author: Bryan Connelly
#9/3/2015

import Queue

class myQueue:
	def __init__(self):
		self.q = Queue.Queue()
	def addItem(self, item):
		if(type(item) == int):
			self.q.put(item)

	def dequeue(self):
		print(self.q.get_nowait())


class Stack:
	def __init__(self):
		self.data = []

	def push(self, integer):
		if(type(integer) == int):
			self.data.append(integer)
		else:
			print("Only integers can be added to the stack")

	def pop(self):
		print(self.data.pop())

	def checkSize(self):
		print('The stack contains ' + str(len(self.data)) + ' items')

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

class BinaryTree:
	def __init__(self, root):
		self.root = root

	def add(self, value, parentValue):
		#search the tree for the parent value
		def addRec(self, value, parentValue, startingNode):
			#if we made it past a leaf to a None, stop
			if(startingNode == None):
				return
			#if we're at the correct node...
			if(startingNode.value == parentValue):
				#try to add it as a left child
				if(startingNode.left is None):
					startingNode.left = Node(value)
					startingNode.parent = startingNode
				#otherwise try to add it as a right child
				elif(startingNode.left is not None and startingNode.right is None):
					startingNode.right = Node(value)
					startingNode.parent = startingNode
					#print('Added right child ' + str(startingNode.right.value))
				#if neither are possible, print a message
				else:
					print('Parent has two children, node not added')
			#If we still aren't at the right node, traverse the tree
			else:
				#helper function that recurses through the tree until the 
				#parent is found
				addRec(self, value, parentValue, startingNode.left)
				addRec(self, value, parentValue, startingNode.right)
		addRec(self, value, parentValue, self.root)

	def delete(self, value):
		def deleteRec(self, value, node):
			#make sure we're not past a leaf at a None
			if(node is None):
				return
			if(node.left != None and node.left.value == value):
				node.left = None
				#let automatic garbage collection clean up the orphaned node
			elif(node.right != None and node.right.value == value):
				node.right = None
			#If we're not at the right node, recurse
			else:
				deleteRec(self, value, node.left)
				deleteRec(self, value, node.right)
		deleteRec(self, value, self.root)


	def printTree(self):
		#do a pre-order traversal and print the values
		def printTreeRec(self, node):
			print(node.value)
			if(node.left is not None):	
				printTreeRec(self, node.left)
			if(node.right is not None):
				printTreeRec(self, node.right)
		printTreeRec(self, self.root)

class Graph:
	def __init__(self):
		self.verticies = {}

	def addVertex(self, value):
		if(value not in self.verticies):
			self.verticies[value] = []
		else:
			print('Vertex already exists')
	def addEdge(self, value1, value2):
		if(value1 in self.verticies and value2 in self.verticies):
			self.verticies[value1].append(value2)
		else:
			print('One or more verticies not found')
	def findVertex(self, value):
		if(value in self.verticies):
			print('Edge from ' + str(value) + ' to ' + str(self.verticies[value]))

class Test:
	def __init__(self):
		self.q = myQueue()
		self.s = Stack()
		self.t = BinaryTree(Node(10))
		self.g = Graph()

	def testQ(self):
		print('----------Testing Queue----------')

		for num in range(1, 11):
			self.q.addItem(num)
			print('added item ' + str(num))

		for num in range(1, 11):
			self.q.dequeue()
		print('\n')

	def testS(self):
		print('----------Testing Stack----------')

		for num in range(1, 11):
			print('pushed item ' + str(num))
			self.s.push(num)

		for num in range(1, 11):
			self.s.pop()

	def testT(self):
		print('----------Testing Tree----------')

		self.t.add(1, 10)
		self.t.add(5, 10)
		self.t.add(3, 1)
		self.t.add(8, 1)
		self.t.add(9, 5)
		self.t.add(2, 5)
		self.t.add(12, 3)
		self.t.add(18, 3)
		self.t.add(11, 8)
		self.t.add(16, 8)
		#makes this tree:
		#          10
		#      /        \
		#     1          5
		#   /   \      /   \
		#  3     8    9     2
		# / \   / \ 
		#12 18 11 16
		print('Tree before deletions:')
		self.t.printTree()

		self.t.delete(12)
		self.t.delete(11)
		self.t.delete(16)

		print('Tree after deletions:')
		self.t.printTree()

	def testG(self):
		print('----------Testing Graph----------')

		for num in range(1, 11):
			self.g.addVertex(num)

		self.g.addEdge(1, 2)
		self.g.addEdge(3, 2)
		self.g.addEdge(1, 6)
		self.g.addEdge(4, 7)
		self.g.addEdge(5, 5)
		self.g.addEdge(8, 1)
		self.g.addEdge(2, 5)
		self.g.addEdge(2, 8)
		self.g.addEdge(3, 1)
		self.g.addEdge(4, 3)
		self.g.addEdge(5, 6)
		self.g.addEdge(6, 2)
		self.g.addEdge(6, 3)
		self.g.addEdge(6, 7)
		self.g.addEdge(7, 7)
		self.g.addEdge(7, 1)
		self.g.addEdge(7, 2)
		self.g.addEdge(8, 3)
		self.g.addEdge(8, 5)
		self.g.addEdge(8, 4)

		self.g.findVertex(1)
		self.g.findVertex(3)
		self.g.findVertex(5)
		self.g.findVertex(7)
		self.g.findVertex(8)



def main():
	tester = Test()
	tester.testQ()
	tester.testS()
	tester.testT()
	tester.testG()


if __name__ == "__main__":
    main()