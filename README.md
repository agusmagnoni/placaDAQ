# placaDAQ #

En este repo vamos a ir subiendo los codigos y avances en el desarrollo de la caracterizacion y uso de una placa DAQ 

# Proximos objetivos #

## Codigos: ##

### Hacer el codigo (y testearlo) para poder generar señales. ###
Estado: Sin empezar. 
Expectativas: Va a depender mucho de poder testearlo en el labo con la placa
Relevancia: Baja.
Prioridad: Alta.

### Hacer el codigo para automatizar la medicion de problemas de sample-rate ###
Estado: Sin empezar.
Expectativas: Deberia ser sencillo y corto a partir de lo que ya hay andando.
Relevancia: Baja.
Prioridad: Alta.

### Hacer codigo para poder medir en forma continua ###
Estado: Sin empezar.
Expectativas: Deberia ser importante para lo que sigue. No es obvio que sea facil de implementar y hay que poder testearlo en la placa.
Relavancia: Alta
Prioridad: Media.

### Pasar en limpio los codigos que ya hay ###
Estado: Hecho.
Expectativas: Deberia ser corto, pero esta bueno tener las funciones moduladas y faciles de llamar.
Relevancia: Media
Prioridad: Alta.

## Mediciones: ## 

### Barrido automatico de frecuencuas ###
Descripcion: Hacer un codigo que barra en frecuencias y vea el problema de muestreo cuando las frecuencia de adquisicion se acerca a la que se desea medir. Se puede hacer generando con un generador externo y variar la de muestreo. Es la opcion mas facil y compatible con el desarrollo actual del soft. Si tuvieramos andando la generacion y la frecuencia de muestreo fuese diferente de la de generacion podriamos variar ambas y ver que onda.

Estado: Para la version simple hay codigo para hacerlo solo hay que agregar el loop. Hecho el codigo.
Expectativa: Tiene sentido hacer la version simple y dejar lo otro eventualmente para mas adelante.
Relevancia: Media
Prioridad: Media.

### Medir Rampa ###
Descripcion: Generando una rampa de variacion lenta y mediendola con el digitalizador, y asumiendo que el voltaje medido es bien preciso podemos determinar como es de regularel sampleo de la placa y mas importante cuando se mide en varios canales como es la distribucion interna de tiempos entre canales (si equidista los canales o mide todos al inicio del tiempo correspondiente).

Estado: Esta la idea y suponemos que otro grupo lo hizo.
Expectativas: Se deberia medir muy rapido, sino no tendria mucho sentido perder tiempo en eso por ahora.
Relevancia: Media.
Prioridad: Media.

### Caracterizacion de la generacion de señales ###

Descripcion: Queremos tener caracterizada la generacion de señales. Mas alla del codigo para hacerlo y las especificaciones queremos saber los limites y caracteristicas que efectivamente tiene la placa.

Estado: Sin iniciar, sin tener claro como comunicarnos con la placa.
Expectativas: Deberia ser un punto central poder generar señales confiables. No esta claro cuanto tiempo nos va a llevar leer y entender la documentacion ni cuantos problemas experimentales podremos tener. Asumimos que a partir del apredizaje que tuvimos en el proceso de digitalizacion deberia ser mas facil.
Relevancia: Alta
Prioridad. Alta.

### Testear implementacion de medicion continua ###
Descripcion: Tenemos que ver que lo que escribamos para implementar mediciones continuas funciones. 

Estado: Sin empezar, necesita el codigo.
Expectativas: No tenemos idea si va a ser un minuto o no ver que ande. Por ahora podriamos arreglarnoslas sin esto pero para una etapa posterior de aplicacion de algun tipo de lazo de control parece muy necesario.
Relevancia: Media/Alta
Prioridad: Baja

### Testear fotoreceptores/termocuplas u otro tipo de sensores ###
Descripcion: El proximo paso es empezar a interactuar con sensores y actuadores. Para eso una vez que elijamos el tipo de sensores/actuadores a utilizar necesitamos tenerlos minimamente caracterizados en cuanto a sensibilidad y cosas por el estilo. 

Estado: Sin empezar, esperando a definir cual usar.
Expectativas: Si llegamos a tener las mediciones anteriores y definimos el tipo de sensor a utilizar estaria bueno arrancar con esto. No necesitaria mucho mas soft que el que ya tenemos, pero no esprioridad.
Relevancia: Alta.
Prioridad: Baja.

## Sensores y Actuadores opciones: ##

### Termico ###

Se podria armar un sistema de regulacion termico. Con algo tipo termocupla y una resistencia.

Ventajas: Es sencillo, es todo electrico, no hay traduccion de señales mas alla de las que ya vienen intrisicas en los elementos. Es facil medir con otros instrumentos para calibrar.

Desventajas: No parece haber mucha mas aplicacion que hacer un sistema de regulacion de temperatura. Hay que manipular elementos eventualmente muy calientes.

### Luminico ###

Se podria usar un fotosensor y una lampara variable para hacer un sistema de control.

Ventajas: Son elementos mas o menos sencillos de conseguir. Se puede implementar fuera del labo quizas con la placa de sonido. Una vez que tengamos el sistema regulado podemos sobre eso montar un sistema de transmision de señales y trabajar en el tema de la relacion señal ruido para la etapa siguiente de mediciones. 

Desventajas: Probablemente una lampara requiera mas electronica complementaria para darle tension, etc.