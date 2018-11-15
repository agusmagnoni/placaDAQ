# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:22:31 2018

@author: Agus
"""

import numpy as np
import PyDAQ 
import control
import matplotlib.pyplot as plt


#%% SOLO PROPORCIONAL

setpoint = 0.1

lazo1 = control.PIDController(setpoint, kp=10.0, ki=10.0, kd=0,tau_i=10000)

for i in range(500):
    data = PyDAQ.adquirir1canal()
    medicion = np.mean(data)
    senal = lazo1.calculate(medicion)
    PyDAQ.write(senal)

plt.close("all")
lazo1.plots()

#%% GUARDAR

np.savez('proporcional_k50.npz',medicion = lazo1.medicion_t,error = lazo1.error_t, senal = lazo1.out_t, p = lazo1.p_term_t)



#%%
np.savez('PID_ruido_1_5_5.npz', medicion = lazo1.medicion_t,error = lazo1.error_t, senal = lazo1.out_t, p = lazo1.p_term_t, i = lazo1.i_term_t, d = lazo1.d_term_t)


