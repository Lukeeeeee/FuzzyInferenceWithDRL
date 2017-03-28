from __future__ import print_function
import numpy as np


class Initializer:


	def __init__(self):
		self.set_parameters(input_nn_parameters)

	def set_parameters(self, input_nn_parameters):
		self._parameters = {}
		self._parameters['learning_rate'] = 0.03
		self._parameters['epoch'] = 1000
		self._parameters['batch_size'] = 200
		self._parameters['data_size'] = np.array()
		for index, key in enumerate(input_nn_parameters):
			self._parameters['index'] = key

	@property
	def parameters(self):
		return self._parameters
	@parameters.setter
	def parameters(self, new_parameters):
		self.parameters = new_parameters