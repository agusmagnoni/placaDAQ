# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:27:55 2018

@author: Agus
"""

import numpy as np
import nidaqmx
import matplotlib.pyplot as plt


#import nidaqmx.system
print("Nombre del dispositivo")
system = nidaqmx.system.System.local()
for device in system.devices:
    print(device)
    #device.reset_device()#si quiero resetear los settings del chabon este

# Pasado
    
#%%Resolución
#Mientras mandamos una rampa muy lenta
#ai0 y ai1 son los dos inputs analógicos del DAQ
fs = 48000
samples = 1000
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev2/ai1")
    #task.start()
    print(task.timing.ai_conv_max_rate)
    task.timing.cfg_samp_clk_timing(fs) # seteo la frecuencia de muestre
    data = task.read(number_of_samples_per_channel=samples)
    #print(data)
    plt.plot(np.arange(samples)/fs, data,'.-')


#%% Frecuencia: A MANO MUY CACUIJA. 
nidaqmx.constants.TerminalConfiguration(10083)
with nidaqmx.Task() as task:
    a = task.ai_channels.add_ai_voltage_chan("Dev3/ai0")
    a.ai_gain = 1
    #task.start()
    task.timing.cfg_samp_clk_timing(20000) # seteo la frecuencia de muestreo
    data = task.read(number_of_samples_per_channel=1000)
    #print(data)
    plt.plot(np.arange(1000)/20000,data,'.-')
    
#%%  

datos2.append(data)

#%% Medir con varios canales. HAY QUE PENSAR QUE SEÑAL LE MANDAMOS PARA QUE SE VEA LA DIFERENCIA. 
fs = 20000
samples = 1000


with nidaqmx.Task() as task:
    ai0 = task.ai_channels.add_ai_voltage_chan("Dev3/ai0",terminal_config = nidaqmx.constants.TerminalConfiguration(10083))
    ai0.ai_gain=1
    ai1 = task.ai_channels.add_ai_voltage_chan("Dev3/ai1",terminal_config = nidaqmx.constants.TerminalConfiguration(10083))
    ai1.ai_gain=1
    #task.start()
    task.timing.cfg_samp_clk_timing(fs) # seteo la frecuencia de muestreo
    data = task.read(number_of_samples_per_channel=samples)
    #print(data)
    plt.plot(np.arange(samples)/fs, data[0],'.-')
    plt.plot(np.arange(samples)/fs, data[1],'.-')

## voy a medir la amplitud máxima para ver que tan 1 es la ganancia 1 y tener esto caracterizado para un sensor.
    
import scipy.signal as sp
peaks = sp.find_peaks_cwt(data[0],np.arange(1,50))
d = np.asarray(data[0])
plt.plot(peaks/fs,d[peaks],'o-')
peaks2 = sp.find_peaks_cwt(data[1],np.arange(1,50))
dd = np.asarray(data[1])
plt.plot(peaks2/fs,dd[peaks2],'o-')


#%%
ampp=np.mean(d[peaks])
ampp2=np.mean(dd[peaks2])
print(ampp)
print(ampp2)
amp.append(ampp)
amp2.append(ampp2)



#%% Medir con varios canales. HAY QUE PENSAR QUE SEÑAL LE MANDAMOS PARA QUE SE VEA LA DIFERENCIA. 
fs = 48000
samples = 1000
plt.close('all')
with nidaqmx.Task() as task:
    #ai0 = task.ai_channels.add_ai_voltage_chan("Dev3/ai0",terminal_config = nidaqmx.constants.TerminalConfiguration(10083))
    #ai0.ai_gain=1
    ai1 = task.ai_channels.add_ai_voltage_chan("Dev3/ai1",terminal_config = nidaqmx.constants.TerminalConfiguration(10083))
    ai1.ai_gain=1
    #task.start()
    task.timing.cfg_samp_clk_timing(fs) # seteo la frecuencia de muestreo
    data = task.read(number_of_samples_per_channel=samples)
    #print(data)
    plt.plot(np.arange(samples)/fs, data,'.-')
    #plt.plot(np.arange(samples)/fs, data[1],'.-')



#%% read and write

##with nidaqmx.Task() as task:
#    ao = task.ao_channels.add_ao_voltage_chan("Dev3/ao0")
#    ao.ao_max = 5
#    ao.ao_min=0
#    #ao.ao_output_type(nidaqmx.constants.AOPowerUpOutputBehavior(10322)) #voltage output
#    #ai0 = task.ai_channels.add_ai_voltage_chan("Dev3/ai0",terminal_config = nidaqmx.constants.TerminalConfiguration(10083))
#    #fs=
#    #t=np.arange(long*fs)
#    #amp*np.sin(2*np.pi*frec*t/self.fs)
#    data = [0]*1000 + [1]*1000 + [2]*1000
#    task.write(data)
#
#    task.start()
#    task.stop()


#with nidaq

task = nidaqmx.Task()
ao = task.ao_channels.add_ao_voltage_chan("Dev3/ao0")
ao.ao_max = 5
ao.ao_min=0
#ao.ao_output_type(nidaqmx.constants.AOPowerUpOutputBehavior(10322)) #voltage output
#ai0 = task.ai_channels.add_ai_voltage_chan("Dev3/ai0",terminal_config = nidaqmx.constants.TerminalConfiguration(10083))
#fs=
#t=np.arange(long*fs)
#amp*np.sin(2*np.pi*frec*t/self.fs)
data = [0]*1000 + [1]*1000 + [2]*1000
task.write(data)
task.start()
















    
    