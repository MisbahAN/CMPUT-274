# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 183574
# operating system: Windows 11
# python version: Python 3.11.9

def analyze_character_frequencies(text):

    """Cleaning the text (removing everything except alphanumeric characters)"""
    clean_text = ""
    for char in text:
        if char.isalnum():
            clean_text += char.lower()

    """Counting character frequencies"""
    frequency_dict = {}
    for char in clean_text:
        if char in frequency_dict:
            frequency_dict[char] += 1  # Increment frequency if character already in dictionary
        else:
            frequency_dict[char] = 1  # Add new character with a frequency of 1

    # If input is empty or non-alphanumeric, return an empty list
    if not frequency_dict:
        return []

    """Sorting characters by frequency, then alphabetically"""
    char_frequency_list = []
    for char, freq in frequency_dict.items():
        char_frequency_list.append((char, freq))

    # Manually implement sorting by frequency (desc), then alphabetically
    for i in range(len(char_frequency_list)):
        for j in range(i + 1, len(char_frequency_list)):
            # First, compare frequency in descending order
            if char_frequency_list[i][1] < char_frequency_list[j][1]:
                char_frequency_list[i], char_frequency_list[j] = char_frequency_list[j], char_frequency_list[i]  # Swapping
            # If frequencies are the same, compare alphabetically (sort by character)
            elif char_frequency_list[i][1] == char_frequency_list[j][1]:
                if char_frequency_list[i][0] > char_frequency_list[j][0]:
                    char_frequency_list[i], char_frequency_list[j] = char_frequency_list[j], char_frequency_list[i]  # Swapping

    # Extract the sorted characters into a list
    sorted_characters = []
    for char, _ in char_frequency_list:
        sorted_characters.append(char)

    return sorted_characters

def main():
    text = input()
    print(analyze_character_frequencies(text))

if __name__ == "__main__":
    main()