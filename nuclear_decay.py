#!/usr/bin/env python3
import numpy as np
'''Want to import numPY somehow--PIP file
import numPy as np
'''
'''
	Author: Jay Spendlove
	Project Name: Nuclear_Decay
	email: jayclark24@gmail.com

	Project for simulating the decay fo Uramium 238 molecules by approximation of a differential
	equation.Purpose of project is for entry into Prof. Gus Hart's Material Simulation Group (MSG).

'''

class Nuclear_Decay (object):
	'''ToDo: Make ARRAYS not LIST'''
	t = np.array []
	n_uranium= np.array []
	'''Class includes functions:
		__init__(self, ui, i_tau, i_dt, i_s_time)
		fill_t_list()
		user_initialize()
		calculate()
		store()
	'''

	def __init__(Nuclear_Decay, ui, i_tau, i_dt, i_s_time)
		'''This function initializes all the variables specific to an instance of the Nuclear_Decay class
		t is an array of values to test for N(u) at
		n_uranium is an array of the values of N(u) at times specified in array t
		tau is the time constant
		dt is the time step to be tested for
		s_time is the sample time, how much time passing you want to simulate 
		'''
		Nuclear_Decay.t.append(0)
		Nuclear_Decay.n_uranium.append(ui)
		tau = i_tau
		dt = i_dt
		s_time = i_s_time

	def user_initialize()
		'''Function takes user input to initialize and instance of class Nuclear_Decay.
		This function is primarily for use with an 'interactive' testing or use of program'''

	def fill_t_list (dt, s_time)
		'''Once input of time step (dt), and sample time (s_time) is given, fill_t_list(t) will
		fill the list with each value of t to be tested and 'sampled'.
		range(start, stop, step)
		''' 
		t = [range(0, s_time, dt)]
		
	def calculate(Nuclear_Decay)
		'''calculate values to go into list n_uranium according to times in t. Using for loop'''
		for val in t
			Nuclear_Decay.uranium_n.append(uranium_n[val] - (uranium_n[val] / tau) * dt)

	def get_t(Nuclear_Decay)
	'''get elements in array t for testing purposes'''
		print(t)

	def get_n_uranium(Nuclear_Decay)
	'''get elements in array n_uranium for testing purposes'''
		print (n_uranium)
