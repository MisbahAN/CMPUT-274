# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: Windows
# python version: 3.11.9
from treenode import TreeNode



def read_tree():
    
    # Extracting n and d from first line of input
    line1 = input()
    split_line1 = line1.split()
    n = int(split_line1[0])
    d = int(split_line1[1])

    # Extracting values of nodes from second line of input
    line2 = input()
    values = line2.split()

    # Converting all values that are not '-' to TreeNode object
    for i in range(len(values)):
        if values[i] != '-':
            values[i] = TreeNode(values[i])

    # Assuming first position is root
    root = values[0]

    # Adding d children to parent
    i=0 # Index for parent node in values list
    j=1 # # Starting index of the child nodes for each parent in values list
    while i < n:
        parent = values[i]
        children = values[j: j+d] # Storing values of each child 
        current_pos = j 

        for child in children:
            if child != '-': # Proceed if child is not empty
              values[current_pos] = child # Doesn't add '-' from original array
              parent.add_child(child) # Adds child to its parent
            current_pos += 1

        i += 1 # Move to the next parent node in values
        j += d # Move to the next set of POTENTIAL child nodes in values

    return root
    


def main():
    # Do not modify
    read_tree().print_tree()

if __name__ == '__main__':
    main()