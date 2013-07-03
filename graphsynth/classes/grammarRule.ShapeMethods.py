# ************************************************************************
# *     This grammarRule.ShapeMethods.cs file partially defines the
# *     grammarRule class (also partially defined in grammarRule.Basic.cs,
# *     grammarRule.RecognizeApply.cs and grammarRule.NegativeRecognize.cs)
# *     and is part of the GraphSynth.BaseClasses Project which is the
# *     foundation of the GraphSynth Application.
# *     GraphSynth.BaseClasses is protected and copyright under the MIT
# *     License.
# *     Copyright (c) 2011 Matthew Ira Campbell, PhD.
# *
# *     Permission is hereby granted, free of charge, to any person obtain-
# *     ing a copy of this software and associated documentation files
# *     (the "Software"), to deal in the Software without restriction, incl-
# *     uding without limitation the rights to use, copy, modify, merge,
# *     publish, distribute, sublicense, and/or sell copies of the Software,
# *     and to permit persons to whom the Software is furnished to do so,
# *     subject to the following conditions:
# *
# *     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# *     EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# *     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGE-
# *     MENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# *     FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# *     CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# *     WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# *
# *     Please find further details and contact information on GraphSynth
# *     at http://www.GraphSynth.com.
# ************************************************************************
from System import *
from System.Collections.Generic import *
from System.Linq import *
# Here is the new overload of grammarRule that includes the ability to view
# * the graph as a 2-D shape where nodes are points or vertices, and arcs are
# * lines or edges.
class grammarRule(object):
	def __init__(self):
		# <summary>
		#   this matrix determines the transform to place the first node at (0,0) and the 
		#   second node at (r,0). This is not stored in the file since it can be quickly 
		#   determined.
		# </summary>
		# <summary>
		#   Resets the regularization matrix.
		# </summary>
		# <summary>
		#   Calculates the regularization matrix.
		# </summary> # theta is 90-degrees #theta is 0-degrees
		self.__flip = transfromType.Prohibited
		self.__projection = transfromType.Prohibited
		self.__rotate = True
		self.__scale = transfromType.BothIndependent
		self.__skew = transfromType.Prohibited
		self.__translate = transfromType.BothIndependent
		self.__useShapeRestrictions = False
		self.__restrictToNodeShapeMatch = False
		self.__transformNodeShapes = True
		self.__transformNodePositions = True

	def get_RegularizationMatrix(self):
		if self.__regularizationMatrix == None:
			self.calculateRegularizationMatrix()
		return self.__regularizationMatrix

	RegularizationMatrix = property(fget=get_RegularizationMatrix)

	def ResetRegularizationMatrix(self):
		self.__regularizationMatrix = None

	def calculateRegularizationMatrix(self):
		self.__regularizationMatrix = Array.CreateInstance(Double, 3, 3)
		a = 1.0
		b = 0.0
		c = 0.0
		d = 1.0
		tauX = 0.0
		tauY = 0.0
		length = 1
		if L.nodes.Count >= 1:
			tauX = -L.nodes[0].X
			tauY = -L.nodes[0].Y
		if L.nodes.Count >= 2:
			theta = -Math.Atan2((L.nodes[1].Y - L.nodes[0].Y), (L.nodes[1].X - L.nodes[0].X))
			if MatrixMath.sameCloseZero(Math.Abs(theta), Math.PI / 2):
				a = d = 0.0
				b = -1 if (theta > 0) else 1
				c = -b
				length = Math.Abs(L.nodes[1].Y - L.nodes[0].Y)
			elif MatrixMath.sameCloseZero(theta):
				a = d = 1
				b = c = 0
				length = Math.Abs(L.nodes[1].X - L.nodes[0].X)
			else:
				a = d = Math.Cos(theta)
				length = (L.nodes[1].X - L.nodes[0].X) / a
				b = -Math.Sin(theta)
				c = -b
		self.__regularizationMatrix[0][0] = a / length
		self.__regularizationMatrix[0][1] = b / length
		self.__regularizationMatrix[0][2] = (a * tauX + b * tauY) / length
		self.__regularizationMatrix[1][0] = c / length
		self.__regularizationMatrix[1][1] = d / length
		self.__regularizationMatrix[1][2] = (c * tauX + d * tauY) / length
		self.__regularizationMatrix[2][0] = 0.0
		self.__regularizationMatrix[2][1] = 0.0
		self.__regularizationMatrix[2][2] = 1.0

	# <summary>
	#   Gets or sets a value indicating whether [use shape restrictions].
	# </summary>
	# <value>
	#   <c>true</c> if [use shape restrictions]; otherwise, <c>false</c>.
	# </value>
	def get_UseShapeRestrictions(self):
		return self.__useShapeRestrictions

	def set_UseShapeRestrictions(self, value):
		self.__useShapeRestrictions = value

	UseShapeRestrictions = property(fget=get_UseShapeRestrictions, fset=set_UseShapeRestrictions)

	# <summary>
	# Gets or sets a value indicating whether [restrict to node shape match].
	# </summary>
	# <value>
	# 	<c>true</c> if [restrict to node shape match]; otherwise, <c>false</c>.
	# </value>
	def get_RestrictToNodeShapeMatch(self):
		return self.__restrictToNodeShapeMatch

	def set_RestrictToNodeShapeMatch(self, value):
		self.__restrictToNodeShapeMatch = value

	RestrictToNodeShapeMatch = property(fget=get_RestrictToNodeShapeMatch, fset=set_RestrictToNodeShapeMatch)

	# <summary>
	# Gets or sets a value indicating whether [transform node positions].
	# </summary>
	# <value><c>true</c> if [transform node positions]; otherwise, <c>false</c>.
	# </value>
	def get_TransformNodePositions(self):
		return self.__transformNodePositions

	def set_TransformNodePositions(self, value):
		self.__transformNodePositions = value

	TransformNodePositions = property(fget=get_TransformNodePositions, fset=set_TransformNodePositions)

	# <summary>
	# Gets or sets a value indicating whether the node shapes are also transformed or simply their position.
	# </summary>
	# <value><c>true</c> if [transform node shapes]; otherwise, <c>false</c>.</value>
	def get_TransformNodeShapes(self):
		return self.__transformNodeShapes

	def set_TransformNodeShapes(self, value):
		self.__transformNodeShapes = value

	TransformNodeShapes = property(fget=get_TransformNodeShapes, fset=set_TransformNodeShapes)

	# <summary>
	#   Gets or sets the translate transformation allowance.
	# </summary>
	# <value>The translate.</value>
	def get_Translate(self):
		return self.__translate

	def set_Translate(self, value):
		self.__translate = value

	Translate = property(fget=get_Translate, fset=set_Translate)

	# <summary>
	#   Gets or sets the scale transformation allowance.
	# </summary>
	# <value>The scale.</value>
	def get_Scale(self):
		return self.__scale

	def set_Scale(self, value):
		self.__scale = value

	Scale = property(fget=get_Scale, fset=set_Scale)

	# <summary>
	#   Gets or sets the skew transformation allowance.
	# </summary>
	# <value>The skew.</value>
	def get_Skew(self):
		return self.__skew

	def set_Skew(self, value):
		self.__skew = value

	Skew = property(fget=get_Skew, fset=set_Skew)

	# <summary>
	#   Gets or sets the flip transformation allowance.
	# </summary>
	# <value>The flip.</value>
	def get_Flip(self):
		return self.__flip

	def set_Flip(self, value):
		self.__flip = value

	Flip = property(fget=get_Flip, fset=set_Flip)

	# <summary>
	#   Gets or sets a value indicating whether this <see cref = "grammarRule" /> allows a rotation transformation.
	# </summary>
	# <value><c>true</c> if rotate; otherwise, <c>false</c>.</value>
	def get_Rotate(self):
		return self.__rotate

	def set_Rotate(self, value):
		self.__rotate = value

	Rotate = property(fget=get_Rotate, fset=set_Rotate)

	# <summary>
	#   Gets or sets the projection transformation allowance.
	# </summary>
	# <value>The projection.</value>
	def get_Projection(self):
		return self.__projection

	def set_Projection(self, value):
		self.__projection = value

	Projection = property(fget=get_Projection, fset=set_Projection)

	def findTransform(self, locatedNodes):
		# if there are no nodes, simply return the identity matrix
		if locatedNodes.Count == 0:
			return MatrixMath.Identity(3)
		# Variable Set-up: This seems a little verbose, but it is necessary
		# * to ease the calculations later and to avoid compile errors.
		x2 = x3 = x4 = y2 = y3 = y4 = 0
		tx = ty = wX = wY = a = b = c = d = 0
		k1 = k2 = k3 = k4 = 0
		u3 = u4 = v3 = v4 = 0
		# This x1 and y1 are matched with the position of L.nodes[0].X and .Y,
		# * which, given the Regularization concept, is effectively at 0,0. This is
		# * what Regularization does. It's as if the first node in L is moved to zero
		# * without loss of generality, and all the other nodes are translated accord-
		# * ingly. So, u1 = v1 = 0.
		x1 = locatedNodes[0].X
		y1 = locatedNodes[0].Y
		if locatedNodes.Count >= 2:
			x2 = locatedNodes[1].X
			y2 = locatedNodes[1].Y
		# Given regularization, this second point is scaled and rotated to 1, 0.
		if locatedNodes.Count >= 3:
			x3 = locatedNodes[2].X
			y3 = locatedNodes[2].Y
			temp = Array[]((L.nodes[2].X, L.nodes[2].Y, 1.0))
			temp = MatrixMath.multiply(self.RegularizationMatrix, temp, 3)
			u3 = temp[0]
			v3 = temp[1]
		if locatedNodes.Count >= 4:
			x4 = locatedNodes[3].X
			y4 = locatedNodes[3].Y
			temp = Array[]((L.nodes[3].X, L.nodes[3].Y, 1.0))
			temp = MatrixMath.multiply(self.RegularizationMatrix, temp, 3)
			u4 = temp[0]
			v4 = temp[1]
		# set values for tx, and ty
		tx = x1
		ty = y1
		if (locatedNodes.Count <= 3) or (MatrixMath.sameCloseZero(v3 * v4)):
			wX = wY = 0
		else:
			#calculate intermediate values used only in this class or method
			#k1 = (u4 * (y4 - y2) / v4 - u3 * (y3 - y2) / v3);   //(Equation 3 of program)
			k1 = u4 * v3 * (y4 - y2) - u3 * v4 * (y3 - y2)
			if MatrixMath.sameCloseZero(k1):
				k1 = 0
			else:
				k1 /= v3 * v4
			#k2 = (y3 - y2 * u3 + ty * u3 - ty) / v3 + (-y4 - ty * u4 + y2 * u4 + ty) / v4;  //(Equation 4 of program)
			k2 = v4 * (y3 - y2 * u3 + ty * u3 - ty) + v3 * (-y4 - ty * u4 + y2 * u4 + ty)
			if MatrixMath.sameCloseZero(k2):
				k2 = 0
			else:
				k2 /= v3 * v4
			#k3 = (u3 * (x3 - x2) / v3 - u4 * (x4 - x2) / v4);
			k3 = u3 * v4 * (x3 - x2) - u4 * v3 * (x4 - x2)
			if MatrixMath.sameCloseZero(k3):
				k3 = 0
			else:
				k3 /= v3 * v4
			#k4 = (x4 - x2 * u4 + tx * u4 - tx) / v4 - (x3 + tx * u3 - x2 * u3 - tx) / v3;
			k4 = v3 * (x4 - x2 * u4 + tx * u4 - tx) - v4 * (x3 + tx * u3 - x2 * u3 - tx)
			if MatrixMath.sameCloseZero(k4):
				k4 = 0
			else:
				k4 /= v3 * v4
			#calculate wY, and wX
			wY = (k1 * k4) - (k2 * k3)
			if MatrixMath.sameCloseZero(wY):
				wY = 0
			else:
				wY /= k3 * (y3 - y4) + k1 * (x3 - x4) #(Equation 7 of program)
			wX = wY * (y3 - y4) + k2
			if MatrixMath.sameCloseZero(wX):
				wX = 0
			else:
				wX /= k1 #is (Equation 8 of program) which is rewritten for program's accuracy
		if locatedNodes.Count <= 1:
			a = d = 1
			b = c = 0
		else:
			# calculate a 
			a = x2 * (wX + 1) - tx
			#calculate c
			c = y2 * (wX + 1) - ty
			if (locatedNodes.Count <= 2) or (self.LnodesAreCollinear()):
				# in order for the validTransform to function, b and d are set as
				# * if there is a rotation as opposed to a Skew in X. It is likely that
				# * isotropic transformations like rotation are more often intended than skews.
				# var theta = Math.Atan2(-c, a);
				b = -c
				d = a
			else:
				#calculate b
				b = x3 * (wX * u3 + wY * v3 + 1) - a * u3 - tx
				if MatrixMath.sameCloseZero(b):
					b = 0
				else:
					b /= v3
				#calculate d
				d = y3 * (wX * u3 + wY * v3 + 1) - c * u3 - ty
				if MatrixMath.sameCloseZero(d):
					d = 0
				else:
					d /= v3
		T = Array.CreateInstance(Double, 3, 3)
		T[0][0] = a
		T[0][1] = b
		T[0][2] = tx
		T[1][0] = c
		T[1][1] = d
		T[1][2] = ty
		T[2][0] = wX
		T[2][1] = wY
		T[2][2] = 1
		T = MatrixMath.multiply(T, self.RegularizationMatrix, 3)
		T[0][0] /= T[2][2]
		T[0][1] /= T[2][2]
		T[0][2] /= T[2][2]
		T[1][0] /= T[2][2]
		T[1][1] /= T[2][2]
		T[1][2] /= T[2][2]
		T[2][0] /= T[2][2]
		T[2][1] /= T[2][2]
		T[2][2] = 1
		self.snapToIntValues(T)
		#if (RestrictToNodeShapeMatch && T[0,0]==1 && T[)
		return T

	def snapToIntValues(T):
		i = 0
		while i < 3:
			j = 0
			while j < 3:
				if MatrixMath.sameCloseZero(T[i][j], 1):
					T[i][j] = 1
				elif MatrixMath.sameCloseZero(T[i][j]):
					T[i][j] = 0
				elif MatrixMath.sameCloseZero(T[i][j], -1):
					T[i][j] = -1
				j += 1
			i += 1

	snapToIntValues = staticmethod(snapToIntValues)

	def LnodesAreCollinear(self):
		n1X = L.nodes[0].X
		n1Y = L.nodes[0].Y
		tNodes = List[node](L.nodes)
		tNodes.RemoveAt(0)
		if tNodes.Count > 3:
			tNodes.RemoveRange(3, tNodes.Count - 3)
		if tNodes.TrueForAll():
			return True
		if tNodes.TrueForAll():
			return True
		m1 = (tNodes[0].Y - n1Y) / (tNodes[0].X - n1X)
		tNodes.RemoveAt(0)
		return tNodes.TrueForAll()

	def validTransform(self, T):
		# In this function the candidate transform, T, "runs the gauntlet.
		# * the long set of if statements each return false, and if T makes it all
		# * the way through, we return true.
		# It's easy to check the translation and projection constraints first. Since there's
		# * a one-to-one match with variables in the matrix and the flags.
		# if Tx is not zero...
		if (not MatrixMath.sameCloseZero(T[0][2])) and ((self.Translate == transfromType.OnlyY) or (self.Translate == transfromType.Prohibited)):
			return False
		if (not MatrixMath.sameCloseZero(T[1][2])) and ((self.Translate == transfromType.OnlyX) or (self.Translate == transfromType.Prohibited)):
			return False
		if (not MatrixMath.sameCloseZero(T[0][2], T[1][2])) and (self.Translate == transfromType.BothUniform):
			return False
		# now for projection.
		if (not MatrixMath.sameCloseZero(T[2][0])) and ((self.Projection == transfromType.OnlyY) or (self.Projection == transfromType.Prohibited)):
			return False
		if (not MatrixMath.sameCloseZero(T[2][1])) and ((self.Projection == transfromType.OnlyX) or (self.Projection == transfromType.Prohibited)):
			return False
		if (not MatrixMath.sameCloseZero(T[2][0], T[2][1])) and (self.Projection == transfromType.BothUniform):
			return False
		# Now, it's a little more complicated since the rotation occupies the same cells
		# * in T as skewX, skewY, scaleX, and scaleY. The approach taken here is to solve
		# * for theta (the amount of rotation) and then call/return what the overload produces
		# * which requires theta and solves for skewX, skewY, scaleX, and scaleY.
		if not self.Rotate:
			return self.validTransform(T, 0.0)
		# Skew restrictions are easier than Scale, because they default to (as in the
		# * identity matrix) 0 whereas Scale is 1.
		if (self.Skew == transfromType.Prohibited) or (self.Skew == transfromType.OnlyY):
			return self.validTransform(T, Math.Atan2(T[0][1], T[1][1]))
		if self.Skew == transfromType.OnlyX:
			return self.validTransform(T, Math.Atan2(-T[1][0], T[0][0]))
		if self.Skew == transfromType.BothUniform:
			return self.validTransform(T, Math.Atan2((T[0][1] - T[1][0]), (T[0][0] + T[1][1])))
		# Lastly, and most challenging, we look at Scale Restrictions. Flip is basically
		# * the same and handled in the overload below.
		if (self.Scale == transfromType.Prohibited) or (self.Scale == transfromType.OnlyY):
			Too2PlusTio2 = T[0][0] * T[0][0] + T[1][0] * T[1][0]
			sqrtt2pt2 = Math.Sqrt(Too2PlusTio2)
			Ky = Math.Sqrt(Too2PlusTio2 - 1)
			return self.validTransform(T, Math.Acos(T[0][0] / sqrtt2pt2) + Math.Atan2(Ky, 1))
		if self.Scale == transfromType.OnlyY:
			Toi2PlusTii2 = T[0][1] * T[0][1] + T[1][1] * T[1][1]
			sqrtt2pt2 = Math.Sqrt(Toi2PlusTii2)
			Kx = Math.Sqrt(Toi2PlusTii2 - 1)
			return self.validTransform(T, Math.Acos(T[0][1] / sqrtt2pt2) + Math.Atan2(1, Kx))
		if self.__scale == transfromType.BothUniform:
			return self.validTransform(T, Math.Atan2((T[0][0] - T[1][1]), (T[0][1] + T[1][0])))
		return True

	def validTransform(self, T, theta):
		# now with theta known, we can find the values for Sx, Sy, Kx, and Ky.
		Kx = T[0][1] * Math.Cos(theta) - T[1][1] * Math.Sin(theta)
		Ky = T[0][0] * Math.Sin(theta) + T[1][0] * Math.Cos(theta)
		Sx = T[0][0] * Math.Cos(theta) - T[1][0] * Math.Sin(theta)
		Sy = T[0][1] * Math.Sin(theta) + T[1][1] * Math.Cos(theta)
		# now check the skew restrictions, once an error is found return false.
		if (not MatrixMath.sameCloseZero(Kx)) and ((self.Skew == transfromType.Prohibited) or (self.Skew == transfromType.OnlyY)):
			return False
		if (not MatrixMath.sameCloseZero(Ky)) and ((self.Skew == transfromType.Prohibited) or (self.Skew == transfromType.OnlyY)):
			return False
		if (not MatrixMath.sameCloseZero(Kx, Ky)) and (self.Skew == transfromType.BothUniform):
			return False
		# now we check scaling restrictions.
		if (not MatrixMath.sameCloseZero(Math.Abs(Sx), 1)) and ((self.Scale == transfromType.Prohibited) or (self.Scale == transfromType.OnlyY)):
			return False
		if (not MatrixMath.sameCloseZero(Math.Abs(Sy), 1)) and ((self.Scale == transfromType.Prohibited) or (self.Scale == transfromType.OnlyX)):
			return False
		if (not MatrixMath.sameCloseZero(Math.Abs(Sx), Math.Abs(Sy))) and (self.Scale == transfromType.BothUniform):
			return False
		# finally, we check if the shape has to be flipped.
		if (Sx < 0) and ((self.Flip == transfromType.Prohibited) or (self.Flip == transfromType.OnlyY)):
			return False
		if (Sy < 0) and ((self.Flip == transfromType.Prohibited) or (self.Flip == transfromType.OnlyX)):
			return False
		if (Sx * Sy < 0) and (self.Flip == transfromType.BothUniform):
			return False
		return True

	def otherNodesComply(self, T, locatedNodes):
		if locatedNodes.Count <= 2:
			return True
		i = 2
		while i != locatedNodes.Count:
			vLVect = Array[]((L.nodes[i].X, L.nodes[i].Y, 1.0))
			vLVect = MatrixMath.multiply(T, vLVect, 3)
			vLVect[0] /= vLVect[2]
			vLVect[1] /= vLVect[2]
			vHostVect = Array[]((locatedNodes[i].X, locatedNodes[i].Y, 1.0))
			if (not MatrixMath.sameCloseZero(vLVect[0], vHostVect[0])) or (not MatrixMath.sameCloseZero(vLVect[1], vHostVect[1])):
				return False
			i += 1
		return True

	def ReorderNodes(self):
		""" <summary>
		 Reorders the nodes for best shape transform. This is to put all NOT-exist nodes
		 at the end of the list and to avoid unlikely problems when first 3 or 4 nodes 
		 are collinear or sitting on top of each other.
		 </summary>
		"""
		# put not-exist nodes at the end of the list.
		notExistNodes = L.nodes.FindAll()
		L.nodes.RemoveAll(notExistNodes.Contains)
		# if all the nodes are collinear, there's nothing we can do.
		if (L.nodes.Count < 3) or (self.LnodesAreCollinear()):
			L.nodes.AddRange(notExistNodes)
			return 
		# take off the node with the lowest x, call it nodeMinX
		minX = L.nodes.Min()
		nodeMinX = L.nodes.Find()
		L.nodes.Remove(nodeMinX)
		# take off the node with the largest x, call it nodeMaxX
		maxX = L.nodes.Max()
		nodeMaxX = L.nodes.Find()
		L.nodes.Remove(nodeMaxX)
		# take off the node with the next lowest x, call it nodeMinXX
		minXX = L.nodes.Min()
		nodeMinXX = L.nodes.Find()
		L.nodes.Remove(nodeMinXX)
		if L.nodes.Count > 0:
			# if you have four or more nodes, find a fourth point,
			# * again at max X.
			maxXX = L.nodes.Max()
			nodeMaxXX = L.nodes.Find()
			L.nodes.Remove(nodeMaxXX)
			L.nodes.Insert(0, nodeMaxXX)
		L.nodes.Insert(0, nodeMinXX)
		L.nodes.Insert(0, nodeMaxX)
		L.nodes.Insert(0, nodeMinX)
		L.nodes.AddRange(notExistNodes)

	def TransformPositionOfNode(update, T, given):
		""" <summary>
		   Updates the position of a node.
		 </summary>
		 <param name = "update">The node to update.</param>
		 <param name = "T">The Transformation matrix, T.</param>
		 <param name = "given">The given rule node.</param>
		"""
		pt = Array[]((given.X, given.Y, 1))
		pt = MatrixMath.multiply(T, pt, 3)
		newT = MatrixMath.Identity(3)
		newT[0][2] = update.X = pt[0] / pt[2]
		newT[1][2] = update.Y = pt[1] / pt[2]
		update.DisplayShape.TransformMatrix = newT

	TransformPositionOfNode = staticmethod(TransformPositionOfNode)

	def TransfromShapeOfNode(update, T):
		""" <summary>
		 Transfroms the shape of node.
		 </summary>
		 <param name="update">The update.</param>
		 <param name="T">The T.</param>
		"""
		newT = T.Clone()
		newT[0][2] = update.X
		newT[1][2] = update.Y
		update.DisplayShape.TransformMatrix = newT

	TransfromShapeOfNode = staticmethod(TransfromShapeOfNode)