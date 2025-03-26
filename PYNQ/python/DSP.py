# Programmer: Connor Fricke (cd.fricke23@gmail.com)
# File: DSP.py
# Latest Revision: 30-Sep-2024
# Desc: Some functions that I may or may not use for DSP testing purposes in PYNQ.

import numpy as np
from math import pi, cos, sin
import cmath

def goertzel_IIR(x: list, k: int):
    """
    Performs a filter implementation of the Goertzel algorithm for single-tone continuous
    wave detection at the specified integer k-value corresponding to frequency
        f = k*f_s/N 
    where f_s is the sampling rate and N is the length of the input signal, x.
    @@ params:
        x: list - the input signal
        k: int - the integer-valued frequency to detect using the Goertzel algorithm
    @@ return:
        (real, imag) - a complex number, X(k).
    """
    N = len(x)
    s = []
    COS = cos(2.0*pi*float(k)/float(N))
    SIN = sin(2.0*pi*float(k)/float(N))
    
    drs0 = 0.0
    drs1 = 0.0
    drs2 = 0.0
    
    for n in range(N):
        drs0 = x[n] + (2*COS*drs1) - drs2 
        s.append(drs0)
        drs2 = drs1
        drs1 = drs0
    
    s_N = (2*COS*s[N-1]) - s[N-2]
    
    real = s_N - (COS*s[N-1])
    imag = SIN * s[N-1]
    return complex(real, imag)

def decimate(x: list, dec_factor: int):
    """
    Returns a decimated version of an input signal based on a decimation factor.
    i.e. the new signal will contain one of every dec_factor samples of the input signal.
    @@ params:
        x: list - the input signal to be decimated
        dec_factor: int - the factor to decimate the input signal by.
    @@ return:
        output: list - a list of values corresponding to the decimated signal.
    """
    output = []
    for i in range(len(x)):
        if i % dec_factor == 0:
            output.append(x[i])
    return output
        
        