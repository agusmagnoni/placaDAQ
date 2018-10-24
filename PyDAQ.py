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
d_device = 'Dev1'
d_channel = 'ai0'
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

def muestreoVariandoFs (f_ini = 100, f_fin = d_fs*1000, puntos = 1000, plot=False):
    # Falta verificar la frecuencia maxima del dispositivo.
    frecuencias_sampleo = np.logspace(f_ini,f_fin,puntos)
    frecs_medidas = []
    for frec_sampleo in frecuencias_sampleo:
        # Es importante limitar el tiempo a travez del tamaño del chunk
        tiempo_max = 1 # En segundos
        chunk = min(1000,tiempo_max*frec_sampleo)
        data = adquirir1canal(chunk=chunk, fs=frec_sampleo)
        fft = np.abs(np.fft.fft(data))
        x = np.array(len(data))
        x = x * len(x)/frec_sampleo
        if plot:
            plt.plot(x,t, '.-')
        frecs_medidas += x[np.argmax(fft)]
    if plot:
        plt.plot(frecuencias_sampleo,frecs_medidas, '.-')
        