
import math

def pTriplet():
	for a in range(2, 1001):
  		for b in range(2, 1001):
  			if a < b:
  				if b < math.sqrt(a**2 + b**2):
  					if (math.sqrt(a**2 + b**2)).is_integer():
  						if (a + b + math.sqrt(a**2 + b**2)) == 1000:
  							return a * b * math.sqrt(a**2 + b**2)

result = pTriplet()
print result
