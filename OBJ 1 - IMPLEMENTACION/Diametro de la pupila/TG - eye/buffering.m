clc, clear, close all;

rng('default');

% Create a memory-mapped file
m = memmapfile('mybinary.bin','Writable',true,'Format','double');

% Open the file outside the loop
fileID = fopen('mybinary.bin','w');

% Initialize the number
numero = 0;

while true
    % Increment the number by 1 in each iteration
    numero = numero + rand ;
    
    % Convert the number to int8
    signalX = double(numero);

     fseek(fileID, 0, 'bof');
    % Write data to the file
    fwrite(fileID, signalX, 'double');

    disp(signalX);
    
    % Pause to control the data streaming rate
    pause(0.1);
end

% Close the file
fclose(fileID);
