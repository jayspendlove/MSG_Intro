#!/usr/bin/env python3

'''Want to import numPY somehow--PIP file'''
'''
	Author: Jay Spendlove
	Project Name: Nuclear_Decay
	email: jayclark24@gmail.com

	Project for simulating the decay fo Uramium 238 molecules by approximation of a differential
	equation.Purpose of project is for entry into Prof. Gus Hart's Material Simulation Group (MSG).

'''

class Nuclear_Decay (object):
	'''ToDo: Make ARRAYS not LIST'''
	t = []
	n_uranium= []
	'''Class includes functions:
		__init__(self, ui, i_tau, i_dt, i_s_time)
		fill_t_list()
		user_initialize()
		calculate()
		store()
	'''

	def __init__(Nuclear_Decay, ui, i_tau, i_dt, i_s_time)
		'''This function initializes all the variables specific to an instance of the Nuclear_Decay class'''
		Nuclear_Decay.t.append(0)
		Nuclear_Decay.n_uranium.append(ui)
		tau = i_tau
		dt = i_dt
		s_time = i_s_time

	def user_initialize()
		'''Function takes user input to initialize and instance of class Nuclear_Decay.
		This function is primarily for use with an 'interactive' testing or use of program'''

	def fill_t_list (dt)
		'''Once input of time step (dt), and sample time (s_time) is given, fill_t_list(t) will
		fill the list with each value of t to be tested and 'sampled'.
		''' 

	def calculate()
		'''calculate values to go into list n_uranium according to times in t. Using for loop'''
		for val in t
			Nuclear_Decay.uranium_n.append(uranium_n[val] - (uranium_n[val] / tau) * dt)

