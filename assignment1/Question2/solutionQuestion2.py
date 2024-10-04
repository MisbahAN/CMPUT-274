# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: macOS
# python version: 3.12.3



#Input: The given input string
#Output: The "clean" version of the input string without characters specified in the problem statement like ?, !, etc
def clean_input_string(inputString):

    # Removing ".", ",", "!", "?", and "'" from inputString
    cleanedString = ""
    for char in inputString:
        if char not in [".", ",", "!", "?", "'"]:
            cleanedString += char

    return cleanedString



#Input: The output from clean_input_string()
#Output: The reversed version of the input string
def reverse_string(cleanedString):

    # Creating a list of cleanedString in reverse
    reversedStringlist = cleanedString.split()
    reversedStringlist = reversedStringlist[::-1]

    # Storing reversedStringlist in a sentence structure rather than list
    reversedString = ""
    for word in reversedStringlist:
        reversedString += word + " " # Add a space after each word

    return reversedString



#Input: The output from reverse_string()
#Output: A string with all the duplicate occurrences of words removed. Only the first occurrence will remain in the string
def remove_duplicates(reversedString):
    reversedStringList = reversedString.split()

    # Removing duplicated words from reversedStringList and storing in reversedStringWithoutDuplicatesList
    reversedStringWithoutDuplicatesList = []
    for word in reversedStringList:
        if word not in reversedStringWithoutDuplicatesList:
            reversedStringWithoutDuplicatesList.append(word)
    
    # Storing reversedStringWithoutDuplicatesList in a sentence structure rather than list
    reversedStringWithoutDuplicates = ""
    for word in reversedStringWithoutDuplicatesList:
        reversedStringWithoutDuplicates += word + " " # Add a space after each word
    
    return reversedStringWithoutDuplicates



#Input: The output from remove_duplicates()
#Output: The median length of the words in the input string. This function must return an integer, more specifically the floor value.
def calculate_median_length(reversedStringWithoutDuplicates):
    list_of_words = reversedStringWithoutDuplicates.split()
    len_of_words_in_list = []

    for word in list_of_words:
        len_of_words_in_list.append(len(word))

    # Sorting to get median 
    len_of_words_in_list = sorted(len_of_words_in_list) 

    # Printing value of median for either odd or even number of reversedStringWithoutDuplicates 
    mid = len(len_of_words_in_list) // 2
    if len(len_of_words_in_list) % 2 == 0:
        medianWordLength = (len_of_words_in_list[mid -1] + len_of_words_in_list[mid]) // 2
    else:
        medianWordLength = len_of_words_in_list[mid]

    return medianWordLength



def main():
    inputString = input()

    cleanedString = clean_input_string(inputString)
    
    reversedString = reverse_string(cleanedString)
    print(reversedString)
    
    reversedStringWithoutDuplicates = remove_duplicates(reversedString)
    print(reversedStringWithoutDuplicates)
    
    medianWordLength = calculate_median_length(reversedStringWithoutDuplicates)
    print(medianWordLength)

    
if __name__ == "__main__":
    main()