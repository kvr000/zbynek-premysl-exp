from decimal import Decimal, getcontext

getcontext().prec = 6  # Set precision to 6 decimal places
intermediate_result = Decimal('1.2') - Decimal('1.0')
final_result = float(intermediate_result)  # Convert back to float if needed
print(f"Intermediate Result: {intermediate_result}\nFinal Result: {final_result}")