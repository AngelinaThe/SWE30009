import operator

# Define basic arithmetic functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y

# List of arithmetic functions to use
operator_functions = [add, subtract, multiply]

def checkConcrete():
    # Iterate through a range of values for 'a'
    for a in range(-100, 100):
        b = 2  # Fixed value for 'b'
        outputs = []  # List to store results of different operations
        
        # Test all combinations of three operators
        for op1 in operator_functions:
            for op2 in operator_functions:
                for op3 in operator_functions:
                    # Apply the operators to compute the intermediate results
                    A = op2(op1(a, b), b)
                    C = op3(A, 5)
                    
                    # Identify the correct expression based on specific operators
                    if op1 == add and op2 == multiply and op3 == subtract:
                        correct_expression = C
                    else:
                        # Store results of incorrect operator combinations
                        outputs.append(C)  
        
        concrete_test = True  # Assume test case is concrete initially
        # Calculate the expected correct result for comparison
        correct_expression = ((a + b) * b) - 5
        
        # Check if the correct expression is present in the outputs
        for out in outputs:
            if correct_expression == out:
                concrete_test = False  # Mark test case as not concrete if match found
                break

        # Print details if the test case is not concrete
        if not concrete_test:
            print(f"When A = {a} and B = 2, it is not a concrete test case")
            print(f"{correct_expression} is present from the output list: {outputs}\n")
            

checkConcrete()
