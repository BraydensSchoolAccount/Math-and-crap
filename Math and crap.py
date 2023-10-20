# Math and Python
# Brayden Towner
# 10/6/23

import math

# Get user inputs for the quadratic formula.
print("For the quadratic formula,")
quad_a_val  = float(input("What is 'a'? - "))
quad_b_val = float(input("What is 'b'? - "))
quad_c_val = float(input("What is 'c'? - "))

# Because this is used multiple times, I put it in a value to make the code easier to read.
# This is the solution to the square root section of the quadratic formula
# √b^2-4ac

quad_discriminant = (quad_b_val ** 2) - (4 * quad_a_val * quad_c_val)
print(quad_discriminant)

# Declaring the variables for the quadratic solution
# This is the easiest way to compensate for the +- symbol
quad_solution = (-quad_b_val - math.sqrt(quad_discriminant)) / 2j * quad_a_val
quad_solution = (-quad_b_val + math.sqrt(quad_discriminant)) / 2j * quad_a_val

print(f"\nThe solution for the quadratic equation is {quad_solution}")

