#!/usr/bin/env python3

from nuclear_decay import Nuclear_Decay

test = Nuclear_Decay()

test.__init__(20, 1, .5, 5)
'''initial uranium, tau, dt, sample time'''
test.fill_t_array(.5, 5)
'''dt, s_time'''

test.get_t()

test.calculate()

test.get_n_uranium()
