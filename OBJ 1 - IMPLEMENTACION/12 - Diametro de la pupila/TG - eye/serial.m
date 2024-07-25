clc, clear, close all;

% Open the serial port
s = serialport("COM9", 9600); % Replace "COM10" with the correct port name

try
    % Read and display data continuously
    while true
        % Read data from the serial port
        data = readline(s);
        
        % Display the received data
        disp(data);
    end
catch ME
    % Close the serial port when done
    delete(s);
    disp('Serial port closed.');
end

