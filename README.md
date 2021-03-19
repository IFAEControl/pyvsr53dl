# pyvsr53dl Thyracont's VSR53DL lib


Library to communicate with Thyracont's VSR53DL over RS485 using an USB to RS485 adapter. 

This library has been implemented by IFAE (www.ifae.es) control software department.

It implements most of the commands available for the device using Thyracont's Communication package protocol.
Given methods allow from retrieving all info about the device (model, version etc) to gathering the pressure measurements in real time.
Only the Relay Control Setting commands are pending although its status can be retrieved and its setting methods might be available in the future.


