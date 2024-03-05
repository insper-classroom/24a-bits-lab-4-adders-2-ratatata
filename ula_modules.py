#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b 
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]

    half_1 = halfAdder(a, b, s[1], s[2]) 
    half_2 = halfAdder(c, s[1], soma, s[3])

    @always_comb
    def comb():
        carry.next = s[2] | s[3]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    soma.next[0] = x[0] ^ y[0] 
    carry0 = x[0] & y[0]  

    soma.next[1] = x[1] ^ y[1] ^ carry0  
    carry.next = (x[1] & y[1]) | (x[1] & carry0) | (y[1] & carry0)
    return instances()


@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
