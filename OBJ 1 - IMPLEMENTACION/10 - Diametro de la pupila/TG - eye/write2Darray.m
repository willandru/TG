
frecuencia = 100; % Frecuencia de la onda en Hz
duracion = 1;     % Duración de la señal en segundos
fs = 1000;        % Frecuencia de muestreo en Hz

% Generar el vector de tiempo
t = linspace(0, duracion, duracion*fs);

% Generar la señal sinusoidal
amplitud = 1; % Amplitud de la onda
fase = 0;     % Fase inicial de la onda
signalX = amplitud * sin(2 * pi * frecuencia * t + fase);

% Definir el nombre del archivo de texto
nombre_archivo = 'datos.txt';

% Combinar datos de tiempo y señal en una matriz
datos = [t' signalX'];

% Escribir los datos en el archivo de texto
dlmwrite(nombre_archivo, datos, 'delimiter', '\t', 'precision', 3);
