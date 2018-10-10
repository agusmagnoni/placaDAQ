# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:27:55 2018

@author: Agus
"""

import numpy as no
import nidaqmx

"""" Creo que con esto podemos ver el nombre que le pone al device""""
#import nidaqmx.system
system = nidaqmx.system.System.local()
for device in system.devices:
    print(device)


"""" leer el voltaje de uno de los inputs analógicos de la placa (ai0). 
OJO CON: Dev1 creo que es el nombre del device. Quizás esto tiene que salir de lo que nos tire previamente cuando pedimos el nombre del device.""""

with nidaqmx.Task() as task:
...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
...     task.read()
