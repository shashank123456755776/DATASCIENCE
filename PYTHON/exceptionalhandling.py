# Example of a compile-time error (SyntaxError)
# print("Hello"  # Uncommenting this line will cause a syntax error

# # Example of a run-time error (ZeroDivisionError)
# try:
# 	result = 10 / 0
# except ZeroDivisionError:
# 	print("Run-time error: Division by zero is not allowed.")

# # Example of a logical error
# def add_numbers(a, b):
# 	# Incorrect logic: should be a + b
# 	return a - b

# print("Logical error example: 5 + 3 =", add_numbers(5, 3))  # Output will be 2 instead of 8

# # Corrected logical error
# def add_numbers_correct(a, b):
# 	return a + b

# print("Corrected: 5 + 3 =", add_numbers_correct(5, 3))  


# wo part jaha error ho sakta wo code try ke under likha ta 
# except mai error aaega to kya karenge

try:
    num=int(input("enter anumber:"))
    num1=10/num
    print(f"result is {num1}")
except ZeroDivisionError:
    print("number cannot be divided by 0")
except SyntaxError:
    print("number cannot be dividede by diffrent data types except numbers")
            



