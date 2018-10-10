# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:27:55 2018

@author: Agus
"""

import numpy as np
import nidaqmx
import matplotlib.pyplot as plt


#import nidaqmx.system
system = nidaqmx.system.System.local()
for device in system.devices:
    print(device)

#%%Resolución
#Mientras mandamos una rampa muy lenta
#ai0 y ai1 son los dos inputs analógicos del DAQ
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai1")
    #task.start()
    print(task.timing.ai_conv_max_rate)
    task.timing.cfg_samp_clk_timing(48000) # seteo la frecuencia de muestre
    data = task.read(number_of_samples_per_channel=1000)
    #print(data)
    plt.plot(data,'.-')

#%% frecuencia
from scipy.optimize import curve_fit  
import time
fs=20000  
t = np.linspace(0,1000/fs,num=1000)
f = lambda t, amp, frec, fase, off: amp*np.sin(frec*t+fase) + off

frecs=np.array([1000,5000,10000,15000,20000,30000,40000,50000,60000,70000])

#%%
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai1")
    #task.start()
    task.timing.cfg_samp_clk_timing(30000) # seteo la frecuencia de muestreo
    data = task.read(number_of_samples_per_channel=1000)
    #print(data)
    plt.plot(data,'.-')
#%%  

datos2.append(data)
    
    