sample = '10010001001111100110010000010100001'

def BinToDecimal(devidedsample):
    devidedsample_dec = int(devidedsample,2)
    decode = chr(devidedsample_dec)
    return decode 
    
# hacer un main que elvalúe el archivo de entrada, divida en grupos de 7 y
# evalue en la función de bintodecimal, luego guarde el decodificado en una archivo nuevo.

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




