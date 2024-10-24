def permutations(n):
    # Base case: if n is 1, the only permutation is [1]
    if n == 1:
        return [[1]]
    
    # Recursive case: get permutations for n-1
    smaller_permutations = permutations(n - 1)
    
    # Prepare a list to store all permutations of [1, ..., n]
    result = []
    
    # Insert n into every possible position in each permutation of [1, ..., n-1]
    for perm in smaller_permutations:
        for i in range(len(perm) + 1):
            # Create a new permutation by inserting n at position i
            new_perm = perm[:i] + [n] + perm[i:]
            result.append(new_perm)
    
    return result

def main():
    n = int(input("Enter number: "))
    print(permutations(n))

# Call main to run the program
main()