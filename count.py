def count(text):

    word = 1
    for i in range(len(text)):
        if text[i] == ' ' or text[i] == '/n' or text[i] == '/t':
            word = word + 1
    return word

if __name__ == '__main__':
    num = count("How many words are in this sentence?")
    print(num)
