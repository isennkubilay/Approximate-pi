iterations = 1000000
multiplier = 1.0
start_denominator = 2.0
pi = 3.0 

for i in range(1, iterations+1):
  pi += ((4.0 / (start_denominator * (start_denominator + 1.0) * (start_denominator + 2.0))) * multiplier)
  start_denominator += 2.0
  multiplier *= -1.0
print(pi)
