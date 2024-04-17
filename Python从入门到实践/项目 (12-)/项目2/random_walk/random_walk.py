from random import choice

class RandomWalk:
	# Generate random walk data
	def __init__(self,num_points=5000):
		self.num_points=num_points

		# All randomwalk data starts at (0,0)
		self.x_values=[0]
		self.y_values=[0]
		
	def fill_walk(self):
	# Calculate all randomwalk dots
		# Walk until reaching given length
		while len(self.x_values)<self.num_points:

			x_step=self._get_step()

			y_step=self._get_step()

			# Make sure every step goes ahead
			if x_step==0 and y_step==0:
				continue

			# Calculate the next x and y
			x=self.x_values[-1]+x_step
			y=self.y_values[-1]+y_step

			# Append the next step into the list
			self.x_values.append(x)
			self.y_values.append(y)

	def _get_step(self):
		direction=choice([1,-1])
		distance=choice([0,1,2,3,4,5,6,7,8])
		return direction*distance
