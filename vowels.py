

def countvowels(word):

    count = 0

    for letter in word:
        if letter.__contains__('a'):
            count += 1
        elif letter.__contains__('e'):
            count += 1
        elif letter.__contains__('i'):
            count += 1
        elif letter.__contains__('o'):
            count += 1
        elif letter.__contains__('u'):
            count += 1
        elif letter.__contains__('A'):
            count += 1
        elif letter.__contains__('E'):
            count += 1
        elif letter.__contains__('I'):
            count += 1
        elif letter.__contains__('O'):
            count += 1
        elif letter.__contains__('U'):
            count += 1
    print("There are ", count ," vowel/s in this word.")

userword = input("Enter a word : ")

countvowels(userword)