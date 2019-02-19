if __name__ == '__main__':
    print("Welcome to hangman!!")
    word = "INSERTWORDHERE"
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("guess letter: ")
    counter = 0
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
            counter += 1
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
            counter += 1
        else:
            print(''.join(guessed))
            if letter is not '':
                lstGuessed.append(letter.upper())
            letter = input("guess letter: ")


        if '_' not in guessed:
            answer = ''.join(guessed)
            print(answer)
            print("You won!!")
            print("It took you {} guesses.".format(counter))
            break