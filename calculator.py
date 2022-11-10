"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_cubes, add_mult)

#setting a forever loop
while True:
    user = input("First enter operator, then your numbers here: \n ")
    
    #user input becomes a token and into a list
    tokens = user.split(" ")                        
  
    if "q" in tokens:
        print("Exit.")
        break

    elif len(tokens) < 2:
        print("Not enough inputs. We need at least 4.")
        continue
       
    #identifying operator starts at index 0 and num1 starts at index 1
    operator = tokens[0]
    num1 = tokens[1]
    
    if len(tokens) < 3:
        num2 = "0"

    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    # storing the value to use when we operate the eqaution
    result = None               

    #.isdigits() checks if either num1 or num2 are digits, if not then it will cont to ask for valid input
    if not num1.isdigit() or not num2.isdigit():            
        print("num1 and num2 is not a valid digit. Please try again.")
        continue
    
    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "power":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    elif operator == "+x":
        result == add_mult(float(num1), float(num2), float(num3))

    elif operator =="+cubes":
        result = add_cubes(num1, num2)
   
    else:
        print("First enter an operator, then two integers.")

    print(result)