import os
sample = '10010001001111100110010000010100001'

# Decode binary to string
def BinToDecimal(devidedsample):
    devidedsample_dec = int(devidedsample, 2)
    decode = chr(devidedsample_dec)
    return decode

# Reads binary from a file
def ReadFile(filename):
    archivo = open(filename, mode='r')
    texto = archivo.read()
    archivo.close()
    # Podemos mostrar en pantalla el archivo que se acaba de cargar
    print(texto)
    return texto

# writes decoded message to a file
def WriteFile(filename, datos):
    file = open(filename, "w")
    file.write(datos)
    file.close()

# Calls the other functions
def __main__():
    sample = ReadFile('C:/Users/felip/Documents/2s2021/Ingeniería de comunicaciones/Proyecto/ProyectoComunicaciones/Message.txt')
    contador = 0
    devidedsample = ''
    decodesample = ''
    for i in sample:
        devidedsample += i
        contador += 1
        if(contador == 7):
            decodesample += BinToDecimal(devidedsample)
            contador = 0
            devidedsample = ''
    print(decodesample)
     
    WriteFile('C:/Users/felip/Documents/2s2021/Ingeniería de comunicaciones/Proyecto/ProyectoComunicaciones/DecodeMessage.txt', decodesample)



__main__()