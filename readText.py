#!/usr/bin/python3

def read_file_content(filename):
    """reads the txt in a file"""
    with open(filename, 'r') as f:
        var = f.read()
        f.close()

    return var


def count_words():
    """counts the no of times a word appear in the txt file"""

    # reads the text file
    text = read_file_content("./story.txt")
    # Create an empty dictionary
    d = dict()

    # Convert the characters in line to lowercase to avoid case mismatch
    line = text.lower()

    # Split the line into words
    words = line.split(" ")
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] += 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])

if __name__ == '__main__':
    count_words()
