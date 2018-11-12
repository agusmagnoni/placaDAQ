# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:27:55 2018

@author: Agus
"""

import nidaqmx
import matplotlib.pyplot as plt
import numpy as np

d_fs = 48000
d_chunk = 1000
d_device = 'Dev4'
d_channel = 'ai1'
out_channel = 'ao0'
d_gain = 1
# Modo_RSE = nidaqmx.constants.TerminalConfiguration(10083)
Modo_RSE = nidaqmx.constants.TerminalConfiguration.RSE

#print (nidaqmx.constants.TerminalConfiguration.RSE)
#print (nidaqmx.constants.TerminalConfiguration(10083))
system = nidaqmx.system.System.local()
if not system.devices:
    print ('Ojo! No se han detectado dispositivos conectados')

def listaDispositivos():
    system = nidaqmx.system.System.local()
    if system.devices:
        print(system.devices)
        for device in system.devices:
            print(device)
    else:
        print ('No se han encontrado dispositivos conectados.')
        
def adquirir1canal(gain = d_gain, device = d_device, channel = d_channel, chunk=d_chunk, fs=d_fs, terminals = Modo_RSE, plot=False):
    with nidaqmx.Task() as task:
        input_setup = task.ai_channels.add_ai_voltage_chan(device+'/'+channel,terminal_config = terminals)
        input_setup.ai_gain = gain
        task.timing.cfg_samp_clk_timing(fs)
        data = task.read(number_of_samples_per_channel=chunk)
    if plot:
        plt.plot(np.arange(chunk)/fs, data,'.-')
    return data

def write(senal, device = d_device, channel = out_channel, val_min = 0, val_max = 5):
    with nidaqmx.Task() as task:
        ao = task.ao_channels.add_ao_voltage_chan(device+'/'+channel)
        ao.ao_max = val_max
        ao.ao_min=val_min
        task.write(senal,auto_start=True)


#def muestreoVariandoFs (f_ini = 100, f_fin = d_fs, puntos = 50, plot=False):
#    # Falta verificar la frecuencia maxima del dispositivo.
#    frecuencias_sampleo = np.linspace(f_ini,f_fin,puntos)
#    frecs_medidas = []
#    k=0
#    medfrec=[]
#    for frec_sampleo in frecuencias_sampleo:
#        print(k)
#        # Es importante limitar el tiempo a travez del tamaño del chunk
#        tiempo_max = 1 # En segundos
#        chunk = 1000
#        data = adquirir1canal(chunk=chunk, fs=frec_sampleo)
#        fft = np.abs(np.fft.fft(data))
#        x = np.arange(len(data))
#        x = x * len(x)/frec_sampleo
#        k=k+1
#        medfrec.append(data)
#        if plot:
#            #plt.plot(x,fft, '.-')
#            plt.plot(np.arange(chunk)/frec_sampleo,data)
#        frecs_medidas += x[np.argmax(fft)]
#    #if plot:
#     #   plt.plot(frecuencias_sampleo,frecs_medidas, '.-')
#    return medfrec, frecuencias_sampleo, chunk
