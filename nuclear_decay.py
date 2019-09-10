#!/usr/bin/env python

'''
	Author: Jay Spendlove
	Project Name: Nuclear_Decay
	email: jayclark24@gmail.com

	Project for simulating the decay fo Uramium 238 molecules by approximation of a differential
	equation.Purpose of project is for entry into Prof. Gus Hart's Material Simulation Group (MSG).

'''

class Nuclear_Decay (object):
	'''Class includes functions:
		initialize()
		fill_t_list()
		user_initialize()
		calculate()
		store()
	'''

	def fill_t_list (dt)
		'''Once input of time step (dt), and sample time (s_time) is given, fill_t_list(t) will
		fill the list with each value of t to be tested and 'sampled'.
		''' 
