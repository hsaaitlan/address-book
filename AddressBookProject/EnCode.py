def en_code(data): 
    encodedata = {'a': "00100", 'A': "01100", 'b': "00200", 'B': "01200", 'c': "00300",
                  'C': "01300", 'd': "00400", 'D': "01400", 'e': "00500", 'E': "01500",
                  'f': "00600", 'F': "01600", 'g': "00700", 'G': "01700", 'h': "00800",
                  'H': "01800", 'i': "00900", 'I': "01900", 'j': "001'0", 'J': "011'0",
                  'k': "002'0", 'K': "012'0", 'l': "003'0", 'L': "013'0", 'm': "004'0",
                  'M': "014'0", 'n': "005'0", 'N': "015'0", 'o': "006'0", 'O': "016'0",
                  'p': "007'0", 'P': "017'0", 'q': "008'0", 'Q': "018'0", 'r': "009'0",
                  'R': "019'0", 's': "001''", 'S': "011''", 't': "002''", 'T': "012''",
                  'u': "003''", 'U': "013''", 'v': "004''", 'V': "014''", 'w': "005''",
                  'W': "015''", 'x': "006''", 'X': "016''", 'y': "007''", 'Y': "017''",
                  'z': "008''", 'Z': "018''", ' ': "00000", '!': "00001", '@': "00002",
                  '#': "00003", '%': "00004", '$': "00005", '^': "00007", '&': "00008",
                  '*': "00049", '(': "00009", ')': "00010", '-': "00011", '_': "00012",
                  '+': "00013", '=': "00014", '1': "00015", '2': "00016", '3': "00017",
                  '4': "00018", '5': "00019", '6': "00020", '7': "00021", '8': "00022",
                  '9': "00023", '0': "00024", '{': "00025", '[': "00026", '}': "00027",
                  ']': "00028", '|': "00029", ':': "00030", ';': "00031", '"': "00032",
                  "'": "00033", '<': "00034", ',': "00035", '>': "00036", '.': "00037",
                  '?': "00038", '/': "00039", '`': "00040", '~': "00041"}
    length = len(data)
    s = ''
    for i in range(0, length): 
        s = s+str(encodedata[data[i]])
    return s
