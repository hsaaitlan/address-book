def de_code(data): 
    decodedata = {"00100": 'a', "01100": 'A', "00200": 'b', "01200": 'B', "00300": 'c',
                  "01300": 'C', "00400": 'd', "01400": 'D', "00500": 'e', "01500": 'E',
                  "00600": 'f', "01600": 'F', "00700": 'g', "01700": 'G', "00800": 'h',
                  "01800": 'H', "00900": 'i', "01900": 'I', "001'0": 'j', "011'0": 'J',
                  "002'0": 'k', "012'0": 'K', "003'0": 'l', "013'0": 'L', "004'0": 'm',
                  "014'0": 'M', "005'0": 'n', "015'0": 'N', "006'0": 'o', "016'0": 'O',
                  "007'0": 'p', "017'0": 'P', "008'0": 'q', "018'0": 'Q', "009'0": 'r',
                  "019'0": 'R', "001''": "s", "011''": "S", "002''": "t", "012''": "T",
                  "003''": 'u', "013''": 'U', "004''": 'v', "014''": 'V', "005''": 'w',
                  "015''": 'W', "006''": 'x', "016''": 'X', "007''": 'y', "017''": 'Y',
                  "008''": 'z', "018''": 'Z', "00000": ' ', "00001": '!', "00002": '@',
                  "00003": '#', "00004": '%', "00005": '$', "00007": '^', "00008": '&',
                  "00049": '*', "00009": '(', "00010": ')', "00011": '-', "00012": '_',
                  "00013": '+', "00014": '=', "00015": '1', "00016": '2', "00017": '3',
                  "00018": '4', "00019": '5', "00020": '6', "00021": '7', "00022": '8',
                  "00023": '9', "00024": '0', "00025": '{', "00026": '[', "00027": '}',
                  "00028": ']', "00029": '|', "00030": ':', "00031": ';', "00032": '"',
                  "00033": "'", "00034": '<', "00035": ',', "00036": '>', "00037": '.',
                  "00038": '?', "00039": '/', "00040": '`', "00041": '~'}
    data = str(data)
    length = int(len(data)/5)
    s = ''
    for i in range(0, length): 
        la = ''
        for j in range(5*i, 5*i+5): 
            la = la+data[j]
        s = s+decodedata[la]
    return s
