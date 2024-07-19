clc, clear, close all;
% Definir la ruta y nombre del archivo
file_path = 'shared_memory.bin';

% Definir parámetros de la simulación
samplingFreq = 1000; % Frecuencia de muestreo (Hz)
duration = 10; % Duración total de la simulación (segundos)
numSamples = samplingFreq * duration; % Número total de muestras
samplePeriod = 1 / samplingFreq; % Período de muestreo

% Crear un objeto de memoria mapeada
memMapFile = memmapfile(file_path, 'Writable', true, 'Format', 'double');

% Iniciar la simulación en bucle
while true
    % Simular las lecturas del sensor (por ejemplo, una onda sinusoidal)
    t = (0:samplePeriod:duration-samplePeriod)'; % Vector de tiempo
    sensorData = sin(2*pi*5*t) + randn(size(t)); % Simular la señal del sensor (onda sinusoidal con ruido)

    % Normalizar los datos para que estén en el rango [-1, 1]
    sensorData = sensorData / max(abs(sensorData));

    % Escribir los datos en la memoria mapeada
    memMapFile.Data = sensorData;

    % Pausa para simular la adquisición en tiempo real (ajusta según sea necesario)
    pause(samplePeriod);
end
