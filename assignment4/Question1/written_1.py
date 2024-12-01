def push_with_priority(stack, priority, element):
    temp_stack = []

    # Create the item with its priority
    item = (priority, element)

    if len(stack) == 0:
        stack.append(item)
    else:
        # Move elements to the temporary stack until the right position is found
        while item[0] > stack[-1][0]:
            temp_stack.append(stack.pop())
        
        # Insert the new element in the correct position
        stack.append(item)

        # Move the elements back from the temporary stack to the main stack
        while len(temp_stack) != 0:
            stack.append(temp_stack.pop())
            
stack = []
push_with_priority(stack, 3, "A")
push_with_priority(stack, 1, "B")
push_with_priority(stack, 2, "C")
print(stack)  # Output: [(3, 'A'), (2, 'C'), (1, 'B')]