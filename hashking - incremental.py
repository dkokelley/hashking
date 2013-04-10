#Hashking#

# Required:
# # Python 3.2 (32 bit)
# # Skein module (Currently only works with 32 bit version of Python 3.2)

import skein
import random

bestguess = ""
bestscore = 1024 # Replace with current best score before running so that only better scores are printed
target = "5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4fdf9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87f4757be023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24b567aa3e2390a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6"

# Function inputs two hex values as strings, and returns the bit differential
def hexdiff(hex1, hex2):
  try:
    return bin(int(hex1, 16)^int(hex2, 16)).count('1') # This is the number of different bits in the hash
  except:
    print("hexdiff inputs must be valid hex strings")
  
seednum = 123467891544 + random.random()
  
while True:
  testvalue = str(seednum).encode('utf-8')
  test = skein.skein1024(init=testvalue, digest_bits=1024)
  score = hexdiff(test.hexdigest(), target)
  if score < bestscore:
    bestguess = testvalue
    bestscore = score
    print(bestguess, score)
  seednum += 1
