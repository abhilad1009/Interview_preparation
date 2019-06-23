"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?

"""
d = {'a': 62, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
     'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51,
     '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '.': 0, '/': 0}
rv = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
      6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 
      27: 'Z', 28: 'Y', 29: 'X', 30: 'W', 31: 'V', 32: 'U', 33: 'T', 34: 'S', 35: 'R', 36: 'Q', 37: 'P', 38: 'O', 39: 'N', 40: 'M', 41: 'L', 42: 'K', 43: 'J', 44: 'I', 45: 'H', 46: 'G', 47: 'F', 48: 'E', 49: 'D', 50: 'C', 51: 'B', 52: 'A', 
      53: '0', 54: '1', 55: '2', 56: '3', 57: '4', 58: '5', 59: '6', 60: '7', 61: '8', 0: '9' }

SHT={}
RST={}

def shorten(url):
    URL=url
    short=""
    pad=len(url)%6
    if pad!=0:
        url=url+'0'*(6-pad)
    jmp=len(url)//6
    i=0
    while i!=len(url):
        tmp=url[i:i+jmp]
        hs=0
        for k in tmp:
            hs+=d[k]
        hs=hs%62
        short+=rv[hs]
        i+=jmp
    SHT[URL]=short
    RST[short]=URL
    return short

def restore(short):
    try:
        return RST[short]
    except:
        return None

