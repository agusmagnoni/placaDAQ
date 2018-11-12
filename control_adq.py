# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:22:31 2018

@author: Agus
"""

import numpy as np
import PyDAQ 
import control
import matplotlib.pyplot as plt

setpoint = 0.1


#%% SOLO PROPORCIONAL

lazo1 = control.PIDController(setpoint, kp=5.0, ki=2.0, kd=5.0,tau_i=10000)

for i in range(200):
    data = PyDAQ.adquirir1canal()
    medicion = np.mean(data)
    senal = lazo1.calculate(medicion)
    PyDAQ.write(senal)

plt.close("all")
lazo1.plots()

#%% GUARDAR

np.savez('proporcional_k50.npz',medicion = lazo1.medicion_t,error = lazo1.error_t, senal = lazo1.out_t, p = lazo1.p_term_t)



#%%
np.savez('PID_5_2_2.npz', medicion = lazo1.medicion_t,error = lazo1.error_t, senal = lazo1.out_t, p = lazo1.p_term_t, i = lazo1.i_term_t, d = lazo1.d_term_t)

