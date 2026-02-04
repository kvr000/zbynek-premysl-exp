import math

n1 = 5.6
n2 = -2.6

# Positive number
data = math.trunc(n1)
print("Truncated (positive):", data, ', Type:', type(data).__name__)

# Negative number
val = math.trunc(n2)
print("Truncated (negative):", val, ', Type:', type(val).__name__)
