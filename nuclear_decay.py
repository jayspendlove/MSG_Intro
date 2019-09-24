#!/usr/bin/env python3
import numpy as np

'''
	Author: Jay Spendlove
	Project Name: Nuclear_Decay
	email: jayclark24@gmail.com

	Project for simulating the decay fo Uramium 238 molecules by approximation of a differential
	equation. Purpose of project is for entry into Prof. Gus Hart's Material Simulation Group (MSG).
    
    TODO:
        figure out matplotlib
        commit to git
        look at giordano and make sure computation is correct
'''

class Nuclear_Decay (object):
    t = np.array ([])
    n_uranium= np.array ([])
    index = np.array([])
    tau =0
    dt=0
    s_time=0
    '''Class includes functions:
        __init__(self, ui, i_tau, i_dt, i_s_time)
        fill_t_array()
        user_initialize()
        calculate()
        store() -- not yet
        '''
        
    '''**********************INITIALIZING***************************************************'''
    def __init__(Nuclear_Decay, ui, i_tau, i_dt, i_s_time):
        '''This function initializes all the variables specific to an instance of the Nuclear_Decay class
        t is an array of values to test for N(u) at
        n_uranium is an array of the values of N(u) at times specified in array t
        tau is the time constant
        dt is the time step to be tested for
        s_time is the sample time, how much time passing you want to simulate 
        ui is the initial amount of uranium
        '''
        print("running...")
        Nuclear_Decay.tau = i_tau
        Nuclear_Decay.dt = i_dt
        Nuclear_Decay.s_time = i_s_time
        Nuclear_Decay.fill_t_array()
        Nuclear_Decay.fill_n_uranium_with_zeros()
        Nuclear_Decay.fill_index_array()
        Nuclear_Decay.n_uranium[0] = ui

    def user_initialize():
        '''Function takes user input to initialize and instance of class Nuclear_Decay.
        This function is primarily for use with an 'interactive' testing or use of program'''
        
    def fill_n_uranium_with_zeros(Nuclear_Decay):
        '''compute number of elements in array (s_time * dt) and fill the array n_uranium with that 
        many elements, with each element being 0. This allows calculate to update the values of n_uranium
        without requiring the creating of a new array each time a value is added.
        '''
        num = Nuclear_Decay.s_time / Nuclear_Decay.dt + 1
        num = int(num)
        print(num)
        Nuclear_Decay.n_uranium = np.zeros((num))
        

    def fill_t_array (Nuclear_Decay):
        '''Once input of time step (dt), and sample time (s_time) is given, fill_t_list() will
        fill the list with each value of t to be tested and 'sampled', up to AND INCLUDING s_time. 
        To incude the end value, dt is added to  the 'stop' value, parameter of the arange function.
        arange(start, stop, step)
        ''' 
        Nuclear_Decay.t = np.arange(0, Nuclear_Decay.s_time + Nuclear_Decay.dt, Nuclear_Decay.dt)
        
    def fill_index_array (Nuclear_Decay):
        '''fill array with values from 0 to the size of array n_uranium. For help with for loop in calculate function'''
        num = int(Nuclear_Decay.s_time / Nuclear_Decay.dt + 1)
        Nuclear_Decay.index = np.arange(0, num, 1)
        
     
    def calculate(Nuclear_Decay):
        '''calculate values to go into list n_uranium according to times in t. Using for loop'''
        for val, i in zip(Nuclear_Decay.n_uranium, Nuclear_Decay.index):
            if (i < (Nuclear_Decay.index.size - 1)):
                Nuclear_Decay.n_uranium[i+1] = val - (val/Nuclear_Decay.tau)*Nuclear_Decay.dt
        return Nuclear_Decay.n_uranium
       
    '''******************TESTING********************************************************'''
    def check_array_size(Nuclear_Decay):
        '''print the size of each  array used. For testing and development purposes'''
        print("N_Uranium array size:", Nuclear_Decay.n_uranium.size)
        print("t array size:", Nuclear_Decay.t.size )
        print("index array size: ", Nuclear_Decay.index.size)
        
    def check_object_values(Nuclear_Decay):
        '''Print value of each global variable used. For testing and development purposes'''
        print("Tau: ", Nuclear_Decay.tau)
        print("dt: ", Nuclear_Decay.dt)
        print("s_time: ", Nuclear_Decay.s_time)
        print("n_uranium: ")
        Nuclear_Decay.get_n_uranium()
        print("t: ")
        Nuclear_Decay.get_t()
        print("index: ")
        Nuclear_Decay.get_index()
        
    def get_t(Nuclear_Decay):
        '''get elements in array t for testing purposes'''
        print(Nuclear_Decay.t)

    def get_n_uranium(Nuclear_Decay):
        '''get elements in array n_uranium for testing purposes'''
        print (Nuclear_Decay.n_uranium)
        
    def get_index(Nuclear_Decay):
        '''get elements in array index'''
        print(Nuclear_Decay.index)
