import numpy as np

from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from FunctionTree import *
from Production import *

class Question(object):

	"""
	
	Exercise parameters

	"""
	input_method = "MathKeyboard"

	"""

	Initialize the exercise (generate a function)

	"""

	def __init__(self):
		self.arg = arg
		self.tree = FunctionTree.buildTreeWithMaxComplexity(7)
		self.func =  self.tree.getOutputFunction() 
		print "Derivative : " 
		#print self.tree.getOutputDerivative()
		self.deriv =  self.tree.getOutputDerivative() 

	"""

	getPrompt() returns the text of the question in HTML.

	"""

	def getPrompt(self):
		prompt = "<p>Differentiate this function : </p><br>"
		self.tree.printTree()
		prompt += "<script type=\"math/tex; mode=display\">" + self.func.getDisplayLatex() + "</script>"
		prompt += "<p>Solution : </p><br>"
		prompt += self.deriv.toString()
		prompt += "<script type=\"math/tex; mode=display\">" + self.deriv.getDisplayLatex() + "</script>"
		return prompt

	"""

	getAnswer() evaluates the student's answer and returns "correct" or hints.

	"""

	def getAnswer(self, studentInput):
		# print("The output function is: ")
		# print(func.toString())		
		# print("The value of the output function for x = 5 is: ")
		# print(func.evaluate(5))
		# print("Which is approximately: " )
		# print(N(func.evaluate(5)))
		return "Correct!"