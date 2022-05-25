#!/usr/bin/python3
def find_anagrams(str1, str2):
    """ Check if a word is an anagrams """
    # converts the strings to lower case
    str1.lower()
    str2.lower()
    # check if length is same
    if (len(str1) == len(str2)):

        # sort the strings
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

        # if sorted char arrays are same
        if (sorted_str1 == sorted_str2):
            return True
        else:
            return False

    else:
        return False

print(find_anagrams("hello", "yello"))
print(find_anagrams("race", "care"))
print(find_anagrams("race", "caring"))