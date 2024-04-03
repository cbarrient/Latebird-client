import esptool

command = ['--port','COM4', 'erase_flash']
esptool.main(command)

command = ['--port','COM4', '--baud', '1000000', 'write_flash', '-fs', '4MB', '0', 'firmware.bin']
esptool.main(command)