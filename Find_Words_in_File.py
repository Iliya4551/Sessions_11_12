def find_words(filename):
    """
    Prints the 3 letter words starting with b
    :param filename: the name of the file
    :return: nothing
    """
    with open(filename, 'r') as f:
        for line in f:

            #We need to breakdown the line into words
            words = line.split() # it splits by space on it's own
            # Check each word
            for word in words:
                if len(word) == 3 and word()[0] == "Bb" :#Len is the size of the word (Length)
                    print(word)

find_words("input.txt")