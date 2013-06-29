# ************************************************************************
# *     This file includes MatrixMath functions and is part of the
# *     GraphSynth.BaseClasses Project which is the foundation of the
# *     GraphSynth Application.
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
# *     Similar functions have been created in a more involved matrix library
# *     written by the author known as StarMath (http://starmath.codeplex.com/).
# *     Please find further details and contact information on GraphSynth
# *     at http://www.GraphSynth.com.
# ************************************************************************
from System import *

class MatrixMath(object):
	def __init__(self):
		# <summary>
		#   This is used below in the close enough to zero booleans to match points
		#   (see below: sameCloseZero). In order to avoid strange round-off issues - 
		#   even with doubles - I have implemented this function when comparing the
		#   position of points (mostly in checking for a valid transformation (see
		#   ValidTransformation) and if other nodes comply (see otherNodesComply).
		# </summary>
		self._epsilon = 0.000001

	def sameCloseZero(x1):
		return Math.Abs(x1) < self._epsilon

	sameCloseZero = staticmethod(sameCloseZero)

	def sameCloseZero(x1, x2):
		return MatrixMath.sameCloseZero(x1 - x2)

	sameCloseZero = staticmethod(sameCloseZero)

	def Identity(size):
		identity = Array.CreateInstance(Double, size, size)
		i = 0
		while i < size:
			identity[i][i] = 1.0
			i += 1
		return identity

	Identity = staticmethod(Identity)

	def multiply(A, x, size):
		b = Array.CreateInstance(Double, size)
		m = 0
		while m != size:
			b[m] = 0.0
			n = 0
			while n != size:
				b[m] += A[m][n] * x[n]
				n += 1
			m += 1
		return b

	multiply = staticmethod(multiply)

	def multiply(A, B, size):
		C = Array.CreateInstance(Double, size, size)
		m = 0
		while m != size:
			n = 0
			while n != size:
				C[m][n] = 0.0
				p = 0
				while p != size:
					C[m][n] += A[m][p] * B[p][n]
					p += 1
				n += 1
			m += 1
		return C

	multiply = staticmethod(multiply)