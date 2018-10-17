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


#%% Frecuencia: A MANO MUY CACUIJA. 
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai1")
    #task.start()
    task.timing.cfg_samp_clk_timing(30000) # seteo la frecuencia de muestreo
    data = task.read(number_of_samples_per_channel=1000)
    #print(data)
    plt.plot(data,'.-')
    
#%%  

datos2.append(data)

#%% Medir con varios canales. HAY QUE PENSAR QUE SEÑAL LE MANDAMOS PARA QUE SE VEA LA DIFERENCIA. 

samples = 1000
data = np.zeros([2,samples]) #row: channel / column: sample
with nidaqmx.Task() as task:
    task.in_stream.channels_to_read("Dev1/ai1","Dev1/ai0") #como catso llamo a los canales?
    nidaqmx.stream_readers.AnalogMultiChannelReader.read_many_sample(data,number_of_samples_per_channel=samples) #esta función va llenando el numpy array con las mediciones. En las filas el channel, en las columnas las mediciones: una por sample. 

































    
    