# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo para analizar la caracterización de la placa DAQ.

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
#%% Relación entre la señal enviada y lo que mide la DAQ. 

### cargo los datos yo:
amp_enviada = np.array([0.5, 1,2,3,4,5,6,7,8,9]) # Volts pico a pico
amp_medida_ch1 = np.array([0.5027,1.004,1.99,2.99,3.99,4.98,5.99,6.98,7.98,8.98])
amp_medida_ch2 = np.array([0.502,0.99,2.00,3.00,4.00,5.00,6.01,6.99,8.02,9.01])

##
my_dpi = 96
plt.figure(1,figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
sns.set_context("poster", font_scale=1, rc={"lines.linewidth": 3})
sns.set_style("ticks") 
ax=plt.subplot(111)
ax.plot(amp_enviada,amp_medida_ch1,'.-',markersize=20)
ax.plot(amp_enviada,amp_medida_ch2,'.-',markersize=20)
ax.grid(True)  
ax.set_xlabel('Amplitud enviada (Vpp)')
ax.set_ylabel('Amplitud medida (Vpp)')
plt.tight_layout()
sns.set()

#%% Resolución LOAD
"""Acá medimos una rampa lenta (1 Hz) para ver el paso que tiene la placa, discreto."""

#levanto el archivo .txt que se llama resolucion
BASE_PATH = "/home/usuario/Documentos/Instrumentacion/Placa DAQ/MedicionesYDatos/Caracterizaciones viejas DAQ" # directorio en el que mirar

volt_res = np.loadtxt(os.path.join(BASE_PATH,'resolucion.txt'))

#%% RESOLUCIÓN
## figura para guardar y mostrar la medicion
my_dpi = 96
plt.figure(2,figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 1})
sns.set_style("ticks") 
ax=plt.subplot(111)
ax.plot(volt_res,'.-',markersize=10)
ax.grid(True)  
ax.set_xlabel('# muestra')
ax.set_ylabel('Voltaje (V)')
plt.tight_layout()
sns.set()

# busco la mínima resolución.

diff = np.diff(volt_res) #hago la resta de los elementos
diff = diff[diff!=0] #saco las que son cero
## veo que es 0.0025

#%% FRECUENCIA LOAD


data = np.load('barrido_frec2410.npz')

data_medida = data['medfrec'].tolist()
frecuencias_sampleo = data['frecuencias_sampleo'].tolist()

#%% 

for i in range(50):
    np.savetxt('frec'+str(i)+'.txt',data_medida[i])

#lo llevo a matlab porque acá el peak finder me cuesta bastante.
#%% RAMPA
    
rampa2 = np.load('rampa_2ch.npz')
rampa1A = np.load('rampa_1ch_samefs.npz')
rampa1B = np.load('rampa_1ch_fs.npz')

data2=rampa2['data'].tolist()
data1a=rampa1A['data'].tolist()
data1b=rampa1B['data'].tolist()


my_dpi = 96
plt.figure(3,figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 3})
sns.set_style("ticks") 
ax=plt.subplot(111)
plt.plot(np.arange(1000)/20000, data2[0],'.-',markersize=15)
plt.plot(np.arange(1000)/20000,data2[1],'.-',markersize=15)
ax.grid(True)  
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Voltaje (V)')
plt.tight_layout()
sns.set()

#fitteo con una recta ambas.
from scipy.optimize import curve_fit

fun = lambda t, a, b: a*t+b 
popt1, pcov1= curve_fit(fun,np.arange(8)/20000,data2[0][232:240],p0=None) #uso el vector de varianzas calculado previamente.
popt2, pcov2= curve_fit(fun,np.arange(8)/20000,data2[1][232:240],p0=None)

my_dpi = 96
plt.figure(4,figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
sns.set_context("paper", font_scale=1.5, rc={"lines.linewidth": 3})
sns.set_style("ticks")
sns.set_palette("tab20") 
ax=plt.subplot(111)
plt.plot(np.arange(8)/20000, data2[0][232:240],'.',markersize=20)
plt.plot(np.arange(8)/20000,data2[1][232:240],'.',markersize=20)
plt.plot(np.arange(8)/20000,fun(np.arange(8)/20000,popt1[0],popt1[1]),'-')
plt.plot(np.arange(8)/20000,fun(np.arange(8)/20000,popt2[0],popt2[1]),'-')
ax.grid(True)  
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Voltaje (V)')
plt.tight_layout()
sns.set()


deltax=-popt1[1]/popt1[0]+popt2[1]/popt2[0]
error_deltax = np.sqrt((1/popt1[0])**2*pcov1[1,1]+(popt1[1]/popt1[0]**2)**2*pcov1[0,0]+(1/popt2[0])**2*pcov2[1,1]+(popt2[1]/popt2[0]**2)**2*pcov2[0,0])