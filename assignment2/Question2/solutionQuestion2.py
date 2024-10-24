# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: macOS
# python version: Python 3.12.3



def simplify_path(path):
    # Check if the path starts with "/"
    if path[0] != "/":
        return "Invalid Path"

    # Clean the path to remove extra slashes
    stack = remove_slashes(path)

    # Use a user-defined function to remove periods ('.' and '..') from the path
    stack = remove_periods(stack)
    
    # Returning simplified path
    simplified_path = "/" # simplified_path remains "/" if stack is empty
    if stack: # If stack is not empty, join the stack elements with "/" 
        for i in range(len(stack)):
             simplified_path += stack[i] + "/" # Join the stack elements with "/"
        simplified_path = simplified_path[:-1] # Removing the last "/"

    return simplified_path



def remove_slashes(path):
    # Initiating stack
    stack = []
    
    # Store each element of path, removing consecutive slashes
    current = ""
    for i in range(len(path)):
        if path[i] == "/":
            if current:  # Only add if current is not empty
                stack.append(current)
                current = ""  # Reset current for the next component
        else:
            current += path[i]

    # Add the last component if any remaining (spent 1 hour finding this mistake)
    if current:
        stack.append(current)

    return stack



def remove_periods(stack):

    simplified_stack = []

    for element in stack:
        if element == ".":
            continue  # Skip the current directory
        elif element == "..":
            if simplified_stack: # If simplified_stack not empty
                simplified_stack.pop() # Pop last directory
        else:
            simplified_stack.append(element)  # Add valid directories

    return simplified_stack



def main():
    # Takes Unix path as input
    path = input()
    # Simplify the path
    print(simplify_path(path))

if __name__ == "__main__":
    main()