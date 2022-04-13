HEX_FILTER = ''.join([(len(repr(chr(c))) == 3) and chr(c) or '.' for c in range(256)])

def hexdump(src, length=16):
    if isinstance(src, bytes):
        src = src.decode()
    result = []
    for i in range(0, len(src), length):
        word = src[i:length+i]
        print(word)
        printable = word.translate(HEX_FILTER)
        hexa = " ".join([f'{ord(c):02x}' for c in word])
        hexlength = 16 * 3
        result.append(f'{i:04x} {hexa:<{hexlength}} {printable}')
    
    if len(result) > 0:
        for line in result:
            print(line)
    else:
        print("No input")

hexdump("Hello there   .   . not me")


