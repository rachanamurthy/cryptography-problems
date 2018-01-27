# Perform XOR of two hex strings

def HexToRaw(string):
  return string.decode('hex')

def RawToHex(string):
  return string.encode('hex')

def sxor(string1,string2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return RawToHex(''.join(chr(ord(a) ^ ord(b)) for a,b in zip(string1,string2)))

string1 = raw_input("Enter first string: ")
string2 = raw_input("Enter second string: ")

print sxor(HexToRaw(string1), HexToRaw(string2))