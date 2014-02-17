import numpy
class SM(object):
	def __init__(self,x):
			#Check that we were given a numpy array
			assert(isinstance(x,numpy.ndarray))
			self.x = []
			self.i = []
			self.p = [0]
			#we'll fill these in shortly
			pcount=0
			for j in xrange(x.shape[0]):
				for i in xrange(x.shape[1]):
					if x[i,j] != 0.0:
						pcount+=1
						self.i.append(i)
						self.x.append(x[i,j])
				self.p.append(pcount)
