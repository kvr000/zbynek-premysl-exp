from decimal import Decimal, getcontext

getcontext().prec = 4
result = Decimal('1.2') - Decimal('1.0')
print(f"High Precision Result: {result}")