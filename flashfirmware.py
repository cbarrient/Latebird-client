import esptool

port = input("Which serial port is your board connected to? Please type the full name, e.g. COM3 ")

command = ['--port', port, 'erase_flash']
esptool.main(command)

command = ['--port', port, '--baud', '1000000', 'write_flash', '-fs', '4MB', '0', 'firmware.bin']
esptool.main(command)