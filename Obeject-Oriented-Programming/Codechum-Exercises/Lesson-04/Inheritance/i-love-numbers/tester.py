from decimalNumber import DecimalNumber
from number import Number
from wholeNumber import WholeNumber

wn1 = WholeNumber(3)
wn2 = WholeNumber(4)
print(wn1)  # 3
wn1.multiply(wn2)
print(wn1)  # 12

# Testing DecimalNumber class
dn1 = DecimalNumber(1234, 2)
dn2 = DecimalNumber(5678, 2)
print(dn1)  # 12.34
dn1.multiply(dn2)
print(dn1)  # 700.6652

dn3 = DecimalNumber(5, 1)
dn4 = DecimalNumber(2, 1)
dn3.multiply(dn4)
print(dn3)  # 1.0 (because 5*2 = 10 and 1+1 = 2, so it is 1.00)