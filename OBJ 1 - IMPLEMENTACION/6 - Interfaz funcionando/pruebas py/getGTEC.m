%% gtec
clc, clear all, close all
A=@gUSBampScaling;
B=@gUSBampInternalSignalGenerator;
C=@gUSBampDeviceConfiguration;
D=@gUSBampChannels;
E=@gNautilusScaling;
F=@gNautilusDeviceConfiguration;
G=@gNautilusChannels;
H=@gHIampScaling;
I=@gHIampInternalSignalGenerator;
J=@gHIampDeviceConfiguration;
K=@gHIampChannels;

display(A())
display(B())
display(C())
display(D())
display(E())
display(F())
display(G())
display(H())
display(I())
display(J())
display(K())

