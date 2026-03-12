odd_numbers = 0
for i in range(10):
    if float(input(f"Enter number {i+1}: ")) % 2 != 0:
        odd_numbers += 1
#output
print(f"Odds: {odd_numbers}")
