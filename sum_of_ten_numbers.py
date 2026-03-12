#Enter ten numbers
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
#Add ten numbers
total_sum = sum(numbers)

#Output
print(f"The sum of the 10 numbers is {total_sum}")
    