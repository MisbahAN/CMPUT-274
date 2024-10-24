# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: macOS
# python version: Python 3.12.3

def fractal_eval(expr):
    
    # Base case: If there are no square brackets, simply evaluate the expression using the built-in eval function
    if '[' not in expr:
        return eval(expr) # int
    
    # Using stack to find the innermost square brackets
    stack = []
    start_of_square_brackets = -1  # Stores index position of the last '['

    # Iterate through the expression to find the innermost square brackets
    for i in range(len(expr)):
        if expr[i] == '[':
            stack.append(i)  # Push the index of '[' to the stack 
        elif expr[i] == ']':
            start_of_square_brackets = stack.pop()  # Get the LAST unmatched '['
            end_of_square_brackets = i
            break

    # Get the innermost expression between the square brackets
    inner_expr = expr[start_of_square_brackets + 1 : end_of_square_brackets] # str
    
    # Recursively evaluate the inner expression
    inner_result = fractal_eval(inner_expr) # int
    
    # Replace the innermost square bracket expression with its squared result
    new_expr = expr[:start_of_square_brackets] + str(inner_result ** 2) + expr[end_of_square_brackets + 1:] # str
    
    # Recursively evaluate the new expression
    return fractal_eval(new_expr)

def main():
    exp = input()
    print(round(fractal_eval(exp)))

if __name__ == "__main__":
    main()