def find_longest_word(sample.txt):
    with open(sample.txt, 'r') as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key=len)
    return longest_word