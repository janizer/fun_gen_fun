#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:25:21 2017

@author: maclean
"""

import numpy
numpy.set_printoptions(threshold='nan')
import math

x = numpy.linspace(0,2*numpy.pi, 400)
sinearr = numpy.sin(x)+1
#'{:f}'.format(sinearr)
print  (sinearr)