import esptool

port = input("Which serial port is your board connected to? (COM3 or COM4) ")

command = ['--port', port, 'erase_flash']
esptool.main(command)

command = ['--port', port, '--baud', '1000000', 'write_flash', '-fs', '4MB', '0', 'firmware.bin']
esptool.main(command)