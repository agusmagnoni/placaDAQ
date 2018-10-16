# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:23:52 2018

@author: Agus
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Frecuencias.
""" Para las frecuencias me parece que va a haber que mostrar los gráficos uno por uno más que hacer un ploteo de frecuencia medida en función de frecuencia enviada. Porque no es sencillo obtener la frecuencia cuando la señal se va al demonio""""

data = np.load('barridofrec.npz')
datos = data['datos'].tolist()
datos2 = data['datos2'].tolist()
frec1 = [0.5, 1, 5, 8, 10, 15, 20, 25, 30, 35, 40]#esto está en kHz
frec2 = [0.5, 1, 5, 10, 15, 20, 25, 30, 35, 40, 45]#esto está en kHz.

#%%
t = np.arange(len(datos[0]))
#
#from scipy.optimize import curve_fit
#f = lambda t, amp, fase, frec, off : amp*np.sin(t*frec+fase)+off
#def f(t,amp,fase,frec,off):
#    return np.sin(t*frec+fase)*amp+off

#popt, pcov= curve_fit(f,t,np.asarray(datos[0]),p0=[10, 0, 500,0]) #uso el vector de varianzas calculado previame

import scipy.signal as sp
frec = np.zeros(len(datos))
for i in range(len(datos)):
    peaks = sp.find_peaks_cwt(datos[i],np.arange(1,50))
    frec[i] = 1/(np.mean(peaks[1:]-peaks[:-1])/48000)
