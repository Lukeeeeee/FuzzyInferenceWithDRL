from __future__ import print_function

import model
import initializer
#import model

if __name__ == '__main__':
	init = initializer.Initializer()
	m = model.Model(0, init)
	print(m.get_hyperparameters())
	init.parameters = 100
	m.set_hyperparameters(init)
	print(m.get_hyperparameters())

 
