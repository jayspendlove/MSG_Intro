#!/usr/bin/env python3
#import numpy as np
from nuclear_decay import Nuclear_Decay

test = Nuclear_Decay(20, 1, 0.5, 10)
'''initial uranium, tau, dt, sample time'''
test.check_array_size()
test.check_object_values()
print(test.calculate())
'''Dividing by 2 every time? At least something is being returned!'''


