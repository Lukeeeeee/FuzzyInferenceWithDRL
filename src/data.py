
class Data:

	def __init__(self, initalizer):
		self.data_count = initalizer.parameters['data_count']
		self.bacth_data_count = initalizer.parameters['bacth_data_count']
		self.sample_size = initalizer.parameters['sample_size']
		self.file = None


	def return_trian_bacth_data(self):
		pass
	def return_test_data(self):
		pass
	def return_dev_data(self):
		pass

