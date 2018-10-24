# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:35:31 2018

@author: Agus
"""

import numpy as np
import nidaqmx
import matplotlib.pyplot as plt
import PyDAQ_test as daq


#import nidaqmx.system
print("Nombre del dispositivo")
system = nidaqmx.system.System.local()
for device in system.devices:
    print(device)
    #device.reset_device()#si quiero resetear los settings del chabon este

#%% 
    
with nidaqmx.Task() as task:
    ao = task.ao_channels.add_ao_voltage_chan("Dev3/ao0")
    ao.ao_max = 5
    ao.ao_min=0
    data = [2]*100
    task.write(data,auto_start=True)


data = daq.adquirir1canal(plot=True)


#%% Lazo de control
RefValue = 0.02
gain = 1
senhal = 2
while True:
    with nidaqmx.Task() as task:
        ao = task.ao_channels.add_ao_voltage_chan("Dev3/ao0")
        ao.ao_max = 5
        ao.ao_min=0
        data = [senhal]*100
        task.write(data,auto_start=True)
    data = daq.adquirir1canal()
    value = np.mean(data)
    delta = RefValue - value
    senhal = senhal + delta*gain
    print(senhal)
    print(value)



















