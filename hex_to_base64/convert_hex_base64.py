# To convert hex to base64

def convert(hex_string):
  base64_string = hex_string.decode('hex').encode('base64')
  return base64_string

string = raw_input("Enter the string to be converted: ")
print convert(string)


