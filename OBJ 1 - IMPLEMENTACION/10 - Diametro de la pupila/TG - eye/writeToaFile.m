% Crear un vector de datos tipo double y lo escribe en un archivo de texto.

nombre_archivo = 'datos.txt';

while true
    
datos = rand(1, 10);   
save(nombre_archivo, 'datos', '-ascii', '-double', '-tabs');
   
pause(0.5);
end
