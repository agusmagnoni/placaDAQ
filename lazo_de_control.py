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
    ao = task.ao_channels.add_ao_voltage_chan("Dev5/ao0")
    ao.ao_max = 5
    ao.ao_min=0
    data = [0]*100
    task.write(data,auto_start=True)


data = daq.adquirir1canal(plot=True)


#%% Lazo de control - básico
RefValue = 0.002
gain = 10
senhal = 2
while True:
    with nidaqmx.Task() as task:
        ao = task.ao_channels.add_ao_voltage_chan("Dev5/ao0")
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

#%% Barrido in - out

Vins = np.linspace(0,5,num = 100)
Vouts = np.zeros(len(Vins))
for Vin , i in zip(Vins,range(len(Vins))):
    with nidaqmx.Task() as task:
        ao = task.ao_channels.add_ao_voltage_chan("Dev5/ao0")
        ao.ao_max = 5
        ao.ao_min=0
        task.write(Vin,auto_start=True)
    data = daq.adquirir1canal()
    Vouts[i] = np.mean(data)
    plt.plot(Vin, Vouts[i],'bo',markersize = 10)
    plt.grid(True)
    plt.xlabel('Vin')
    plt.ylabel('Vout')
    
#%% Lazo de control con ploteos y cosas. 
plt.close("all")
    
def lazoControlSimple(medicion,ref,senhal,gain=1,informe=False):
    delta = medicion - ref
    correccion = - delta * gain
    if informe:
        return senhal + correccion, delta, correccion
    return senhal + correccion
    
RefValue = 0.008 #valor en el que queremos que se mantenga el voltaje. Elijo según barridoin_out.
gain = 5 # esto me define que tan rápido voy a corregir. 
senal_t=[]#lo que mando al LED
value_t=[]#lo que mido del fotodetector
error_t=[]
correccion_t=[]
senhal = 2 # voltaje inicial que mando al LED. Levemente por debajo que RefValue.

for i in range(1000):
    with nidaqmx.Task() as task:
        ao = task.ao_channels.add_ao_voltage_chan("Dev5/ao0")
        ao.ao_max = 5
        ao.ao_min=0
        task.write(senhal,auto_start=True)
    data = daq.adquirir1canal()
    value = np.mean(data)
    senhal, delta, correccion = lazoControlSimple(value,RefValue,senhal,gain=gain, informe=True)
    print('RefValue:',RefValue,'Value:',value)
    senal_t.append(senhal)
    value_t.append(value)
    error_t.append(delta)
    correccion_t.append(correccion)
    
f,ax = plt.subplots(nrows = 3,sharex = True)    
f.text(0.5,0.04,"Iteración",ha='center')
ax[0].plot(value_t,'.-',markersize = 10)
ax[0].set_ylabel("Value")
ax[0].grid(True)
ax[1].plot(error_t,'.-',markersize = 10)
ax[1].set_ylabel("Error")
ax[1].grid(True)
ax[2].plot(correccion_t,'.-',markersize = 10)    
ax[2].set_ylabel("Corrección")
ax[2].grid(True)    
    
    
#%% Barrido ganancia
from scipy.optimize import curve_fit
from tqdm import tqdm
fun = lambda t, A, T, B: A*np.exp(-t/T)+B
 
plt.close("all")
tau_g=[]
error_g=[]
varerror_g=[]
    
def lazoControlSimple(medicion,ref,senhal,gain=1,informe=False):
    delta = medicion - ref
    correccion = - delta * gain
    if informe:
        return senhal + correccion, delta, correccion
    return senhal + correccion

gains=np.linspace(1,100)

for gain in tqdm(gains):
    
    RefValue = 0.008 #valor en el que queremos que se mantenga el voltaje. Elijo según barridoin_out.
    senal_t=[]#lo que mando al LED
    value_t=[]#lo que mido del fotodetector
    error_t=[]
    correccion_t=[]
    senhal = 2 # voltaje inicial que mando al LED. Levemente por debajo que RefValue.
    it=100
    for i in range(it):
        with nidaqmx.Task() as task:
            ao = task.ao_channels.add_ao_voltage_chan("Dev5/ao0")
            ao.ao_max = 5
            ao.ao_min=0
            task.write(senhal,auto_start=True)
        data = daq.adquirir1canal()
        value = np.mean(data)
        senhal, delta, correccion = lazoControlSimple(value,RefValue,senhal,gain=gain, informe=True)
        #print('RefValue:',RefValue,'Value:',value)
        senal_t.append(senhal)
        value_t.append(value)
        error_t.append(delta)
        correccion_t.append(correccion)
    
    popt, pcov= curve_fit(fun,np.arange(it),error_t,p0=None) #uso el vector de varianzas calculado previamente.
    tau_g.append(popt[1])
    error_g.append(popt[2])
    varerror_g.append(np.std(error_t[-int(len(error_t)/5):]))
      
f,ax = plt.subplots(nrows = 3,sharex = True)    
f.text(0.5,0.04,"Gain",ha='center')
ax[0].plot(gains,tau_g,'.-',markersize = 10)
ax[0].set_ylabel("tau")
ax[0].grid(True)
#ax[0].set_xscale('log')
ax[1].plot(gains,error_g,'.-',markersize = 10)
ax[1].set_ylabel("Error final")
ax[1].grid(True)
#ax[1].set_xscale('log')
ax[2].plot(gains,varerror_g,'.-',markersize = 10)    
ax[2].set_ylabel("Varianza del error")
ax[2].grid(True)    
#ax[2].set_xscale('log')        

np.savez('barrido_gain5.npz',gains=gains,tau_g=tau_g,error_g=error_g,varerror_g=varerror_g)    
    
    

















