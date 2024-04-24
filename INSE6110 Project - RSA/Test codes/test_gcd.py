import math
def gcd(a, b):
   return math.gcd(a, b)
while True:
  e = int(input("Enter your number 1: "))
  phi_n = int(input("Enter your number 2: "))
  if gcd(e, phi_n) == 1:
    print("Gcd = 1 ")
    break
  else:
      print("They have the GCD")
      break