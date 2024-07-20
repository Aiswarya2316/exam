def find_longest_word(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
    return longest_word

# Example usage:
file_name = 'sample.txt'
longest_word = find_longest_word(file_name)
print("Longest word in the file:", longest_word)
